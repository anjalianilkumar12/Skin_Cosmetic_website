from django.shortcuts import render
from . models import Product,Categories,Brands
# Create your views here.
def homeview(request):
    return render(request,'home.html')
#def categoryview(request):
    #product=Productsample.objects.all()
    #return render(request,'categories.html',{'product':product})

def categoryview(request):
     Category=Categories.objects.all()
     return  render(request,'categories.html',{'cat':Category})

def productview(request,id):
     cat=Categories.objects.get(cat_id=id)
     pro=Product.objects.filter(Category=cat)
     return  render(request,'product.html',{'pro':pro})
def contactview(request):
     return render(request,'contact.html')
def aboutview(request):
     return render(request,'about.html')
def Brandview(request):
     brand=Brands.objects.all()
     return render(request,'brands.html',{'brand':brand})
def branddetail(request,id):
     brands=Brands.objects.get(id=id)
     pro=Product.objects.filter(brand=brands)
     return render(request,'branddetials.html',{'pro':pro})

