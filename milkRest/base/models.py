from django.db import models

# Create your models here.

class CompanyName(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

class Header(models.Model):
    title = models.TextField()
    isMain = models.BooleanField()
    textOne = models.TextField()
    textTwo = models.TextField()
    image = models.ImageField(upload_to = 'headerImage')
