from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class AccessCode(BaseModel):
    """Модель кода доступа"""
    code: str = Field(..., min_length=4, max_length=20)
    note: str = Field(default="Друг", max_length=100)
    created_at: str = Field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M"))


class LoginRequest(BaseModel):
    """Запрос авторизации"""
    code: str = Field(..., min_length=4)


class GenerateCodeRequest(BaseModel):
    """Запрос генерации кода"""
    note: str = Field(default="Друг", max_length=100)


class DeleteCodeRequest(BaseModel):
    """Запрос удаления кода"""
    code: str


class StatusResponse(BaseModel):
    """Ответ статуса сервера"""
    running: bool
    ping: str
    launches: int
    start_time: Optional[float]


class OperationResponse(BaseModel):
    """Стандартный ответ операции"""
    success: bool
    message: Optional[str] = None
    error: Optional[str] = None


class GenerateCodeResponse(OperationResponse):
    """Ответ генерации кода"""
    code: Optional[str] = None


class Stats(BaseModel):
    """Статистика сервера"""
    launches: int = 0
    start_time: Optional[float] = None