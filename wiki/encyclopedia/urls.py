from django.urls import path

from . import views

urlpatterns = [
    path("wiki/", views.index, name="index"),
    path("wiki/search", views.searchEntry, name="search"),
    path("wiki/create", views.create, name="create"),
    path("wiki/createentry", views.createEntry, name="createentry"),
    path("wiki/random", views.randompage, name="random"),
    path("wiki/edit/<str:title>", views.editpage, name="edit"),
    path("wiki/saveentry", views.saveEntry, name="saveentry"),
    path("wiki/<str:title>", views.loadEntry, name="title"),
]