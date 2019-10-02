from django.shortcuts import render

from mainConfig.models import *
from .models import *

# Create your views here.

def index(request):
    allFront = Front.objects.filter(status=True)[:1].get()
    headerImage=headBackImage.objects.filter(status=True)[:3]
    aboutInfo=About.objects.filter(status=True)[:1].get()
    menu=Menu.objects.all()
    setingInfo=setting.objects.filter(status=True)[:1].get()  
    allService=Service.objects.filter(status=True)[:3]
    print(allService)
    
      
    data={
        'allFront':allFront,
        'imageBack':headerImage,
        'aboutInfo':aboutInfo,
        'menus':menu,
        'seting':setingInfo,
        'services':allService,
    }
    return render(request,'pages/index.html',data)

def about(request):
    return render(request,'pages/about.html')

def menu(request):
    return render(request,'pages/menu.html')

def reservations(request):
    return render(request,'pages/reservations.html')
