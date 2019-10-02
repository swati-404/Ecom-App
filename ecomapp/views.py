from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from ecomapp.models import User
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
    prod = Product.objects.values('category_id', 'id')
    print(prod)
    allProds =[]
    
    catprods = Category.objects.values('category_name', 'id')
    print(catprods)
    cats = {item['category_name'] for item in catprods}
    for cat in cats:
        prod = Category.objects.filter(category_name=cat)
        if Category.category_id == Product.category_id:
            allProds.append(prod)
            print(allProds)
        
    param = {'prod':prod, 'catprods':catprods}
    return render(request, "product.html", param)

