from django.urls import path
from . import views

urlpatterns = [
	path("base", views.base, name="base"),
	path("home", views.home, name="home"),
	path("about", views.about, name="about"),
	path("navbar", views.navbar, name="navbar"),
	path("sign_in", views.sign_in, name="sign_in"),
	#path("sign_up", views.sign_up, name="singn_up"),
]
