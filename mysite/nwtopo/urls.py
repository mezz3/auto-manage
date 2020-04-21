from django.urls import path

from . import views

urlpatterns = [
    path('', views.nwtopo, name='nwtopo'),
    path('topo_nw/', views.topo, name='topo_nw'),
]