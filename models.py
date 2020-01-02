from django.db import models

# Create your models here.

class Webdata(models.Model):
    name = models.CharField(max_length=45)
    price = models.FloatField(max_length=45)
    rating = models.FloatField()

    def __str__(self):
        return self.name