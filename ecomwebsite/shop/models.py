from django.db import models

class Products(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    images = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title