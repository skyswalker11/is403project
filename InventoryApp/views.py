from django.shortcuts import render
from django.http import HttpResponse

# View for the landing page
def indexPageView(request) : 
    return HttpResponse("This is the landing page") 

# View for displaying the inventory page 
def inventoryPageView(request) : 
    return HttpResponse("This is the inventory page")

# View for editing or deleting inventory page 
def editPageView(request, item_id) : 
    return HttpResponse("This is the editing inventory page for item id: " + str(item_id))

# View for creating new inventory page
def createPageView(request) : 
    return HttpResponse("This is the create new inventory page ")
