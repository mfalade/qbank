from django.db import models
from django.core.validators import RegexValidator

class AccountModel(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    iban = models.CharField(
        max_length=10,
        unique=True,
        validators=[RegexValidator(r'^\d{1,10}$')]
    )

    def __str__(self):
        return '{0}-{1}'.format(self.firstname, self.lastname)
