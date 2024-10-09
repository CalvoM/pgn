from typing import Any

from celery.result import AsyncResult
from django import forms
from django.core.files.uploadedfile import UploadedFile

from past_chess.tasks import parse_uploaded_file_task


class UploadFileForm(forms.Form):
    file = forms.FileField()

    def parse_uploaded_file(self, file: UploadedFile) -> AsyncResult:
        task_res: AsyncResult = parse_uploaded_file_task.delay(list(file.chunks()))
        return task_res
