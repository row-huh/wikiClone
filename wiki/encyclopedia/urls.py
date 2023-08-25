from django.urls import path

from . import views

urlpatterns = [
    path("wiki/", views.index, name="index"),
    path("wiki/search", views.searchEntry, name="search"),
    path("wiki/<str:title>", views.loadEntry, name="title"),
]