from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100) #first_name VARCHAR(100)
    surname = models.CharField(max_length=100)
    birth_date = models.DateField()
    profile = models.URLField(max_length=255, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    rating = models.FloatField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ],
        default=0.0
    )
    deleted_at = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.name




