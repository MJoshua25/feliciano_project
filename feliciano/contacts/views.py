from django.shortcuts import render
from .models import *
# Create your views here.
def contact(request):
    myName=request.POST.get('name',False)
    myEmail=request.POST.get('email',False)
    mySubject=request.POST.get('suject',False)
    myMessage=request.POST.get('message',False)
    isSave=False
    if request.method == 'POST':
        if myName is not False and myEmail is not False and mySubject is not False:
            try:
                print(myEmail,myName,mySubject,myMessage)
                newMessage=Message(name=myName,email=myEmail,suject=mySubject,message=myMessage)
                newMessage.save()
                isSave=True
                print('message save ')
            except:
                isSave=False
                print('erreur save message ')
                
    data={
        'error':isSave
    }
    return render(request,'pages/contact.html',data)