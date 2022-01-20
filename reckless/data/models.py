from django.db import models


class Source(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.TextField()
    file = models.FileField(upload_to='data/')
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
