from django.db import models

# Create your models here.
class Homework(models.Model):
    title = models.CharField(max_length=200)
    due_date = models.CharField(max_length=50)
    def __str__(self):
        return  self.title
