from django.utils import timezone
from django.shortcuts import render

from .models import Post


def post_list(request):
    """Main page, display all posts."""
    posts = Post.objects.filter(
        published_at__lte=timezone.now()
    ).order_by('-published_at')

    context = {'posts': posts}
    return render(request, 'blog/post_list.html', context)
