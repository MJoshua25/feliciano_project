from django.shortcuts import render
from .models import *
from mainConfig.models import contact
# Create your views here.
def contactfonc(request):
    
    contacts=contact.objects.filter(status=True)[:1].get()

    myName=request.POST.get('name',False)
    myEmail=request.POST.get('email',False)
    mySubject=request.POST.get('subject',False)
    myMessage=request.POST.get('message',False)
    isSave=False
    print(myEmail,myName,mySubject,myMessage)

    if request.method == 'POST':
        if myName is not False and myEmail is not False and mySubject is not False:
           
            isSave=True
            try:
                print(myEmail,myName,mySubject,myMessage)
                newMessage=Message(name=myName,email=myEmail,sujet=mySubject,message=myMessage)
                newMessage.save()
                isSave=True
                print('message save ')
            except :
                isSave=False
                print('erreur de sauvegarde ')
                
    data={
        'error':isSave,
        'contact':contacts,
    }
    return render(request,'pages/contact.html',data)