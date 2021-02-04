from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.blog_index, name="blog_index"),
    path('post/<uuid:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<uuid:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    # path('comment/<uuid:pk>/approve/', views.comment_approve, name='comment_approve'),
    # path('comment/<uuid:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('filtered_posts/', views.SearchResultsListView.as_view(), name='filtered_posts')
]   


