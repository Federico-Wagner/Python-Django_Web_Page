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
	return render(response, "main/base.html", {})

def home(response):
	return render(response, "main/home.html", {})

def about(response):
	return render(response, "main/about.html", {})

def navbar(response):
	#return HttpResponse("<h1>HOME: FW site</h1>")
	return render(response, "main/navbar.html", {})

def sign_in(response):
	return render(response, "main/sign_in.html", {})

"""def sign_up(response):
	return render(response, "main/sign_up.html", {})"""
