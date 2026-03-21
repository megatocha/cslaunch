import asyncio
import logging
import sys
import time

from aiogram import Bot, Dispatcher, F, types
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.exceptions import TelegramBadRequest

import app.config as config
from app.config import settings
from app.services import CS2Service, StatsService

log = config.setup_logging(logging.getLogger("__name__"))

bot = Bot(token=settings.TELEGRAM_BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()

# --- ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ---

def get_uptime(start_time):
    """Красивый формат времени работы"""
    if not start_time:
        return "00:00:00"
    diff = int(time.time() - start_time)
    hours = diff // 3600
    minutes = (diff % 3600) // 60
    seconds = diff % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def get_dashboard_data(starting=False):
    """Собирает текст и клавиатуру для сообщения"""
    is_running = CS2Service.is_running()
    stats = StatsService.get_stats()
    
    if is_running and stats.start_time is None:
        StatsService.set_start_time(time.time())
        stats = StatsService.get_stats()
    elif not is_running and stats.start_time is not None:
        StatsService.set_start_time(None)
        stats = StatsService.get_stats()

    status_icon = "🟣 STARTING..." if starting else "🟢 ONLINE!" if is_running else "🔘 OFFLINE."
    uptime = get_uptime(stats.start_time)
    
    text = (
        f"<b>Статус:</b> {status_icon}\n"
        f"<b>Время сессии:</b> {uptime}\n"
        f"<b>Всего запусков:</b> {stats.launches}"
    )
    
    kb = InlineKeyboardBuilder()

    if is_running:
        kb.button(text="⏹ ОСТАНОВИТЬ", callback_data="stop_cs2")
    else:
        kb.button(text="▶️ ЗАПУСТИТЬ", callback_data="start_cs2")
        
    kb.button(text="🔄 Обновить статус", callback_data="refresh")
    kb.adjust(2)

    return text, kb.as_markup()

# --- HANDLERS (ОБРАБОТЧИКИ) ---

@dp.update.outer_middleware
async def check_access(handler, event, data):
    user_id = None
    if event.message:
        user_id = event.message.from_user.id
    elif event.callback_query:
        user_id = event.callback_query.from_user.id
        
    if user_id and user_id not in settings.ALLOWED_TELEGRAM_IDS:
        if event.message:
            await event.message.answer("⛔️ Доступ запрещен.")
        return
        
    return await handler(event, data)


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    """Обработчик команды /start"""
    text, reply_markup = get_dashboard_data()
    await message.answer(text, reply_markup=reply_markup, parse_mode="HTML")


@dp.callback_query(F.data == "refresh")
async def process_refresh(callback: types.CallbackQuery):
    """Кнопка обновления"""
    text, reply_markup = get_dashboard_data()
    try:
        await callback.message.edit_text(text, reply_markup=reply_markup, parse_mode="HTML")
    except TelegramBadRequest:
        pass
    await callback.answer("Данные обновлены!")


@dp.callback_query(F.data == "start_cs2")
async def process_start(callback: types.CallbackQuery):
    """Запуск игры"""
    log.debug("Запуск CS2...")
    
    if CS2Service.is_running():
        await callback.answer("Игра уже запущена!", show_alert=True)
    else:
        success = CS2Service.start()
        if not success:
            await callback.answer("Ошибка при запуске!", show_alert=True)
            log.error(f"Ошибка при запуске: {success}")
    
    await callback.answer("Запуск CS2...")
    text, reply_markup = get_dashboard_data(True)
    await callback.message.edit_text(text, reply_markup=reply_markup, parse_mode="HTML")
    await asyncio.sleep(4)
    text, reply_markup = get_dashboard_data()
    await callback.message.edit_text(text, reply_markup=reply_markup, parse_mode="HTML")


@dp.callback_query(F.data == "stop_cs2")
async def process_stop(callback: types.CallbackQuery):
    """Остановка игры"""
    await callback.answer("Остановка CS2...")
    log.debug("Остановка CS2...")
    
    CS2Service.stop()
    
    await asyncio.sleep(3)
    text, reply_markup = get_dashboard_data()
    await callback.message.edit_text(text, reply_markup=reply_markup, parse_mode="HTML")


# --- ЗАПУСК ---
async def main():
    log.info("🤖 Бот запущен!")
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    if not settings.TELEGRAM_BOT_TOKEN:
        log.error("Не указан TELEGRAM_BOT_TOKEN в .env")
        sys.exit(1)
    
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        log.info("Бот остановлен!")