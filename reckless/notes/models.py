from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class Note(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    tags = TaggableManager()
