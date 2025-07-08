from django.db import models


class Personal(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField('personal/images/')
    url = models.URLField(blank=True)
