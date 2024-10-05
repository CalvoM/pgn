import json

from celery.result import AsyncResult
from django import forms
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from pgn_web import celery_app

from .forms import UploadFileForm


def home(request: HttpRequest):
    return render(request, "past_chess/index.html")


@csrf_exempt
def upload_game_file(request: HttpRequest):
    if request.method == "POST":
        form: forms.Form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            task_res = form.parse_uploaded_file(request.FILES["file"])
            return HttpResponse(task_res.task_id)
    else:
        return HttpResponse("No Bye")


def check_upload_status(request: HttpRequest, task_id: str):
    if request.method == "GET":
        response: AsyncResult = celery_app.AsyncResult(task_id)
        return render(
            request,
            "past_chess/upload_status.html",
            {
                "status": response.state,
                "success": response.successful(),
                "value": response.result,
            },
        )
    else:
        return HttpResponse("No bye")
