from django.shortcuts import render


def post_list(request):
    """Main page, display all posts."""
    context = {}
    return render(request, 'blog/post_list.html', context)
