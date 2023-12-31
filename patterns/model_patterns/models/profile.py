import datetime

from django.conf import settings
from django.db import models



# Create your models here.


class BaseProfile(models.Model):
    USER_TYPES = (
        (0, 'Ordinary'),
        (1, 'SuperHero'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True,on_delete=models.CASCADE,)
    user_type = models.IntegerField(max_length=1, null=True, choices=USER_TYPES)
    bio = models.CharField(max_length=200, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)

    @property
    def age(self):
        today = datetime.date.today()
        return f"your birthdate is {self.birthdate} and today is {today}"
    def __str__(self):
        return "{}: {:.20}". format(self.user, self.bio or "")

    class Meta:
        abstract = True

class SuperHeroProfile(models.Model):
    origin = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        abstract = True

class OrdinaryProfile(models.Model):
    address = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        abstract = True

class Profile(SuperHeroProfile, OrdinaryProfile, BaseProfile):
    pass
