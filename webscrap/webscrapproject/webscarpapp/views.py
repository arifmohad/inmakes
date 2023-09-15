import requests 
from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Links

# Create your views here.

def home(request):
    if request.method=='POST':
        newlink=request.POST.get('page','')
        urls=requests.get(newlink)
        buetysoup=BeautifulSoup(urls.text,'html.parser')

        for link in buetysoup.find_all('a'):
            li_address=link.get('href')
            li_name=link.string
            Links.objects.create(address=li_address,stringname=li_name)
        return HttpResponseRedirect('/')
    else:

        datas=Links.objects.all()
    return render(request,'home.html',{'datas':datas})

