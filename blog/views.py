from django.utils import timezone
from django.shortcuts import render, get_object_or_404

from .models import Post


def post_list(request):
    """Main page, display all posts."""
    posts = Post.objects.filter(
        published_at__lte=timezone.now()
    ).order_by('-published_at')

    context = {'posts': posts}
    return render(request, 'blog/post_list.html', context)


def post_detail(request, post_id):
    """Display the full content of a specific post."""
    post = get_object_or_404(Post, pk=post_id)

    context = {'post': post}
    return render(request, 'blog/post_detail.html', context)
