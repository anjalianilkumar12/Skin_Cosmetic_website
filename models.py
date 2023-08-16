from django.db import models

# Create your models here.
class Categories(models.Model):
    cat_id=models.IntegerField(primary_key=True)
    catname=models.CharField(max_length=100)
    def __str__(self):
        return self.catname
class Brands(models.Model):
    brandname=models.CharField(max_length=100)
   
    def __str__(self):
        return self.brandname
class Product(models.Model):
    product_img=models.ImageField(upload_to='product_img')
    product_name=models.CharField(max_length=100)
    content=models.CharField(max_length=100)
    brand=models.ForeignKey(Brands,on_delete=models.CASCADE)
    price=models.IntegerField()
    expirydate=models.DateField()
    Category=models.ForeignKey(Categories,on_delete=models.CASCADE)
    def __str__(self):
        return self.product_name
