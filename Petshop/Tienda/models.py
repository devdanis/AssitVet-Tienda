from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.CharField(max_length=200, default='https://media.istockphoto.com/id/177370583/photo/traffic-cones-and-hardhat-3d-isolated.jpg?s=612x612&w=0&k=20&c=RDDLHMULBB-G_FMMijdavKuVkpYnLIRCbAA1a41r-7o=')

    def __str__(self):
        return self.name