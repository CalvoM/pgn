# pyright:reportUnnecessaryComparison=false,reportArgumentType=false
from celery.result import AsyncResult
from django import forms
from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST

from pgn_web import celery_app

from .forms import UploadFileForm


@csrf_exempt
@require_POST
def upload_game_file(request: HttpRequest):
    form: forms.Form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
        uploaded_file = request.FILES.get("file")
        task_res: AsyncResult = form.parse_uploaded_file(uploaded_file)
        ret_task: dict[str, str | None] = {"tracking_id": task_res.task_id}
        return JsonResponse(ret_task)


@require_GET
def check_upload_status(request: HttpRequest, task_id: str):
    response: AsyncResult = celery_app.AsyncResult(task_id)
    ret_status: dict[str, str | bool] = {
        "status": response.status,
        "success": response.successful(),
    }
    return JsonResponse(ret_status)


@csrf_exempt
@require_POST
def filter_gamees(request: HttpRequest):
    print(request.body)
    return JsonResponse([1, 2, 3], safe=False)
