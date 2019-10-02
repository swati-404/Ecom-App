from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from ecomapp.models import User
from django.db import connection
#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Product, Category


# Create your views here.
def index(request):
    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        
        user_name = request.POST['user_name']
        mobile_No = request.POST['mobile_No']
        password = request.POST['password']
        address = request.POST['address']
        user = User(user_name=user_name, mobile_No=mobile_No, password=password, address=address)
        user.save()
        print(request)
    return render(request, 'registrationform.html')


    # if request.method == "POST":
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponse("User created successfully!")
 
    # else:
    #     form = UserCreationForm()
    #     return render(request, 'registrationform.html', {'form':form})


    # if request.method == "POST":
    #     user.save();
    # return render(request, 'registrationform.html')
    

def product(request):
    allProds =[]
    catprods = Category.objects.values('id', 'category_name')
    # print(catprods)
    for cat in catprods:
        prod = Product.objects.select_related().filter(category_id=cat["id"])
        # print(prod)
        allProds.append(prod)
    # print(allProds)
        
    param = {'prods':allProds, 'catprods':list(catprods)}
    return render(request, "product.html", param)

