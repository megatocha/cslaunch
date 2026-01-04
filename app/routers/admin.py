from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from app.dependencies import require_admin
from app.services import CodeService
from app.models import GenerateCodeRequest, DeleteCodeRequest, GenerateCodeResponse, OperationResponse

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("", response_class=HTMLResponse)
async def admin_panel(request: Request):
    """Админ-панель"""
    # Проверка авторизации
    if not request.session.get("admin_auth"):
        return RedirectResponse(url="/login")
    
    codes = CodeService.get_codes()
    return templates.TemplateResponse("admin.html", {
        "request": request,
        "codes": codes
    })


@router.post("/generate", response_model=GenerateCodeResponse)
async def generate_code(
    data: GenerateCodeRequest,
    session: dict = Depends(require_admin)
):
    """Сгенерировать новый код"""
    new_code = CodeService.add_code(note=data.note)
    return GenerateCodeResponse(
        success=True,
        code=new_code.code,
        message="Код успешно создан"
    )


@router.post("/delete", response_model=OperationResponse)
async def delete_code(
    data: DeleteCodeRequest,
    session: dict = Depends(require_admin)
):
    """Удалить код"""
    success = CodeService.delete_code(data.code)
    
    if success:
        return OperationResponse(
            success=True,
            message="Код успешно удален"
        )
    else:
        return OperationResponse(
            success=False,
            error="Код не найден"
        )