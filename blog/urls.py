from . import views
from django.urls import path

urlpatterns = [

    path('', views.blog, name='blog'),
    path('<slug:slug>', views.post_detail, name='post_detail'),
    path('add/', views.add_post, name='add_post'),
    path('edit/<slug:slug>/', views.edit_post, name='edit_post'),
    path('delete/<slug:slug>/', views.delete_post, name='delete_post'),
    path('like/<slug:slug>/', views.like_post, name='like_post'),
]
