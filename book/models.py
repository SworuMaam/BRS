# book/models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.FloatField(default=0.0)  # Or other criteria for popularity

    def __str__(self):
        return self.title
