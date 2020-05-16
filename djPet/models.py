from django.db import models


class pricer(models.Model):
    document = models.FileField(upload_to='media/')
    shopID = models.CharField(max_length=1)
    name = models.CharField(max_length=1)
    amount = models.CharField(max_length=1)
    price = models.CharField(max_length=1)
    partNumber = models.CharField(max_length=1)
    MRP = models.CharField(max_length=1)
    # user_ID
    # operation_time


