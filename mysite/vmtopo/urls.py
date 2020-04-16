from django.urls import path

from . import views

urlpatterns = [
    path('', views.vmtopo, name='vmtopo'),
    path('topo/', views.topo, name='topo'),
]