from django.db import models
from weekly_dashboard import settings

# Create your models here.
class Registration(models.Model):
    event_type = models.CharField(max_length=80)
    date_time = models.DateField()
    count = models.IntegerField()

class VDP_Sli_KR(models.Model):
    date_time = models.DateField()
    name = models.CharField(max_length=50)
    partner_system_name = models.CharField(max_length=50)
    linking_status = models.CharField(max_length=50)
    count = models.IntegerField()

class Reward_Sli(models.Model):
    reward = models.CharField(max_length=80)
    awarded_on = models.DateField()
    count = models.IntegerField()


class Goals_Sli(models.Model):
    effective_from = models.DateField()
    effective_to = models.DateField()
    goal_status = models.CharField(max_length = 100)
    count = models.IntegerField()

class Registration_KR(models.Model):
    event_type = models.CharField(max_length=80)
    date_time = models.DateField()
    count = models.IntegerField()

class Reward_KR(models.Model):
    reward = models.CharField(max_length=80)
    awarded_on = models.DateField()
    count = models.IntegerField()


class Goals_KR(models.Model):
    effective_from = models.DateField()
    effective_to = models.DateField()
    goal_status = models.CharField(max_length = 100)
    count = models.IntegerField()

