from django.urls import path
from . import views

urlpatterns = [
	path("", views.home, name="home"),
	path("base", views.base, name="base"),
	path("home", views.home, name="home"),
	path("about", views.about, name="about"),
	path("navbar", views.navbar, name="navbar"),
	#path("log_in", views.log_in, name="sign_in"),
	#path("sign_up", views.sign_up, name="singn_up"),
]
