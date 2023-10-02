from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(r):
    return HttpResponse('<h1>Welcome to django live server, thanks for visitgit</h1>')

def show(r):
    return HttpResponse('Hi rohit how r you')