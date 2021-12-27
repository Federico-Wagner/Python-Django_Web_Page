from django.db import models
import datetime

# Create your models here.
class TodoList(models.Model):
	name = models.CharField(max_length=200) #name of the list
	creation_date = models.DateTimeField('date created', default=datetime.datetime.now())

	def __str__(self): #instead of printing the wraped object...
		return self.name

class Item(models.Model): #atributes of every item
	todolist = models.ForeignKey(TodoList, on_delete= models.CASCADE)
	text = models.CharField(max_length=300)
	creation_date = models.DateTimeField('date created', default=datetime.datetime.now())
	priority = models.IntegerField(default=0)
	complete = models.BooleanField()

	def __str__(self):
		return self.text

#models.ForeignKey  <- difines a relationship (each item is related to a single Todolist
