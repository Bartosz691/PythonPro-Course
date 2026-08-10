
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path("hello/", views.hello_celery),
    path("multiply/", views.multiply_view),
    path("process-video/", views.process_video_view),
    path("start-progress/", views.start_progress_task),
    path("task-status/<str:task_id>/", views.task_status),
    path(
    "generate-report/",
    views.generate_report_view,
),
path(
    "report-status/<str:task_id>/",
    views.report_status_view,
),
path("upload-image/", views.upload_image_view),
path("start-chain/", views.start_chain_view),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)