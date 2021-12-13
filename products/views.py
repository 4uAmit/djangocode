from django.shortcuts import render
from products.models import Product,Category
# Create your views here.

def productcategory(request):
    categories=Category.objects.all()
    context={"categories":categories} 
    return render(request,'products/productcat.html',context)
    

def products(request,slug):
    category=Category.objects.filter(slug=slug).first()
    productss = Product.objects.filter(category=category)
    context={'productss':productss}
    return render(request, 'products/products.html', context)