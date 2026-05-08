from django.db import models

# Create your models here.

class Comments(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Project(models.Model):
    image = models.ImageField(upload_to='static/images/')
    name = models.CharField(max_length=100)
    description = models.TextField()
    rooms = models.IntegerField()
    floor = models.IntegerField()
    location = models.CharField(max_length=100)
    available_numbers = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

class Lead(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class AdminPanel(models.Model):
    name = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
