from django.db import models

# Create your models here.
class ToDoList (models.Model):
    name= models.CharField(max_length=200)

    def __str__ (self):
        return self.name
    
class Item(models.Model):
    #ForeingKey é usado pois ToDoList não é uma classe do Django,
    #logo, é estrangeira. O on deleteh Cascade indica que, ao se 
    #apagar a ToDoList, todos os itens serão apagados, pois existem somente na ToDoList
    todolist=models.ForeignKey(ToDoList,on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete=models.BooleanField()

    def __str__(self):
        return self.text   