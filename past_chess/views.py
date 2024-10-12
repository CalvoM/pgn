# pyright:reportUnnecessaryComparison=false,reportArgumentType=false
import json

from celery.result import AsyncResult
from django import forms
from django.core.serializers import serialize
from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST

from past_chess.models import Game, ModelJsonSerializer
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
@require_GET
def filter_gamees(request: HttpRequest):
    findings = Game.objects.all()
    white_player = request.GET.get("white")
    if white_player:
        findings = findings.filter(white__contains=white_player)
    black_player = request.GET.get("black")
    if black_player:
        findings = findings.filter(black__contains=black_player)
    event = request.GET.get("event")
    if event:
        findings = findings.filter(event__contains=event)
    site = request.GET.get("site")
    if site:
        findings = findings.filter(site__contains=site)
    date = request.GET.get("date")
    if date:
        findings = findings.filter(date__date=date)
    round = request.GET.get("round")
    if round:
        findings = findings.filter(round=round)
    result = request.GET.get("result")
    if result:
        findings = findings.filter(result=result)

    serialize
    ret = ModelJsonSerializer().serialize(
        queryset=findings,
        fields=("event", "site", "white", "black"),
        use_natural_foreign_keys=True,
        use_natural_primary_keys=True,
    )
    return JsonResponse(json.loads(ret), safe=False)
