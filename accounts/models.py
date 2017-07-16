from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator, RegexValidator
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
    iban = models.CharField(
        max_length=10,
        unique=True,
        validators=[RegexValidator(r'^\d{10}$')],
        verbose_name='IBAN',
        error_messages={
            'invalid':'IBAN must consist of numbers only and must be 10 characters in length.',
            'unique': 'An account with this IBAN already exists.'
        }
    )
    date_created = models.DateTimeField('date created', default=timezone.now)
    creator = models.ForeignKey(User)

    def __str__(self):
        return '{0}-{1}'.format(self.firstname, self.lastname)
