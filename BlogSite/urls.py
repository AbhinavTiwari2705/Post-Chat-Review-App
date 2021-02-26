from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.blog_index, name="blog_index"),
    path('post/<uuid:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<uuid:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    # path('post/<uuid:pk>/like/', views.PostLike, name='post_like'),
    path('comment/approve/<uuid:pk>/', views.comment_approve, name='comment_approve'),
    path('comment/remove/<uuid:pk>/', views.comment_remove, name='comment_remove'),
    path('filtered_posts/', views.SearchResultsListView.as_view(), name='filtered_posts'),
]   


