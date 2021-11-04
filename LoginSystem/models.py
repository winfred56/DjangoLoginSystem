from django.db import models


class UserDetails(models.Model):
    Male = 'Male'
    Female = 'Female'
    sex_choices = [(Male,'Male'), (Female,'Female')]
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    sex = models.CharField(max_length=8, choices=sex_choices, default=Male)
