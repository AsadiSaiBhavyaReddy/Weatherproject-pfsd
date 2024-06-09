from django.contrib.sites import requests
from django.shortcuts import render


def homefunction(request):
    return render(request,"index.html")

def login(request):
    return render(request,"login.html")



