from django.shortcuts import render
from .models import Algorithm

# Create your views here.

def get_option():

    option = Algorithm.objects.all()
    return option
