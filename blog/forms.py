"""Forms for the blog app."""

from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from .models import Post, Comment


class PostForm(ModelForm):
    """Form for create a new post in the blog."""

    class Meta:
        model = Post
        fields = ('title', 'body')
        labels = {
            'title': _('Título'),
            'body': _('Conteúdo'),
        }


class CommentForm(ModelForm):
    """Form for add a new comment on a post."""

    class Meta:
        model = Comment
        fields = ('author', 'text')
        labels = {
            'author': _('Seu nome'),
            'text': _('Comentário'),
        }
