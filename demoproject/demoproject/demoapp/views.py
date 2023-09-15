from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(request):

    return HttpResponse('hello world are you okay')


def demo1(request):
    return render(request,'login.html')

def demo2(request):

    return HttpResponse('python is one of the best language')


def demo3(request):
    return render(request,'Result.html')

def demo4(request):

    return HttpResponse('hello world, the world is buetiful')


