from django.urls import path
from . import views

app_name = 'register'
urlpatterns = [
	path("sign_up", views.sign_up, name="singn_up"),
	path("pass_reco", views.f_pass, name="password recovery"),
]
