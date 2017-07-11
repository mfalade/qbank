from django.db import models
from django.core.validators import RegexValidator

class Account(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    iban = models.CharField(
        max_length=10,
        unique=True,
        validators=[RegexValidator(r'^\d{1,10}$')]
    )
