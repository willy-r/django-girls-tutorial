from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
    """A model for a post in the blog."""
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    create_at = models.DateTimeField(default=timezone.now)
    published_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        """String representation of a post by title."""
        return self.title

    def publish(self):
        """Publish a post."""
        self.published_at = timezone.now()
        # Update the post on db with the published date.
        self.save()
