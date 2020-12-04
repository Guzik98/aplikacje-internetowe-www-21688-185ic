from collections import UserList

from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views
from .views import UserList, UserDetail, PostDetail, PostList


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('<int:pk>/', PostDetail.as_view()),
    path('Post', PostList.as_view()),
]


