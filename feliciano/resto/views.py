from django.shortcuts import render
import datetime


from mainConfig.models import *
from .models import *
from customers.models import *
from blog_App.models import Article


# Create your views here.

def index(request):
    allFront = Front.objects.filter(status=True)[:1].get()
    headerImage=headBackImage.objects.filter(status=True)[:3]
    aboutInfo=About.objects.filter(status=True)[:1].get()
    menu=Menu.objects.all()
    setingInfo=setting.objects.filter(status=True)[:1].get()  
    allService=Service.objects.filter(status=True)[:3]
    masters=MasterChef.objects.all()
    allTesti=Testi.objects.all()
    allBlog=Article.objects.filter(status=True)[:3]
    contacts=contact.objects.filter(status=True)[:1].get()
    programme=WorkingHours.objects.filter(status=True)[:7]
    munday=WorkingHours.objects.filter(day='Lundi')[:1].get()
    samdi=WorkingHours.objects.filter(day='Vendredi')[:1].get()
    
    isSave=False
    myName=request.POST.get('name',False)
    myEmail=request.POST.get('email',False)
    myPhone=request.POST.get('phone',False)
    myDate=request.POST.get('date',False)
    myTime=request.POST.get('time',False)
    myPlace=request.POST.get('place',False)
    if request.method =='POST':
        if  myDate is not False :
            try:
                newRdv=Reservation(name=myName,email=myEmail,phone=myPhone,date=myDate,time=myTime,place_number=myPlace)
                newRdv.save()
                isSave=True
                print('rendevous enregistre')
            except:
                print('Erreur enregistrement rendevous ')
                isSave=False
    data={
        'allFront':allFront,
        'imageBack':headerImage,
        'aboutInfo':aboutInfo,
        'menus':menu,
        'seting':setingInfo,
        'services':allService,
        'masters':masters,
        'newRdv':isSave,
        'allTesti':allTesti,
        'allBlog':allBlog,
        'contact':contacts,
        'workingHours':programme,
        'lundi':munday,
        'vendredi':samdi
    }
    return render(request,'pages/index.html',data)

def about(request):
    return render(request,'pages/about.html')

def menu(request):
    return render(request,'pages/menu.html')

def reservations(request):
    isSave=False
    name=request.POST.get('name')
    email=request.POST.get('email')
    phone=request.POST.get('phone')
    date=request.POST.get('date')
    time=request.POST.get('time')
    place=request.POST.get('place')
    print(name,email,phone,date,time,place)
    try:
        newRdv=Reservation(name=name,email=email,phone=phone,date=date,time=time,place_number=place)
        newRdv.save()
        isSave=True
    except:
        isSave=False
        print('Erreur d\'enregistrement ')
    
    return render(request,'pages/reservations.html')
