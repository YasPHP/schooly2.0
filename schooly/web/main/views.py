from django.shortcuts import render
from django.http import HttpResponse

#create your views here

def homepage(request):
    return render(request, 'main/home.html', context={})