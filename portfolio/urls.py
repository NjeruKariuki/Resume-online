from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio, name="portfolio-home"),
    path('resume/', views.resume, name="portofolio-resume"),
]