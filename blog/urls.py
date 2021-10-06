from django.urls import path
from .views import PostListView,PostDetailView,PostCreateView,LikeView
from . import views
from django.shortcuts import render
urlpatterns = [
    path('', PostListView.as_view(), name = 'blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'),
    path('post/new/', PostCreateView.as_view(), name = 'post-create'),
    path('about/',views.about, name = 'blog-about'),
    path('like/<int:pk>',LikeView, name='like-post'),
]
