from django.db import models
from django.urls import reverse
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200)
    detail = models.CharField(max_length=400)
    Image = models.ImageField()
    price = models.PositiveIntegerField(blank=False)


    def __str__(self):
       return self.name

    def get_absolute_url(self):
        return reverse('detail', args=[(self.id)])