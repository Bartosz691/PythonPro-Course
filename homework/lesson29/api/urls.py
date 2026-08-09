
from django.urls import path

from . import views


urlpatterns = [
    path("hello/", views.hello_celery),
    path("multiply/", views.multiply_view),
    path("process-video/", views.process_video_view),
    path("start-progress/", views.start_progress_task),
    path("task-status/<str:task_id>/", views.task_status),
]