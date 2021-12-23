from django.shortcuts import render

# Create your views here.
def sign_up(response):
	return render(response, "register/sign_up.html", {})

def f_pass(response):
	return render(response, "register/password_recov.html", {})