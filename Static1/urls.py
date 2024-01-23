from django.urls import path
from . import views
from Static1 import views

urlpatterns = [
    path("", views.index, name="index"),
    path("form", views.add, name="form" )
]
