from django.db import models

# Create your models here.

class Book (models.Model):
    name = models.CharField(max_length=200)
    pageNumber = models.IntegerField()
    genre = models.CharField(max_length=200)
    publishDate = models.DateField()

    def __str__(self):
        return self.genre
