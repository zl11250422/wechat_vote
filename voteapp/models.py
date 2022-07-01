from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser
import django.utils.timezone as timezone
import os

# Create your models here
class DEMO_VOTE(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    title = models.CharField(max_length=32)

class DEMO_VOTE_DETAIL(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    vote_id = models.IntegerField(null=False)
    content = models.CharField(max_length=32)
    sort = models.IntegerField(null=False, default = 0)
    #CREATE_TIME = models.DateTimeField('日期',default=timezone.now)

class DEMO_VOTE_RESULT(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    vote_id = models.IntegerField(null=False)
    detail_id = models.IntegerField(null=False)
    open_id = models.CharField(max_length=100)
    #CREATE_TIME = models.DateTimeField('日期',default=timezone.now)
