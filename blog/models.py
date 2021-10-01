from django.db import models
from django.conf import settings

# Create your models here.


class Post(models.Model):
    class Meta:
        ordering = ["-publish_date"]

    title = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=999, blank=True)
    publish_date = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)


class Comments(models.Model):
    class Meta:
        ordering = ["-created_at"]

    text = models.CharField(max_length=255, unique=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)