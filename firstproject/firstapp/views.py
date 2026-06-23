from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

# Function based view
def hello_world(request):
    return HttpResponse("Hello World")

# class based view, we use inheritance to create a class based view
class HelloSomalia(View):
    def get(self, request):
        return HttpResponse("Hello Somalia")