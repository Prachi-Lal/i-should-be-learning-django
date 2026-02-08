from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

# Create your views here.
def index(request):
    item_list = Item.objects.all()
    context = {
        "item_list":item_list
    }
    return HttpResponse(render(request,"myapp/index.html", context))

def details(request, id):
    item = Item.objects.get(id=id)
    context = {
        "item":item,
        "id":id,
    }
    return HttpResponse(render(request,"myapp/details.html", context))

def item(request):
    return HttpResponse("yay" )