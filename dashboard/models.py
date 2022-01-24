from django.db import models

# Create your models here.
class Book(models.Model):
    name=models.CharField(max_length=100)
    picture = models.ImageField()
    author=models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        result = self.name + " by " + self.author
        return result