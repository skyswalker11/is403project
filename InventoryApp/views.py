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
def productDetailsPageView(request, product_id) :
    product = Inventory.objects.get(product_id = product_id)

    context = {
        "product": product
    }

    return render(request, 'inventorypages/productdetails.html', context)

# View for editing or deleting inventory page 
def editPageView(request, product_id) : 
    if request.method == 'POST' :
        product_id = request.POST['product_id']
        product = Inventory.objects.get(product_id=product_id)
        
        context = {
            "product": product
        }

        return render(request, 'inventorypages/inventory.html', context)

    else :
        return render(request, 'inventorypages/edit.html')

# View for creating new inventory page
def createPageView(request) : 
    if request.method == 'POST' :
        codigo = request.POST['codigo']
        marca = request.POST['marca']
        descripcion = request.POST['descripcion']
        ubicacion = request.POST['ubicacion']
        unidad = request.POST['unidad']
        stock = request.POST['stock']
        dolares = request.POST['dolares']
        soles = request.POST['soles']
        valor_del_stock = request.POST['valor_del_stock']
        tipo_de_cambio = request.POST['tipo_de_cambio']

        instance = Inventory(codigo=codigo, marca=marca, descripcion=descripcion, ubicacion=ubicacion, unidad=unidad, \
            stock=stock, dolares=dolares, soles=soles, valor_del_stock=valor_del_stock, tipo_de_cambio=tipo_de_cambio)

        instance.save()

    return inventoryPageView(request)