from django.urls import path

from . import views

urlpatterns = [
    # path("games/"),
    path("games/filtered-results", views.filter_gamees, name="filter_games"),
    path("upload/", views.upload_game_file, name="upload"),
    path(
        "upload/status/<str:task_id>",
        views.check_upload_status,
        name="upload_task_status",
    ),
]
