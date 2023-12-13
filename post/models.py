from django.db import models
import uuid
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError


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


def validate_file_size(value):
    limit = 1 * 1024 * 1024  # 5 MB limit
    if value.size > limit:
        raise ValidationError('File size cannot exceed 1 MB.')


class Tag(models.Model):
    name = models.CharField(max_length=50)
    image = models.FileField(
        upload_to='icons/', null=True, blank=True,
        validators=[FileExtensionValidator(['jpg', 'png', 'svg']),
                    validate_file_size])
    slug = models.SlugField(max_length=50, unique=True)
    order = models.IntegerField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']
        unique_together = ['name']
