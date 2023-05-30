from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.WorkerList.as_view(), name='index'),
    path('index', views.WorkerList.as_view(), name='index'),
    path('add_worker', views.add_worker, name='add_worker'),
    path('best_worker', views.best_worker, name='best_worker'),
    path('check', views.check, name='check'),
    path('worker_detail/<int:pk>', views.WorkerDetail.as_view(), name='worker_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)