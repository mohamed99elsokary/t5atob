from django.urls import path
from . import views

urlpatterns = [
    path("lecture/<int:id>", views.lecture),
]
