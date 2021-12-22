from django.urls import path
from . import views

urlpatterns = [
	path("base", views.base, name="base"),
	path("home", views.home, name="home"),
	path("navbar", views.navbar, name="navbar"),
]
