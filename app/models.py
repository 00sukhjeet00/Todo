from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    choice = [
        ('C', 'Complete'),
        ('P', 'pending')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=2, choices=choice, default=choice[1])
    date = models.DateTimeField(auto_now_add=True)
