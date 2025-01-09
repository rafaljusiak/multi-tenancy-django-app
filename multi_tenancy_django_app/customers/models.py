from django.db import models


class Organization(models.Model):
    customer = models.ForeignKey("customers.Customer", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


class Customer(models.Model):
    name = models.CharField(max_length=255)
