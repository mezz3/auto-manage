from django.urls import path

from . import views

urlpatterns = [
    path('', views.vmtopo, name='vmtopo'),
    path('topo/delete_port/<str:pg_name>', views.del_port, name='del_port'),
    path('topo/<str:pg_name>', views.topo, name='topo'),
    path('topo/start_vm/<str:vm_name>', views.start_vm, name='start_vm'),
    path('topo/stop_vm/<str:vm_name>', views.stop_vm, name='stop_vm'),
    path('topo/remove_vm/<str:vm_name>', views.remove_vm, name='remove_vm'),
    path('vm_portgroup/', views.vm_pg, name='vm_pg'),
    path('vm_portgroup/create_VM/', views.createVM_pg, name='createVM_pg'),
    path('vm_portgroup/create_VM/port_group/<str:pg_name>', views.choose_pg, name='choose_pg'),
]