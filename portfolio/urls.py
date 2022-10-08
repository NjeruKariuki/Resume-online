from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio, name="portfolio-home"),
    path('contact/', views.send_mail)
    path('project/<int:pk>/', views.project, name="project-detail"),
    path('resume/', views.resume, name="resume"),
]