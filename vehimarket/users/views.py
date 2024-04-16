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
from django.views.decorators.cache import never_cache
from django.shortcuts import render, get_object_or_404
from .models import CarListing
from .models import Accessory
from .models import Accessory, AccessoryImage
from django.urls import reverse
from .models import Payment
import razorpay
from django.shortcuts import render
from django.conf import settings
from decimal import Decimal
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from django_xhtml2pdf.utils import generate_pdf
from .models import Order, OrderItem
from django.shortcuts import render, HttpResponse
from django.template.loader import render_to_string
from django_xhtml2pdf.utils import generate_pdf
from .models import Order, OrderItem
from django.shortcuts import render
from .models import Order, OrderItem



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

@never_cache
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
    
@never_cache
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
    
@never_cache
@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('index')

@never_cache
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

@never_cache
@login_required(login_url='login')
def view_profile(request):
    # Get the user profile based on the username
    user_profile = users.objects.get(user=request.user)
    return render(request, 'view_profile.html',{'user': user_profile,} )

@never_cache
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
    
@never_cache
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

@never_cache
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


@never_cache
@login_required(login_url='login')
def viewcar(request):
    available_cars = CarListing.objects.filter(status='available').exclude(seller__user=request.user)
    return render(request, 'viewcar.html', {'available_cars': available_cars})


@login_required(login_url='admin_login') 
def admin_carview(request):
    car_listings = CarListing.objects.all()
    return render(request,'admin_carview.html', {'car_listings': car_listings})


@never_cache
@login_required(login_url='login') 
def cardetail(request, car_id):
    car = get_object_or_404(CarListing, pk=car_id)
    return render(request, 'cardetail.html', {'car': car})


@never_cache
@login_required(login_url='login') 
def car_booking(request, car_id):
    car = get_object_or_404(CarListing, pk=car_id)
    user = request.user

    if request.method == 'POST':
        # Check if the user already has a booking for this car
        existing_booking = CarBooking.objects.filter(user=user, car_listing=car).first()

        if existing_booking:
            # If a booking exists, redirect to payment directly
            return redirect('payment', car_id=car_id, booking_id=existing_booking.id)
        else:
            # If no booking exists, create a new one
            new_booking = CarBooking(user=user, car_listing=car)
            # You can add other fields to the CarBooking model as needed
            new_booking.save()

            # Redirect to the payment page with car_id and booking_id
            return redirect('payment', car_id=car_id, booking_id=new_booking.id)

    return render(request, 'car_booking.html', {'car': car})
    # carbook= get_object_or_404(CarListing, pk=car_id)
    # return render(request,'car_booking.html',{'car': carbook})


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


@never_cache
@login_required(login_url='login')
def chatwithadmin(request):
    if request.method == "POST":
        feedback_message = request.POST.get('feedback_message')
        if feedback_message:
            Feedback.objects.create(user=request.user, message=feedback_message)
            # You can add additional logic here (e.g., sending a confirmation email)
            return redirect('chatwithadmin')

    return render(request,'chatwithadmin.html')


def admin_viewchat(request):
    feedback_list = Feedback.objects.all()
    return render(request, 'admin_viewchat.html',{'feedback_list':feedback_list})



razorpay_api_key = settings.RAZORPAY_API_KEY
razorpay_secret_key = settings.RAZORPAY_API_SECRET

razorpay_client = Client(auth=(razorpay_api_key, razorpay_secret_key))

@login_required(login_url='login')
@never_cache
@csrf_exempt
def payment(request,car_id,booking_id):
    carbook= get_object_or_404(CarListing, pk=car_id)
    bookid = get_object_or_404(CarBooking, pk=booking_id)
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
    payment = Payment.objects.create(
        booking=bookid,
        car=carbook,
        user=request.user,  # Assuming the user is authenticated
        is_paid=True,
        amount=amount
    )
    payment.save()

    # Update the CarListing status to 'sold'
    carbook.status = 'sold'
    carbook.save()

    context = {
        'razorpay_api_key': razorpay_api_key,
        'amount': order_data['amount'],
        'currency': order_data['currency'],
        'order_id': order['id'],
    }
    return render(request, 'payment.html', context)


