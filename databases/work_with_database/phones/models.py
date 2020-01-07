from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=256)
    price = models.CharField(max_length=10)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.CharField(max_length=150)

