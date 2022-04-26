from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.


class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=300, blank=True, null=True)
    completed = models.BooleanField(default=False)
    current_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task-details', kwargs={'pk': self.pk})
