from django.urls import path

from . import views

urlpatterns = [
    path('', views.vmtopo, name='vmtopo'),
    path('topo/<str:pg_name>', views.topo, name='topo'),
    path('topo/delete_port/<str:pg_name>', views.del_port, name='del_port'),
]