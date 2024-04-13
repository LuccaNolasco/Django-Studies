from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.

def index(response,id):
    list = ToDoList.objects.get(id=id)
    #O dicionário serve para passar as variáveis necessárias
    return render(response,"main/list.html",{"list":list})

def home( response):
    return render(response,"main/home.html",{})

def create(response):
    if response.method == "POST":
      form = CreateNewList(response.POST) 
      
      #Vai irá pegar esse Post e pegar todos os dados do formulário
      # e teremos todos os dados como formulário.
      #cleaned data irá desencriptá-lo. Depois isso, usamos o nome da field. 
      
      
      #A lógica aqui é que da primeira vez, o usuário entrará no else e será renderizada
      #uma pag vazia. Depois de preencher os dados e apertar o botão, entra na mesma url
      #e entra no if, criando a nova ToDoList  
      if form.is_valid():
         n = form.cleaned_data["name"]
         t = ToDoList(name=n)
         t.save()
         #Redirecionando para a url que recebe inteiros e os usa como id
         return HttpResponseRedirect("/%i" %t.id)
    else:   
      form = CreateNewList()
    return render(response,"main/create.html",{ "form":form})
    #Post é para informaçoes secretas e mudanças no BD. Get é para o resto
    #Podemos checar ambos os casos com essa estrutura de if else

 