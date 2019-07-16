from django.db import models


class Placeholder(models.Model):
    placeholder = models.CharField(max_length=200)


class Officer(models.Model):
    available = models.BooleanField(default=False)
    location_x = models.IntegerField(default=0, null=True)
    location_y = models.IntegerField(default=0, null=True)


class Incident(models.Model):
    assigned_officer = models.ForeignKey(null=True, on_delete=models.DO_NOTHING, to='Officer')
    location_x = models.IntegerField(default=0, null=True)
    location_y = models.IntegerField(default=0, null=True)
    type = models.CharField(max_length=200)
    active = models.BooleanField(default=False)
