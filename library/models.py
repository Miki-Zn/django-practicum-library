from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=100) #first_name VARCHAR(100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()



