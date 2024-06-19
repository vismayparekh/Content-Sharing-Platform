# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article-list'),
    path('articles/<int:pk>/', views.article_detail, name='article-detail'),
    path('articles/create/', views.article_create, name='article-create'),
    path('articles/<int:pk>/update/', views.article_update, name='article-update'),
    path('articles/<int:pk>/delete/', views.article_delete, name='article-delete'),
    path('api/articles/', views.ArticleListCreateAPIView.as_view(), name='article-list-create-api'),
    path('api/articles/<int:pk>/', views.ArticleRetrieveUpdateDestroyAPIView.as_view(), name='article-retrieve-update-destroy-api'),
]
