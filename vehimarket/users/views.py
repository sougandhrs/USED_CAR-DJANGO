from django.shortcuts import render,redirect
from . models import *
from django.http import JsonResponse
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .models import users
from datetime import datetime

# Create your views here.
def index(request):
    print(request.user)
    return render(request,'index.html')

def login_view(request):
    if request.method=='POST':
        email=request.POST['txt1']
        password=request.POST['txt2']
        user=authenticate(request,username=email,password=password)
        if user is not None:
            auth_login(request, user)
            request.session['userid']=user.id
            return redirect('home')
        else:
            messages.error(request,'INVALID Username or Password')
            return redirect('login')
        # try:
        #     user=users.objects.get(u_email=email,u_password=password)
        #     request.session['userid']=user.id
        #     return redirect('home')
        # except users.DoesNotExist:l
        #     return render(request,'login.html',{'errmsg':'LOGIN FAILED'}) 
    response= render(request, 'login.html')
    response['Cache-Control']='no-store,must-revalidate'
    return response

def register(request):
    message=""
    if request.method=='POST':
        email=request.POST['txt1']
        fname=request.POST['txt2']
        lname=request.POST['txt3']
        dob=request.POST['txt4']
        contact=request.POST['txt5']
        house=request.POST['txt6']
        place=request.POST['txt7']
        pin=request.POST['txt8']
        profile=request.FILES.get('txt9', False)
        # rdate=request.POST['txt10']
        password=request.POST['txt11']
        # cpassword=request.POST['txt12']
        myuser=User.objects.create_user(username=email,email=email,password=password)
        myuser.save()

        data=users(user=myuser,u_fname=fname,u_lname=lname,u_dob=dob,u_contact=contact,u_house=house,u_place=place,u_pin=pin,u_profile=profile)
        data.save()
        message='Data Inserted Successfully'
    return render(request,'registration.html',{'msg':message})

def nav(request):
    return render(request,'nav.html')

@csrf_exempt
def checkemailavailable(request):
    useremail=request.POST['email']
    emailavailable=User.objects.filter(email=useremail).exists()
    if emailavailable:
        return JsonResponse({
            'is_available':False
        })
    else:
        return JsonResponse({
            'is_available':True
        })
    
def home(request):
    if 'userid' in request.session:
        u_id=request.session['userid']
        usr=User.objects.get(id=u_id)
        response= render(request, 'Home.html',{'user':usr})
        response['Cache-Control']='no-store,must-revalidate'
        return response
    else:
        return redirect('login')
    # return render(request,'Home.html',{'user':usr})
    
def logout_view(request):
    logout(request)
    return redirect('index')


def update_profile(request):
    user_profile = users.objects.get(user=request.user)

    if request.method == 'POST':
        # Handle the form submission here
        user_profile.u_fname = request.POST.get('u_fname')
        user_profile.u_lname = request.POST.get('u_lname')
        
        # Convert the date input to a Python date object
        dob_input = request.POST.get('u_dob')
        if dob_input:
            user_profile.u_dob = datetime.strptime(dob_input, '%Y-%m-%d')
        
        user_profile.u_contact = request.POST.get('u_contact')
        user_profile.u_house = request.POST.get('u_house')
        user_profile.u_place = request.POST.get('u_place')
        user_profile.u_pin = request.POST.get('u_pin')
        
        # Handle the profile image here (you'll need to save the file)
        if 'u_profile' in request.FILES:
            user_profile.u_profile = request.FILES['u_profile']

        user_profile.save()
        return redirect('home')  # Create a URL for profile update success

    # Convert the u_dob date to a string in 'YYYY-MM-DD' format
    dob_initial = user_profile.u_dob.strftime('%Y-%m-%d')

    return render(request, 'update_profile.html', {
        'user': user_profile,
        'dob_initial': dob_initial,
    })


def view_profile(request):
    # Get the user profile based on the username
    user_profile = users.objects.get(user=request.user)
    return render(request, 'view_profile.html',{'user': user_profile,} )
