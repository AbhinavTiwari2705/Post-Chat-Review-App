from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.blog_index, name="blog_index"),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('article_overview/', views.article_overview, name='article_overview')
]   


