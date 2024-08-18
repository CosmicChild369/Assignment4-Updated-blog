from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
    path('article/create/', views.article_create, name='article_create'),
    path('article/<int:pk>/edit/', views.article_edit, name='article_edit'),
    path('article/<int:pk>/delete/', views.article_delete, name='article_delete'),
    path('article/<int:pk>/comment/', views.add_comment, name='add_comment'),
    path('article/<int:article_id>/like/', views.like_article, name='like_article'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', views.custom_logout, name='logout'),
]

