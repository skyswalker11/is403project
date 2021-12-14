from django.shortcuts import render
from django.http import HttpResponse

# View for the landing page
def indexPageView(request) : 
        return render(request, 'inventorypages/index.html')

# View for displaying the inventory page 
def inventoryPageView(request) : 
    return render(request, 'inventorypages/inventory.html')

# View for editing or deleting inventory page 
def editPageView(request) : 
    return render(request, 'inventorypages/edit.html')

# View for creating new inventory page
def createPageView(request) : 
    return render(request, 'inventorypages/create.html')

 