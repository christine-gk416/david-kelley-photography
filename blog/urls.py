from . import views
from django.urls import path

urlpatterns = [
    # path('all_posts.html', views.PostList.as_view(), name='blog'),
    path('', views.blog, name='blog'),
    # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug>', views.post_detail, name='post_detail')
]