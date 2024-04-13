from django.urls import path

from . import views

urlpatterns = [
    #Se estivermos na home do nosso app, sem digitar nada na barra de pesquisa,
    #chamaremos a view (tela) de nome "index"
    path("<int:id>",views.index,name="index"),
    path("",views.home, name="home"),
    path("create/", views.create, name="create")
    
]
