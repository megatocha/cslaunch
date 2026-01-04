from fastapi import APIRouter, Request, Form, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from app.services import CodeService
from app.config import settings

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    """Страница входа"""
    return templates.TemplateResponse("login.html", {
        "request": request,
        "error": None
    })


@router.post("/login")
async def login(request: Request, code: str = Form(...)):
    """Обработка авторизации"""
    # Проверка админского пароля
    if code == settings.ADMIN_PASSWORD:
        request.session["authenticated"] = True
        request.session["admin_auth"] = True
        return RedirectResponse(url="/admin", status_code=status.HTTP_303_SEE_OTHER)
    
    # Проверка кода доступа
    if CodeService.validate_code(code):
        request.session["authenticated"] = True
        request.session["user_code"] = code
        return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
    
    # Ошибка авторизации
    return templates.TemplateResponse("login.html", {
        "request": request,
        "error": "Неверный код доступа"
    }, status_code=status.HTTP_401_UNAUTHORIZED)


@router.get("/logout")
async def logout(request: Request):
    """Выход из системы"""
    request.session.clear()
    return RedirectResponse(url="/login", status_code=status.HTTP_303_SEE_OTHER)