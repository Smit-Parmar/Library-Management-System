
from django.urls import path,include
from rest_framework import routers
from . import views


urlpatterns = [
    path("signup/",views.AdminSignup.as_view(),name="signup"),
]
