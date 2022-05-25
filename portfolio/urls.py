from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio, name="portfolio-home"),
    path('project/<int:pk>/', views.project, name="project-detail"),
]