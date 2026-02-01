from pydantic_settings import BaseSettings
from functools import lru_cache
import logging
import os


class Settings(BaseSettings):
    """Настройки приложения"""

    # Логирование
    LOGS_PATH: str = "logs/" # Путь к файлу логов
    COLORS: bool = True # Включить цветной вывод в консоли
    EMOJIS: bool = True  # Включить эмодзи в логах
    
    # Безопасность
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-change-this")
    ADMIN_PASSWORD: str = os.getenv("ADMIN_PASSWORD", "admin123")
    
    # Сервер
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", 8000))
    DEBUG: bool = os.getenv("DEBUG", "True").lower() in ("true", "1", "yes")
    
    # Файлы данных
    STATS_FILE: str = "data/stats.json"
    CODES_FILE: str = "data/codes.json"
    
    # Сессии
    SESSION_MAX_AGE: int = 3600  # 1 час

    # Интеграция с Telegram
    TELEGRAM_BOT_TOKEN: str = os.getenv("TELEGRAM_BOT_TOKEN", "")
    
    ALLOWED_TELEGRAM_IDS: list[int] = os.getenv("ALLOWED_TELEGRAM_IDS", "")
    
    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    """Получение синглтона настроек"""
    return Settings()


settings = get_settings()


# === НАСТРОЙКА ЛОГИРОВАНИЯ ===

class Colors:
    # Основные цвета
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    
    # Цвета текста
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Яркие цвета
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    
    # Цвета фона
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'

#? Можно ли изменять? Да!
class Changeable:
    # Цвета для разных уровней логирования
    COLORS = {
        'DEBUG': Colors.BRIGHT_BLACK,
        'INFO': Colors.BRIGHT_GREEN,
        'WARNING': Colors.BRIGHT_YELLOW,
        'ERROR': Colors.BRIGHT_RED,
        'CRITICAL': Colors.BRIGHT_RED + Colors.BOLD
    }

    # Эмодзи для разных уровней логирования
    EMOJIS = {
        'DEBUG': '🔍 ',
        'INFO': 'ℹ️  ',
        'WARNING': '⚠️  ',
        'ERROR': '❌ ',
        'CRITICAL': '🚨 '
    }

    # Форматы даты и времени
    FILE_DATEFMT = '%Y-%m-%d %H:%M:%S'
    CONSOLE_DATEFMT = '%H:%M:%S'

class ColoredFormatter(logging.Formatter):
    def format(self, record):
        # Базовое форматирование
        log_message = super().format(record)
        
        # Добавляем цвета для консольного вывода
        if hasattr(record, 'levelname') and record.levelname in Changeable.COLORS:
            color = Changeable.COLORS[record.levelname]
            reset = Colors.RESET

            # Эмодзи для разных уровней
            if Changeable.EMOJIS:
                emoji = Changeable.EMOJIS.get(record.levelname, '')
            else:
                emoji = ''
            
            # Сообщение с цветом и эмодзи
            formatted_message = f"{color}{emoji}{log_message}{reset}"
            return formatted_message
        
        return log_message

def setup_logging(logger):
    logger.setLevel(logging.DEBUG)
    logger.handlers.clear()

    path = settings.LOGS_PATH
    os.makedirs(path, exist_ok=True)
    
    # Форматтер для файла (без цветов)
    file_formatter = logging.Formatter(
        '%(asctime)s | %(name)s | %(levelname)s | %(message)s',
        datefmt=Changeable.FILE_DATEFMT
    )
    
    # Форматтер для консоли (с цветами)
    if Changeable.COLORS:
        console_formatter = ColoredFormatter(
            '%(asctime)s [%(levelname)s] %(message)s',
            datefmt=Changeable.CONSOLE_DATEFMT
        )
    else:
        console_formatter = logging.Formatter(
        '%(asctime)s [%(levelname)s] %(message)s',
        datefmt=Changeable.CONSOLE_DATEFMT
    )
    
    # Обработчик для файла
    file_handler = logging.FileHandler(
        path + f"{logger.name}.log", 
        encoding='utf-8'
    )
    file_handler.setFormatter(file_formatter)
    file_handler.setLevel(logging.DEBUG)
    
    # Обработчик для консоли
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(console_formatter)
    console_handler.setLevel(logging.DEBUG)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger