from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_id>/connections/', views.connections, name='connections'),
    path('add_user/', views.add_user, name='add_user'),
    path('<int:user_id>/connections/find_user/', views.find_user, name='find_user'),
    path('<int:user_id>/connections/connect_user/', views.connect_user, name='connect_user'),
]
