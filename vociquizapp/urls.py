from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("vocabulary/<int:vocabulary_id>/menu/", views.menu, name="menu"),
    path("vocabulary/<int:vocabulary_id>/vocicard/", views.vocicard, name="vocicard"),
]
