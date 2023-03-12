from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Band(models.Model):
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
        RAP = 'RP'
        PHONK = 'PH'

    name = models.CharField(max_length=100)
    genre = models.fields.CharField(choices = Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
    validators=[MinValueValidator(1900), MaxValueValidator(2023)]
    )
    active= models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)
    def __str__(self):
        return f'{self.name}'


class Listing(models.Model):
    class type(models.TextChoices):
        Records = 'RE'
        Clothing = 'CL'
        Posters = 'PO'
        Miscellaneous = 'MI'

    title = models.CharField(max_length=100)
    description = models.fields.CharField(max_length=1000)
    sold = models.fields.BooleanField(default=False)
    year_released = models.fields.IntegerField(    
        null=True, 
        blank=True, 
        validators=[MinValueValidator(1900), MaxValueValidator(2023)
        ],
    )
    type = models.fields.CharField(choices = type.choices, max_length=5)
    band = models.ForeignKey(Band, null = True,  on_delete=models.SET_NULL)
    


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.fields.EmailField()
    message = models.fields.CharField(max_length=1000)

class Abt(models.Model):
    description = models.fields.CharField(max_length=1000)
