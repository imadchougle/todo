# models.py
from django.db import models
from django.utils import timezone

class Todo(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
