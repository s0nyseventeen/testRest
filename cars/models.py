from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Car(models.Model):
    vin = models.CharField(max_length=64, verbose_name='Vin', db_index=True, unique=True)
    color = models.CharField(max_length=64, verbose_name='Color')
    brand = models.CharField(max_length=64, verbose_name='Brand')
    CAR_TYPES = (
        (1, 'Sedan'),
        (2, 'Hatchback'),
        (3, 'Universal'),
        (4, 'Coupe')
    )
    car_type = models.IntegerField(choices=CAR_TYPES, verbose_name="Car's type")
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
