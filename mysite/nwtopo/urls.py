from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.nwtopo, name='nwtopo'),
    path('temp_del/<int:temp_id>/<str:temp_name>', views.temp_del, name='temp_del'),
    path('temp_clone/<str:temp_name>', views.temp_clone, name='temp_clone'),
    path('topo_nw/', views.topo, name='topo_nw'),
    path('deploy/', views.deploy, name='deploy'),
    path('deploy/deploy_temp/<str:temp_name>', views.deploy_temp, name='deploy_temp'),
    path('ip_report/', views.report, name='report'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)