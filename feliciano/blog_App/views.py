from django.shortcuts import render

# Create your views here.
def blog(request):
    return render(request,'pages/blog.html')

def single_blog(request):
    return render(request,'pages/single_blog.html')
