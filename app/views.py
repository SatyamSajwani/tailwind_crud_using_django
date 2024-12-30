from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import phone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, f"Username '{username}' already exists.")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "This email is already registered.")
            else:
                a_user=User.objects.create_user(username=username,password=password)
                a_user.save()
                
                messages.success(request, "Registration successful. Please log in.")
                return render(request,'login.html')
        else:
            messages.error(request, "Passwords do not match.")
    return render(request, 'ragister.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful.")
            return render(request,'index.html')  # Ensure 'home' is defined in your URLs
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('mainhome')

def home(request):
    return render(request,'home.html')

def index(request):
    phone_data = phone.objects.all()
    return render(request,'index.html',{'phone_data':phone_data})


def update(request, id):
    update=get_object_or_404(phone,id=id)
    if request.method == 'POST':
        update.name_of_phone=request.POST.get('name_of_phone')
        update.name_of_brand=request.POST.get('name_of_brand')
        update.color=request.POST.get('color')
        update.cetegory_of_phone=request.POST.get('cetegory_of_phone')
        update.price=request.POST.get('price')
        update.description=request.POST.get('description')
        update.save()
        return redirect('home')
    return render(request,'update.html',{'update':update})





def insert(request):
    if request.method == 'POST':
        name_of_phone = request.POST.get('name_of_phone')
        name_of_brand = request.POST.get('name_of_brand')
        price= request.POST.get('price')
        cetegory_of_phone = request.POST.get('cetegory_of_phone')
        color = request.POST.get('color_of_phone')
        description = request.POST.get('description')
        p=phone(name_of_phone=name_of_phone,color=color,cetegory_of_phone=cetegory_of_phone,price=price,name_of_brand=name_of_brand,description=description)
        p.save()
        return redirect('home')
    return render(request,'insert.html')
    

def delete(request,id):
    delete_phone=get_object_or_404(phone,id=id).delete()
    return redirect('home')