from fastapi import Request, HTTPException, status
from fastapi.responses import RedirectResponse


async def require_auth(request: Request):
    """Проверка авторизации пользователя"""
    if not request.session.get("authenticated"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication required"
        )
    return request.session


async def require_admin(request: Request):
    """Проверка прав администратора"""
    if not request.session.get("admin_auth"):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )
    return request.session


def redirect_if_not_auth(request: Request):
    """Редирект на логин если не авторизован (для HTML страниц)"""
    if not request.session.get("authenticated"):
        return RedirectResponse(url="/login", status_code=status.HTTP_303_SEE_OTHER)
    return None