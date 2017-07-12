from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

class AccountModel(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    iban = models.CharField(
        max_length=10,
        unique=True,
        validators=[RegexValidator(r'^\d{1,10}$')]
    )
    date_created = models.DateTimeField('date created', default=timezone.now)
    creator = models.ForeignKey(User)

    def __str__(self):
        return '{0}-{1}'.format(self.firstname, self.lastname)
