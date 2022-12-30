from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('read/<int:manga_id>/', views.read_manga, name="read_manga"),
    path('manga/create/', views.create_manga, name="create_manga"),
    path('manga/update/', views.update_manga, name="update_manga"),
    path('manga/delete/', views.delete_manga, name="delete_manga"),
]
