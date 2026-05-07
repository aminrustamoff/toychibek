from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.CharField(max_length=100)

    STATUS = (
        ('new', 'New'),
        ('sold', 'Sold'),
    )

    status = models.CharField(max_length=20, choices=STATUS)

    image = models.ImageField(upload_to='static/images/')

class Lead(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    message = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

