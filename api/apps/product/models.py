from django.db import models
from api.apps.common.models import BaseModel
import uuid

sizes = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('XL', 'Extra Large'),
    ('XXL', 'Extra Extra Large'),
)

color = (
    ('Red', 'Red'),
    ('Blue', 'Blue'),
    ('Green', 'Green'),
    ('Black', 'Black'),
    ('White', 'White'),
)


class Product(BaseModel):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(default=99.99 , max_digits=10, decimal_places=2)
    discountPercentage = models.DecimalField(default=0 , max_digits=4, decimal_places=2)
    rating = models.DecimalField(default=0  , max_digits=4, decimal_places=2)
    deleted = models.BooleanField(default=False)
    stock = models.IntegerField(default=0)
    brand = models.CharField(max_length=120)
    category = models.CharField(max_length=120)
    thumbnail = models.URLField(max_length=500 , null=True, blank=True)
    images = models.ManyToManyField("Image", blank=True  ) 
    color = models.CharField(max_length=120, choices=color, null= True, blank=True)
    size = models.CharField(max_length=120, choices=sizes ,null= True, blank=True)

    def __str__(self):
        return self.title


class Image(BaseModel):
    image_url = models.URLField(max_length=500 , blank=True , null=True , default="https://via.placeholder.com/150")
