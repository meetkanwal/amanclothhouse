from django.db import models


class product(models.Model):
    product_name = models.CharField(max_length=300)
    product_details = models.CharField(max_length=500)
    product_image = models.FileField()
    product_price = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)






