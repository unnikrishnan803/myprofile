from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vlogs/', views.vlogs, name='vlogs'),
    path('projects/', views.projects, name='projects'),
]