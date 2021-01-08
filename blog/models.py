from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
    """A model for a post in the blog."""
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    published_at = models.DateTimeField(blank=True, null=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        """String representation of a post by title."""
        return self.title

    def publish(self):
        """Publish a post."""
        self.published_at = timezone.now()
        # Update the post on db with the published date.
        self.save()

    def add_view(self):
        """Adds a view on a post."""
        self.views = models.F('views') + 1
        # Save on db and refresh the object to access him.
        self.save()
        self.refresh_from_db()


class Comment(models.Model):
    """A model for a comment in a post."""
    post = models.ForeignKey(Post, related_name='comments',
                             on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        """String representation of a comment by text."""
        if len(self.text) > 50:
            return f'{self.text[:50]}...'
        return self.text
