from django.db import models

# Create your models here.

class CompanyName(models.Model):
    name = models.TextField()
    year = models.CharField(max_length = 4)

    def __str__(self):
        return self.name

class Header(models.Model):
    title = models.TextField()
    isMain = models.BooleanField()
    textOne = models.TextField()
    textTwo = models.TextField()
    image = models.ImageField(upload_to = 'headerImage')

    def __str__(self):
        if self.isMain:
            return f"MAIN HEADER {self.title}"
        else:
            return f"SUB HEADER {self.title}"
