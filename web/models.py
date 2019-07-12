from django.db import models


class Placeholder(models.Model):
    placeholder = models.CharField(max_length=200)
