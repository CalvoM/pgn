from django import forms
from django.utils.datastructures import MultiValueDict

from past_chess.tasks import parse_uploaded_file_task


class UploadFileForm(forms.Form):
    file = forms.FileField()

    def parse_uploaded_file(self, file: MultiValueDict):
        task_id = parse_uploaded_file_task.delay(list(file.chunks()))
        return task_id
