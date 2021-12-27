from django.urls import path
from . import views

urlpatterns = [
	path("sign_up", views.sign_up, name="singn_up"),
	path("log_in", views.log_in, name="log_in"),
	path("pass_reco", views.f_pass, name="password recovery"),
]
