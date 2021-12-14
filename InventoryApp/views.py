from django.shortcuts import render
from django.http import HttpResponse
from .models import Inventory
import psycopg2

# View for the landing page
def indexPageView(request) : 
        return render(request, 'inventorypages/index.html')

# View for displaying the inventory page 
def inventoryPageView(request) : 
    products = Inventory.objects.all()

    context = {
        "products": products
    }

    return render(request, 'inventorypages/inventory.html', context)

# View for displaying product details
def productDetailsPageView(request, productid) :
    product = Inventory.objects.get(productid = productid)

    context = {
        "product": product
    }

    return render(request, 'inventorypages/productdetails.html', context)

# View for editing or deleting inventory page 
def editPageView(request) : 
    return render(request, 'inventorypages/edit.html')

# View for creating new inventory page
def createPageView(request) : 
    if request.method == 'POST' :
        return productDetailsPageView(request)

    else :
        return render(request, 'inventorypages/create.html')

 