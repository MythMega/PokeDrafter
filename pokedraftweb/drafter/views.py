from django.shortcuts import render
from django.http import HttpResponse

def index(request) -> None:
    return HttpResponse("Index de l'app");
