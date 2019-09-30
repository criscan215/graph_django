from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=20, blank=True, null=True)
    text = models.CharField(max_length=150, blank=True, null=True)

    active = models.BooleanField(default=True)