from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [
    path('', views.WorkerList.as_view(), name='index'),
    path('index', views.WorkerList.as_view(), name='index'),
    path('worker_create', views.WorkerCreate.as_view(), name='worker_create'),
    path('best_worker', views.best_worker, name='best_worker'),
    path('worker_update/<int:pk>', views.WorkerUpdate.as_view(), name='worker_update'),
    path('worker_delete/<int:pk>', views.WorkerDelete.as_view(), name='worker_delete'),
    path('worker_detail/<int:pk>', views.WorkerDetail.as_view(), name='worker_detail'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)