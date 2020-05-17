from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# from django.conf.urls import patterns, url
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('', views.nwtopo, name='nwtopo'),
    path('temp_del/<int:temp_id>/<str:temp_name>', views.temp_del, name='temp_del'),
    path('temp_clone/<str:temp_name>', views.temp_clone, name='temp_clone'),
    path('topo_nw/', views.topo, name='topo_nw'),
    path('deploy/', views.deploy, name='deploy'),
    path('deploy/deploy_temp/', views.deploy_temp, name='deploy_temp'),
    path('deploy/deploy_temp/succ/<str:temp_name>', views.deploy_temp_succ, name='deploy_temp_succ'),
    path('ip_report/', views.report, name='report'),
    path('ip_report/delete/<str:deploy_name>', views.deploy_del, name='deploy_del'),

    path(r'^remote_admin/$', RedirectView.as_view(url='http://10.0.15.21/static/web-ui/server/1/project/9c278930-5a87-4b14-b2fb-7a11bd957e08'),
        name='remote_admin'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)