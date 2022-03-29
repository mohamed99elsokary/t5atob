from django.urls import path
from . import views

urlpatterns = [
    path("category/<int:id>", views.category),
]
