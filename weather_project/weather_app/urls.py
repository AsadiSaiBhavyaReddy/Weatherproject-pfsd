from django.urls import path
from . import views

urlpatterns = [
    path("weather", views.weather, name="weather"),

    path("adminlogout", views.logout, name="login"),
    path("checkadminlogin", views.checkadminlogin, name="checkadminlogin"),
    ]