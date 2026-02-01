from django.db import models
from django.core.validators import (MinValueValidator,
                                    MaxValueValidator,
                                    RegexValidator,
                                    EmailValidator,
                                    MinLengthValidator,
                                    MaxLengthValidator,
                                    )
from django.core.exceptions import ValidationError



# Create your models here.
class Player_Serializer(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField(validators=[MinValueValidator(18)])
    country=models.CharField(max_length=10)
    jersy_number=models.IntegerField(max_length=3)

    def __str__(self):
        return (self.name,self.country)
