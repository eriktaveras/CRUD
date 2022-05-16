from pyclbr import Class
from django.db import models

# Create your models here.

class Task(models.Model):
    content = models.TextField(max_length=400)
    date_create = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


