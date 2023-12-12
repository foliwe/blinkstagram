from django.db import models
import uuid


class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField(max_length=500)
    artist = models.CharField(max_length=200, null=True)
    url = models.URLField(max_length=500, null=True)
    tags = models.ManyToManyField('Tag', blank=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(max_length=100, default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    order = models.IntegerField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']
        unique_together = ['name']
