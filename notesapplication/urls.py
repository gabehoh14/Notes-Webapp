from django.urls import path
from . import views

urlpatterns = [
    path('', views.take_notes)
]