def adminaccessoriesadd(request):
    if request.method == 'POST':
        accessory_name = request.POST.get('accessory_name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        brand = request.POST.get('brand')
        category = request.POST.get('category')
        quantity = request.POST.get('quantity')
        warranty = request.POST.get('warranty')
        image1 = request.FILES['images1']
        image2 = request.FILES['images2']
        image3 = request.FILES['images3']
        image4 = request.FILES['images4']
        
        if not (accessory_name and description and price and brand and category and quantity and warranty):
            # If any of the required fields are missing, render the form again with an error message
            return render(request, 'admin_accessoriesadd.html', {'error': 'All fields are required'})
        
        try:
            # Create an instance of Accessory model
            accessory = Accessory.objects.create(
                accessory_name=accessory_name,
                description=description,
                price=price,
                brand=brand,
                category=category,
                quantity=quantity,
                warranty=warranty
            )

            
            accessoryimage = AccessoryImage.objects.create(accessory=accessory,image1=image1,image2=image2,image3=image3,image4=image4,)
            # images = []
            # for i in range(1, 5):  # Assuming you have four image input fields
            #     image_file = request.FILES.get(f'images{i}')
            #     if image_file:
            #         # Create AccessoryImage instance and link it to the accessory
            #         image_field_name = f'image{i}'
            #         image_instance = AccessoryImage(accessory=accessory, **{image_field_name: image_file})
            #         images.append(image_instance)
            # AccessoryImage.objects.bulk_create(images)

            # Redirect to a success page or anywhere you want
            return redirect('adminaccessoriesadd')
        except Exception as e:
            # If an error occurs during object creation, render the form again with an error message
            return render(request, 'admin_accessoriesadd.html', {'error': str(e)})
    return render(request,'admin_accessoriesadd.html')



def accessories_list(request):
    accessories = Accessory.objects.all()
    return render(request, 'accessories_list.html', {'accessories': accessories})


def update_accessory(request, accessory_id):
    # Get the accessory object by its primary key
    accessory = get_object_or_404(Accessory, pk=accessory_id)
    accessory_images = AccessoryImage.objects.filter(accessory=accessory)
    if request.method == 'POST':
        accessory.accessory_name = request.POST['accessory_name']
        accessory.description = request.POST['description']
        accessory.price = request.POST['price']
        accessory.brand = request.POST['brand']
        accessory.category = request.POST['category']
        accessory.quantity = request.POST['quantity']
        accessory.warranty = request.POST['warranty']
        
        # Save the updated accessory
        accessory.save()
        
        # Handle image updates
        for i in range(1, 5):
            image_field_name = f'image{i}'
            if image_field_name in request.FILES:
                # Get the corresponding accessory image object or create a new one if it doesn't exist
                accessory_image, created = AccessoryImage.objects.get_or_create(accessory=accessory)
                # Update the image field
                setattr(accessory_image, image_field_name, request.FILES[image_field_name])
                # Save the accessory image object
                accessory_image.save()
        
        # Redirect to a success page or wherever needed
        return redirect('admin_home')
    return render(request, 'update_accessory.html', {'accessory': accessory})



def delete_accessory(request, pk):
    # Get the accessory object by its primary key
    accessory = get_object_or_404(Accessory, pk=pk)

    if request.method == 'POST':
        # Delete the accessory object
        accessory.delete()
        return redirect('accessories_list')  # Redirect to the accessories listing page

    # Render the delete confirmation page with the accessory object
    return render(request, 'delete_accessory.html', {'accessory': accessory})


@never_cache
@login_required(login_url='login')
def accessory_view(request):
    accessories = Accessory.objects.all()
    accessory_images = AccessoryImage.objects.all() 
    return render(request,'accessory_view.html',{'accessories': accessories, 'accessory_images': accessory_images})



def admin_addcategory(request):
    if request.method == 'POST':
        accessory_name = request.POST.get('accessory_name')
        if accessory_name:  # Check if accessory_name is not empty
            category = Category(name=accessory_name)
            category.save()
            return redirect('admin_addcategory')  # Assuming you have a URL named 'category_list'
    return render(request,'admin_addcategory.html')



@never_cache
@login_required(login_url='login')
def accessories_detail(request,accessory_id):
    accessory = get_object_or_404(Accessory, pk=accessory_id)
    accessory_images = AccessoryImage.objects.filter(accessory=accessory)
    return render(request,'accessories_detail.html', {'accessory': accessory, 'accessory_images': accessory_images})




@never_cache
@login_required(login_url='login')
def accessories_wishlist(request):
    user_wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request,'accessories_wishlist.html', {'user_wishlist_items': user_wishlist_items})



