from django.db import models
from django.urls import reverse


class Text(models.Model):
    data = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.data

    def get_absolute_url(self):
        return reverse("text:list")
