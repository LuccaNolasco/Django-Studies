from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.

def index(response,id):
    list = ToDoList.objects.get(id=id)

    if response.method == "POST":
       print(response.POST)
       if response.POST.get("save"): #save é o value que colocamos no botão de salvar. Aqui é para checar a origem da response do formulario
        #response.POST é um dicionário com todas as mudanças feitas no formulário. Se algo for modificado, seu value aparece. Logo, podemos saber o que mudou
        #ao checar quais valores aparareceram

          #Esse loop é para checar cada checkbox. Cada item. Verificará pela id se foi marcado
          for item in list.item_set.all():
              if response.POST.get("c"+str(item.id)) == "clicked":
                item.complete = True
              else:
                item.complete = False
              item.save()

       elif response.POST.get("newItem"):
          txt = response.POST.get("new")

          if len(txt)>2: #Aqui irá validar o input e adicionar na lista
             list.item_set.create(text=txt, complete = False)
          else:
             print("Invalid input")   

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

 