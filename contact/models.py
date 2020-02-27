from django.db import models
from django.utils import timezone
import datetime

class contactmsg(models.Model):
    firstname=models.CharField(max_length=300)
    lastname=models.CharField(max_length=300)
    email=models.EmailField()
    subject=models.CharField(max_length=300)
    message=models.CharField(max_length=3000,blank=False,null=False)
    subtime=models.DateTimeField(auto_now=False)

    class Meta:
        ordering=['subtime']

    def __str__(self):
        return self.firstname + self.lastname