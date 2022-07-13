from turtle import title
from django.db import models

class details(models.Model):
    title  = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title