from django.shortcuts import render
from time import strftime
# Create your views here.
def index(request):
    return render(request,'blog/blog.html', {'now': strftime('%c')})

def bio(request):
    return render(request,'blog/bio.html', {'now': strftime('%c')})

def tips(request):
    return render(request,'blog/tips.html', {'now': strftime('%c')})
    


