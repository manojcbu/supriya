from os import PathLike
from django.db import connection
from django.db.models.query_utils import Q
from django.shortcuts import render, redirect
import mysql.connector
# Create your views here.
#from django.contrib.auth.forms import User
from django.contrib import messages
from operator import itemgetter
from .forms import CropSoilForm
from django.shortcuts import redirect
from .models import User, question, CropData
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CropSoilForm




def home(request):
    return render(request, 'home.html')

def home2(request):
    return render(request, 'home2.html')

def registration (request):
    
    if request.method =="POST":
        
        user = User()

        user.username= request.POST['username']
        user.email= request.POST['email']
        user.password1= request.POST['password1']
        user.password2= request.POST['password2']
        if user.password1 != user.password2:
            messages.warning(request,"Passwords didn't match")
            return redirect("registration")
        elif user.email == "" or user.username=="" or user.password1=="" or user.password2=="":
            messages.warning(request, "Some feilds are empty")
            return redirect("registration")
        else:
            user.save()
            messages.success(request, "Registration Successful")
            return render(request, "home.html")
            
        
        
    else:
        return render(request, 'registration.html')


def login (request):
    connection = mysql.connector.connect(host="localhost",user="root",password="Corei5@1",database="maddi")
    cursor=connection.cursor()
    connection2 = mysql.connector.connect(host="localhost",user="root",password="Corei5@1",database="maddi")
    cursor2=connection2.cursor()
    sqlcommand = "select email from Krishi_Pradhan_user"
    sqlcommand2 = "select password1 from Krishi_Pradhan_user"
    cursor.execute(sqlcommand)
    cursor2.execute(sqlcommand2)

    e=[]
    p=[]
    for i in cursor:
        e.append(i)
    for j in cursor2:
        p.append(j)
    res = list(map(itemgetter(0),e))
    res2 = list(map(itemgetter(0),p))
    
    if request.method == "POST":
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        i=1
        k=len(res)
        while i<k:
            if res[i]==email and res2[i]==password1:
                messages.success(request,"Login Successful")
                return render(request,'home2.html')
                break
            i+=1
        else:
            messages.warning(request,"Check Email and Password")
            return redirect('login')

    else:
        return render(request, 'login.html')

def about (request):
    return render(request, 'about.html')

def organic(request):
    return render(request, 'organic.html')

def organic2(request):
    return render(request, 'organic2.html')

def about2 (request):
    return render(request, 'about2.html')



def questionnare(request):
    if request.method == 'POST':
        form = CropSoilForm(request.POST)
        if form.is_valid():
            saved_entry = form.save()
            messages.success(request, "Form submitted successfully!")
            # Pass the ID or other necessary data to the solution view
            return redirect('solution.html', saved_entry.id)
        else:
            print(form.errors)  # Print errors to console for debugging
            messages.error(request, "There was an error in your form. Please correct the errors below.")
            return render(request, 'questionnare.html', {'form': form})
    else:
        form = CropSoilForm()
    return render(request, 'questionnare.html', {'form': form})
    
def success(request):
    return render(request, 'success.html')
    
def solution(request):
    # Query the database to get crop details
    cropdata = Crop.objects.all()  # You may need to adjust this query based on your model structure and requirements

    # Prepare the data to pass to the template
    data = {
        'cropdata': crops  # Pass the queryset of crop objects to the template
    }

    return render(request, 'solution.html', data)