from django.db import models
import uuid


class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField(max_length=500)
    artist = models.CharField(max_length=200, null=True)
    url = models.URLField(max_length=500, null=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(max_length=100, default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
