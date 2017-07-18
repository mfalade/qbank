from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator, RegexValidator
from internationalflavor.iban import IBANField
from django.contrib.auth.models import User


class AccountModel(models.Model):
    firstname = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2, message='2 or more characters required.')]
    )
    lastname = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2, message='2 or more characters required.')], 
    )
    iban = IBANField(
        verbose_name='IBAN',
        unique=True,
    )
    date_created = models.DateTimeField('date created', default=timezone.now)
    creator = models.ForeignKey(User)

    def __str__(self):
        return '{0}-{1}'.format(self.firstname, self.lastname)
