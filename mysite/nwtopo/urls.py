from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.nwtopo, name='nwtopo'),
    path('topo_nw/', views.topo, name='topo_nw'),
    path('deploy/', views.deploy, name='deploy'),
    path('ip_report/', views.report, name='report'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)