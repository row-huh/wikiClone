from django.urls import path

from . import views

urlpatterns = [
    path("wiki", views.index, name="index"),
    path("wiki/<str:title>", views.loadEntry, name="title"),
    path("wiki/?q=<str:entry>", views.searchEntry, name="search")
]