from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
	path("", views.home, name="home"),
	path("base", views.base, name="base"),
	path("home", views.home, name="home"),
	path("about", views.about, name="about"),
	path("navbar", views.navbar, name="navbar"),
	path("list/<int:list_number>/", views.list, name="List"),#automaticlly pases list_number variable to views.list
	path("list/<int:list_number>/detail", views.list_detail, name="List_detail"),
]
