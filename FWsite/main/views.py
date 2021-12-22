from django.shortcuts import render
from django.http import HttpResponse
from .models import TodoList, Item
# Create your views here.
"""
def index(response):
	#ls = TodoList.objects.get(name=name) #dynamic url from database object HERE
	return HttpResponse("<h1>FW site: empty URL</h1>") #("<h1>FW site %s</h1>" % ls.name)
"""

def base(response):
	#ls = TodoList.objects.get(name=name) #dynamic url from database object HERE
	return render(response, "main/base.html", {})

def home(response):
	#return HttpResponse("<h1>HOME: FW site</h1>")
	arr_1 = [1, 2, 3]
	arr_2 = [4, 5, 6]
	return render(response, "main/home.html", {"arr_1":arr_1, "arr_2":arr_2})

def navbar(response):
	#return HttpResponse("<h1>HOME: FW site</h1>")
	return render(response, "main/navbar.html", {})