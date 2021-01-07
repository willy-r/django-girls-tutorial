"""URL patterns for the blog app."""

from django.urls import path

from . import views

urlpatterns = [
    # /
    path('', views.post_list, name='post_list'),

    # /post/1/
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),

    # /post/new/
    path('post/new/', views.post_new, name='post_new'),

    # /post/1/edit/
    path('post/<int:post_id>/edit/', views.post_edit, name='post_edit'),

    # /drafts/
    path('drafts/', views.post_draft_list, name='post_draft_list'),

    # /post/1/publish/
    path('post/<int:post_id>/publish/',
         views.post_publish, name='post_publish'),

    # /post/1/delete/
    path('post/<int:post_id>/delete/', views.post_delete, name='post_delete'),

    # /post/1/comment/
    path('post/<int:post_id>/comment/', views.add_comment, name='add_comment'),

    # /comment/1/delete/
    path('comment/<int:comment_id>/delete/',
         views.comment_delete, name='comment_delete'),
]
