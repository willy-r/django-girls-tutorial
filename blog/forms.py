"""Forms for the blog app."""

from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from .models import Post


class PostForm(ModelForm):
    """Form for create a new post in the blog."""

    class Meta:
        model = Post
        fields = ('title', 'body')
        labels = {
            'title': _('Título'),
            'body': _('Conteúdo'),
        }
