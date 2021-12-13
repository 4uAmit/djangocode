from django.db import models

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=30)
    img=models.ImageField(upload_to='prdct')
    slug=models.SlugField(unique=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='pixx')
    slug=models.SlugField(unique=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    url=models.URLField()
    description = models.TextField()
    
    def __str__(self):
        return self.name