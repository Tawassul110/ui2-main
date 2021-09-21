from django.db import models

# Create your models here.
class Algorithm(models.Model):
    option = models.TextField() 

    def __str__(self):

        return self.option

