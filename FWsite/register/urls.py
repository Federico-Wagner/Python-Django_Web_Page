from django.urls import path
from . import views

urlpatterns = [
	path("sign_up", views.sign_up, name="singn_up"),
	path("pass_reco", views.f_pass, name="password recovery"),
]
