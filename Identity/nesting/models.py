from django.db import models


from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


from Identity import settings
import datetime



# Create your models here.

class Identity_unique(models.Model):

    NIS = models.CharField(max_length = 200, primary_key = True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    Timestamp = models.DateTimeField(auto_now = True)

    first_Name = models.CharField(max_length = 80, null = True )

    last_Name = models.CharField(max_length = 80, null = True )

    location = models.CharField(max_length = 100, blank = True)

    date_of_birth = models.DateField(auto_now = False, auto_now_add = False, blank = True, null = True)

    contact = models.CharField(max_length = 15, null = True)







class Symptom_relation(models.Model):

    symptom_name = models.CharField(max_length = 80, default = '')

    symptom_description = models.TextField(max_length = 1000, default = '')

    time_record = models.DateTimeField(auto_now = True)

    Unique_Identity = models.ManyToManyField(Identity_unique, blank = False, related_name = 'Symptom')




class Treatment(models.Model):

    pass
