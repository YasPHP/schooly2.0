from django.shortcuts import render
from django.http import HttpResponse

#create your views here

def homepage(request):
    return render(request = request,
           template_name= 'main/home.html',
           context = {"Notes": Notepad.objects.all})
