from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import RegisterForm

# Create your views here.
def sign_up(response):
	form = RegisterForm(response.POST)
	if response.method == "POST":
		if form.is_valid():
			form.save()
			return redirect("/home")
	else:
		form = RegisterForm()
	return render(response, "register/sign_up.html", {"form":form})

def f_pass(response):
	return render(response, "register/password_recov.html", {})
