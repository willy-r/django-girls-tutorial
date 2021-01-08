from django.http import Http404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .models import Post, Comment
from .forms import PostForm, CommentForm


def post_list(request):
    """Main page, display all posts."""
    posts = Post.objects.filter(
        published_at__lte=timezone.now()
    ).order_by('-published_at')

    context = {'posts': posts}
    return render(request, 'blog/post_list.html', context)


def post_draft_list(request):
    """Display all post that are drafts."""
    posts = Post.objects.filter(
        published_at__isnull=True
    ).order_by('created_at')

    context = {'posts': posts}
    return render(request, 'blog/post_draft_list.html', context)


def post_detail(request, post_id):
    """Display the full content of a specific post."""
    post = get_object_or_404(Post, pk=post_id)

    if post.published_at:
        # Count one view on that post.
        post.add_view()

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
            post.save()
            return redirect('post_detail', post_id=post.id)

    context = {'form': form}
    return render(request, 'blog/post_new.html', context)


@login_required
def post_edit(request, post_id):
    """Edits a post."""
    post = get_object_or_404(Post, pk=post_id)

    if request.method != 'POST':
        form = PostForm(instance=post)
    else:
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', post_id=post.id)

    context = {
        'post': post,
        'form': form
    }
    return render(request, 'blog/post_edit.html', context)


@login_required
def post_publish(request, post_id):
    """Publishs a post."""
    post = get_object_or_404(Post, pk=post_id)
    post.publish()

    return redirect('post_detail', post_id=post.id)


@login_required
def post_delete(request, post_id):
    """Deletes a post."""
    post = get_object_or_404(Post, pk=post_id)

    if not post.published_at:
        post.delete()
        return redirect('post_draft_list')
    else:
        post.delete()
        return redirect('post_list')


def add_comment(request, post_id):
    """Adds a comment to a post."""
    post = get_object_or_404(Post, pk=post_id)

    if not post.published_at:
        raise Http404

    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', post_id=post.id)

    context = {
        'post': post,
        'form': form
    }
    return render(request, 'blog/add_comment.html', context)


@login_required
def comment_delete(request, comment_id):
    """Deletes a comment from a post."""
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return redirect('post_detail', post_id=comment.post.id)
