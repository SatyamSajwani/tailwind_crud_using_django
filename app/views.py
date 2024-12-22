from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')


def update(request):
    return render(request,'update.html')


def login(request):
    return render(request,'login.html')


def ragister(request):
    return render(request,'ragister.html')