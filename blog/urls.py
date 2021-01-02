"""URL patterns for the blog app."""

from django.urls import path

from . import views

urlpatterns = [
    # /
    path('', views.post_list, name='post_list'),

    # /post/1
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),

    # /post/new/
    path('post/new/', views.post_new, name='post_new'),

    # /post/1/edit
    path('post/<int:post_id>/edit/', views.post_edit, name='post_edit'),
]
