from django.http import Http404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .models import Post
from .forms import PostForm


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


@login_required
def post_new(request):
    """Creates a new post."""
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish()
            return redirect('post_detail', post_id=post.id)

    context = {'form': form}
    return render(request, 'blog/post_new.html', context)


@login_required
def post_edit(request, post_id):
    """Edits a post."""
    post = get_object_or_404(Post, pk=post_id)

    if post.author != request.user:
        raise Http404

    if request.method != 'POST':
        form = PostForm(instance=post)
    else:
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish()
            return redirect('post_detail', post_id=post.id)

    context = {
        'post': post,
        'form': form
    }
    return render(request, 'blog/post_edit.html', context)
