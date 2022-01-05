from django.shortcuts import render

from product.models import Product

def home(request):
    prod=Product.objects.all().filter(is_available=True)

    print(prod)

    context = {
        'prods':prod
    }

    return render(request,'home.html',context)