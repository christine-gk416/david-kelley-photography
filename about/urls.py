from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    # path('success/', views.successView, name='success'),
]