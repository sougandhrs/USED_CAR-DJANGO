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
from .models import CarListing
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
import razorpay
from django.conf import settings
from django.http import HttpResponseBadRequest
from razorpay import Client

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



@csrf_exempt
def register(request):
    if request.method == 'POST':
        email = request.POST['txt1']
        password = request.POST['txt11']

        # Check if a user with the given email already exists
        if User.objects.filter(username=email).exists():
            message = 'Email already registered.'
            messages.error(request, message)
        else:
            myuser = User.objects.create_user(username=email, email=email, password=password)
            myuser.save()

            fname = request.POST['txt2']
            lname = request.POST['txt3']
            dob = request.POST['txt4']
            contact = request.POST['txt5']
            house = request.POST['txt6']
            place = request.POST['txt7']
            pin = request.POST['txt8']
            profile = request.FILES.get('txt9', False)

            data = users(user=myuser, u_fname=fname, u_lname=lname, u_dob=dob, u_contact=contact, u_house=house, u_place=place, u_pin=pin, u_profile=profile)
            data.save()

            message = 'Data Inserted Successfully'
            messages.success(request, message)

    return render(request, 'registration.html')


@login_required(login_url='login') 
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
    

@login_required(login_url='login')  
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
    

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('index')


@login_required(login_url='login') 
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


@login_required(login_url='login')
def view_profile(request):
    # Get the user profile based on the username
    user_profile = users.objects.get(user=request.user)
    return render(request, 'view_profile.html',{'user': user_profile,} )


@login_required(login_url='admin_login')
def admin_home(request):
    if 'userid1' in request.session:
        u_id=request.session['userid1']
        usr=User.objects.get(id=u_id)
        response= render(request, 'admin_home.html',{'user1':usr})
        response['Cache-Control']='no-store,must-revalidate'
        return response
    else:
        return redirect('admin_login')
    

@login_required(login_url='admin_login')
def admin_userview(request):
    users_data = User.objects.filter(is_superuser=False)
    
    # Get additional user details from the 'users' model
    user_details = users.objects.filter(user__in=users_data)

    # Combine the 'User' and 'users' data into a single list
    user_list = []
    for user in users_data:
        user_detail = user_details.filter(user=user).first()
        user_list.append((user, user_detail))
    return render(request,'admin_userview.html', {'user_list': user_list})


@login_required(login_url='login') 
def sellcar(request):
    if request.method == 'POST':
        make = request.POST['make']
        model = request.POST['model']
        year = request.POST['year']
        price = request.POST['price']
        description = request.POST['description']
        image_1 = request.FILES['image_1']
        image_2 = request.FILES['image_2']
        image_3 = request.FILES['image_3']
        image_4 = request.FILES['image_4']
        image_5 = request.FILES['image_5']
        engine_type = request.POST['engine_type']
        transmission_type = request.POST['transmission_type']
        exterior_color = request.POST['exterior_color']
        interior_color = request.POST['interior_color']
        fuel_type = request.POST['fuel_type']
        kilometer_driven = request.POST['km']
        owner=request.POST['owner']

        
        # Create a new car listing
        car_listing = CarListing(
            seller=request.user.users,  # Assuming request.user is authenticated and has a related users instance
            make=make,
            model=model,
            year=year,
            price=price,
            description=description,
            image_1=image_1,
            image_2=image_2,
            image_3=image_3,
            image_4=image_4,
            image_5=image_5,
            engine_type=engine_type,
            transmission_type=transmission_type,
            exterior_color=exterior_color,
            interior_color=interior_color,
            fuel_type=fuel_type,
            kilometer_driven = kilometer_driven,
            owner=owner,
        )
        car_listing.save()
        return redirect('home')
    return render(request,'sellcar.html')



def admin_login(request):
    if request.method == 'POST':
        email = request.POST.get('txt1')
        password = request.POST.get('txt2')

        # Authenticate the user
        user1 = authenticate(request, username=email, password=password)

        if user1 is not None:
            if user1.is_superuser:
                # User is a superuser
                auth_login(request, user1)
                request.session['userid1']=user1.id
                return redirect('admin_home')  # Redirect to the admin home page
            else:
                messages.error(request, 'Invalid username or password for a superuser.')
        else:
            messages.error(request, 'Invalid username or password.')
    response= render(request, 'admin_login.html')
    response['Cache-Control']='no-store,must-revalidate'
    return response


@login_required(login_url='admin_login')
def admin_logout_view(request):
    logout(request)
    return redirect('index')


@login_required(login_url='login')
def viewcar(request):
    available_cars = CarListing.objects.filter(status='available').exclude(seller__user=request.user)

    return render(request, 'viewcar.html', {'available_cars': available_cars})

@login_required(login_url='admin_login') 
def admin_carview(request):
    car_listings = CarListing.objects.all()
    return render(request,'admin_carview.html', {'car_listings': car_listings})



from django.shortcuts import render, get_object_or_404
from .models import CarListing

@login_required(login_url='login') 
def cardetail(request, car_id):
    car = get_object_or_404(CarListing, pk=car_id)
    return render(request, 'cardetail.html', {'car': car})

@login_required(login_url='login') 
def car_booking(request, car_id):
    carbook= get_object_or_404(CarListing, pk=car_id)
    return render(request,'car_booking.html',{'car': carbook})


@login_required(login_url='admin_login') 
def admin_assign_timeslots(request):
    if request.method == 'POST':
        date = request.POST['date']
        time_slots = request.POST.getlist('time_slots')

        # Validate if the timeslots are available
        for time_slot in time_slots:
            # Create a new TestDrive instance for each timeslot
            test_drive = TestDrive(date=date, time_slot=time_slot, is_booked=False)
            test_drive.save()

        messages.success(request, 'Timeslots assigned successfully!')
        return redirect('admin_home')
    return render(request,'admin_assign_timeslots.html')


razorpay_api_key = settings.RAZORPAY_API_KEY
razorpay_secret_key = settings.RAZORPAY_API_SECRET

razorpay_client = Client(auth=(razorpay_api_key, razorpay_secret_key))

@csrf_exempt
def payment(request,car_id):
    carbook= get_object_or_404(CarListing, pk=car_id)
    # Amount to be paid (in paisa), you can change this dynamically based on your logic
    amount = 2000000

    # Create a Razorpay order (you need to implement this based on your logic)
    order_data = {
        'amount': amount,
        'currency': 'INR',
        'receipt': 'order_rcptid_11',
        'payment_capture': '1',  # Auto-capture payment
    }

    # Create an order
    order = razorpay_client.order.create(data=order_data)

    context = {
        'razorpay_api_key': razorpay_api_key,
        'amount': order_data['amount'],
        'currency': order_data['currency'],
        'order_id': order['id'],
    }

    return render(request, 'payment.html', context)