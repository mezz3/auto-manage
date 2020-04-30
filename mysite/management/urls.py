from django.urls import path

from . import views

urlpatterns = [
    path('add_admin/', views.register, name='add_admin'),
    path('delete_admin/', views.search_admin, name='delete_admin'),
    path('delete_admin/delete/<int:user_id>/', views.delete, name='delete'),
]