from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import TodoList, Item
# Create your views here.
"""
def index(response):
	#ls = TodoList.objects.get(name=name) #dynamic url from database object HERE
	return HttpResponse("<h1>FW site: empty URL</h1>") #("<h1>FW site %s</h1>" % ls.name)
"""

def base(response):
	return render(response, "main/base.html", {})

def home(response):
	list_array = TodoList.objects.all() #Data Base querry
	args = {"list_array":list_array, "user":response.user}
	return render(response, "main/home.html", args)

def about(response):
	return render(response, "main/about.html", {})

def navbar(response):
	#return HttpResponse("<h1>HOME: FW site</h1>")
	return render(response, "main/navbar.html", {})

def list(response,list_number):# I recive number variable, from the url
	obj = get_object_or_404(TodoList,id = list_number)  #Django built in shortcut
	args = {"list_number": list_number,
			"list_obj":obj}
	return render(response, "main/list_view.html", args)


def list_detail(response,list_number):# I recive number variable, from the url
	list_obj = TodoList.objects.filter(id=list_number) #returns a list only one match
	tasks = Item.objects.filter(todolist=list_obj[0])
	args = {"list_number": list_number,
			"list_obj":list_obj[0],
			"tasks":tasks}
	return render(response, "main/list_view_detail.html", args)
