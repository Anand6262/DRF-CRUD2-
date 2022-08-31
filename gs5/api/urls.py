from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('stucreate/', views.StudentAPI.as_view()),
]