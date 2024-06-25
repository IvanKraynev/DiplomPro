from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Brand(models.Model):
    image = models.ImageField(upload_to='brands/')
    
    def __str__(self):
        return str(self.id)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='example@example.com')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username

