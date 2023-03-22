from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return HttpResponse("Hello this is about page")
