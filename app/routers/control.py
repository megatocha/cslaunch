from fastapi import APIRouter, Depends

from app.dependencies import require_auth
from app.services import CS2Service, StatsService
from app.models import StatusResponse, OperationResponse

router = APIRouter()


@router.get("/get-status", response_model=StatusResponse)
async def get_status(session: dict = Depends(require_auth)):
    """Получить статус сервера"""
    stats = StatsService.get_stats()
    is_running = CS2Service.is_running()
    ping = CS2Service.get_ping()
    
    # Обновление времени старта
    if is_running and stats.start_time is None:
        import time
        StatsService.set_start_time(time.time())
        stats = StatsService.get_stats()
    elif not is_running and stats.start_time is not None:
        StatsService.set_start_time(None)
        stats = StatsService.get_stats()
    
    return StatusResponse(
        running=is_running,
        ping=ping,
        launches=stats.launches,
        start_time=stats.start_time
    )


@router.post("/start-cs2", response_model=OperationResponse)
async def start_cs2(session: dict = Depends(require_auth)):
    """Запустить CS2"""
    if CS2Service.is_running():
        return OperationResponse(
            success=False,
            message="Игра уже запущена"
        )
    
    success = CS2Service.start()
    
    if success:
        return OperationResponse(
            success=True,
            message="Команда запуска отправлена"
        )
    else:
        return OperationResponse(
            success=False,
            error="Ошибка при запуске"
        )


@router.post("/stop-cs2", response_model=OperationResponse)
async def stop_cs2(session: dict = Depends(require_auth)):
    """Остановить CS2"""
    success = CS2Service.stop()
    
    if success:
        return OperationResponse(
            success=True,
            message="Процесс завершен"
        )
    else:
        return OperationResponse(
            success=False,
            error="Ошибка при остановке"
        )