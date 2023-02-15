from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostView.as_view(), name = 'posts_list'),
    path('create_post/', views.create_post),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('review/<int:pk>/', views.AddComment.as_view(), name='add_comments'),
    path('about/', views.AboutPage, name='view'),
    path('rules/', views.RulesPage, name='rules'),
    path('post_wait/', views.post_wait, name='post_wait'),
    path('changelog/', views.changelog, name = 'changelog')
]