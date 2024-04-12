from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.

def index(response,id):
    list = ToDoList.objects.get(id=id)
    items = list.item_set.get(id=1)
    return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" %(list.name,items.text))

