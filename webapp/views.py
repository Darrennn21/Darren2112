from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature

# Create your views here.
def index(request):
    return render(request, 'index.html')

def cust(request):
    return render(request, 'cust.html')

def custtable(request):
    return render(request, 'custtable.html')

def dealer(request):
    return render(request, 'dealer.html')

def dealertable(request):
    return render(request, 'dealertable.html')

