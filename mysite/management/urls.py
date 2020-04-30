from django.urls import path

from . import views

urlpatterns = [
    path('add_admin/', views.register, name='add_admin'),
    path('delete_admin/', views.delete_admin, name='delete_admin'),
]