@never_cache
@login_required(login_url='login')
def add_to_wishlist(request, accessory_id):
    accessory = Accessory.objects.get(pk=accessory_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    if not wishlist.accessories.filter(pk=accessory_id).exists():
        wishlist.accessories.add(accessory)
    return redirect('accessories_detail', accessory_id=accessory_id)



@never_cache
@login_required(login_url='login')
def remove_from_wishlist(request, item_id):
    if request.method == 'POST':
        wishlist_item = get_object_or_404(Wishlist, id=item_id)
        wishlist_item.delete()
        return redirect('accessories_wishlist')  # Redirect to the wishlist page after deletion
    else:
        return redirect('accessories_wishlist') 
    


def check_availability(request):
    if request.method == 'GET':
        accessory_id = request.GET.get('accessory_id')
        accessory = get_object_or_404(Accessory, pk=accessory_id)
        available = accessory.quantity > 0  # Check if the quantity is greater than 0
        return JsonResponse({'available': available})
    else:
        return JsonResponse({'error': 'Invalid request method'})



def add_to_cart(request, accessory_id):
    accessory = get_object_or_404(Accessory, pk=accessory_id)
    if request.method == 'POST':
        quantity = request.POST.get('qty', '1')  # Default to '1' if 'qty' is not provided
        if str(quantity).isdigit():  # Ensure quantity is a valid integer
            quantity = int(quantity)
            if 1 <= quantity <= 10:  # Ensure quantity is between 1 and 10
                user = request.user  # Assuming you have user authentication enabled
                existing_cart_item = AddToCart.objects.filter(user=user, accessory=accessory).first()

                if existing_cart_item:
                    # Item already exists in the cart, handle this scenario as needed
                    # For example, show a message to the user that the item is already in the cart
                    return redirect('cart')  # Redirect to the cart page or any other page
                else:
                    # Item does not exist in the cart, create a new entry
                    add_to_cart_item = AddToCart.objects.create(user=user, accessory=accessory, quantity=quantity)
                    return redirect('cart')  # Replace 'cart' with your actual cart URL name

    # Handle invalid quantity or other scenarios as needed
    return redirect('accessories_detail', accessory_id=accessory_id)




from django.shortcuts import render
from .models import AddToCart

def cart(request):
    # Get all the cart items for the current user
    cart_items = AddToCart.objects.filter(user=request.user)
    
    context = {
        'cart_items': cart_items,
        'your_accessory_id_variable': cart_items.first().accessory.id if cart_items.exists() else None,  # Assuming you want the ID of the first item in the cart
    }
    return render(request, 'cart.html', context)





def remove_from_cart(request, item_id):
    # Get the cart item to be removed
    cart_item = get_object_or_404(AddToCart, id=item_id)
    
    # Check if the cart item belongs to the logged-in user
    if cart_item.user == request.user:
        cart_item.delete()
        messages.success(request, 'Item removed from cart successfully.')
    else:
        messages.error(request, 'You are not authorized to remove this item from the cart.')
    
    return redirect('cart')


razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))

def accessory_payment(request):
    # Fetch the cart items for the current user
    cart_items = AddToCart.objects.filter(user=request.user)
    
    currency = 'INR'
    
    # Calculate the subtotal of the cart items
    sub_total = sum([
        item.accessory.price * item.quantity
        if item.accessory is not None and item.quantity is not None
        else 0
        for item in cart_items
    ])
    
    # Calculate the total price as a Decimal
    total_price = Decimal(sub_total)
    
    # Convert the total price to an integer amount in paise (100 paise = 1 rupee)
    amount = int(total_price * 100)
    
    # Create a Razorpay order with the calculated amount
    razorpay_order = razorpay_client.order.create(dict(amount=amount, currency=currency, payment_capture='0'))
    
    razorpay_order_id = razorpay_order["id"]
    
    # Create the Order object and save it
    order = Order.objects.create(
        user=request.user,
        amount=amount,
        razorpay_order_id=razorpay_order_id,
        payment_status=Order.PaymentStatusChoices.PENDING
    )
    
    # Loop through cart items to store accessory ID and quantity in OrderItem instances
    for item in cart_items:
        order_item = OrderItem.objects.create(order=order, accessory=item.accessory, quantity=item.quantity)
    
    # Prepare context data to pass to the template
    context = {
        'cart_items': cart_items,
        'amount': amount,
        'razorpay_order_id': razorpay_order_id,
        'razorpay_merchant_key': settings.RAZORPAY_API_KEY,
        'razorpay_amount': amount,
        'currency': currency,
        'callback_url': reverse('payment_confirm'),  # Assuming 'payment_confirm' is the correct URL name
    }

    # Render the payment page with the context data
    return render(request, "payment_accessories.html", context=context)



@csrf_exempt
def payment_confirm(request):
    if request.method == "POST":
        payment_id = request.POST.get('razorpay_payment_id', '')
        razorpay_order_id = request.POST.get('razorpay_order_id', '')
        signature = request.POST.get('razorpay_signature', '')
        params_dict = {
            'razorpay_order_id': razorpay_order_id,
            'razorpay_payment_id': payment_id,
            'razorpay_signature': signature,
        }

        result = razorpay_client.utility.verify_payment_signature(params_dict)
        if result is not None:
            # Fetch the order using razorpay_order_id
            order = Order.objects.get(razorpay_order_id=razorpay_order_id)
            # Update the payment status and create a Payment instance
            order.payment_status = Order.PaymentStatusChoices.SUCCESSFUL
            order.save()
            
            # Fetch the cart items associated with the current user
            cart_items = AddToCart.objects.filter(user=request.user)

            # Loop through cart items to update accessory stock and delete cart items
            for item in cart_items:
                accessory = item.accessory
                if accessory.quantity >= item.quantity:
                    accessory.quantity -= item.quantity
                    accessory.save()
                else:
                    return render(request, 'paymentfail.html', {'messages': 'Insufficient stock'})

            cart_items.delete()  # Delete cart items after successful payment

            # Redirect to the invoice area with the order ID
            return redirect('home')
        else:
            return render(request, "paymentfail.html")
    else:
        return redirect('accessory_payment')  # Redirect to the payment page if not a POST request


def view_orders(request):
    # Assuming you have a way to identify the current user
    user = request.user
    # Filter orders by user and payment status
    orders = Order.objects.filter(user=user, payment_status=Order.PaymentStatusChoices.SUCCESSFUL)
    context = {'orders': orders}
    return render(request, 'orders.html', context)

