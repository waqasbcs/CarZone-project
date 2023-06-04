from django.shortcuts import render, redirect
from django.contrib import messages
from .models import contact
from django.core.mail import send_mail
from django.contrib.auth.models import User

def inquiry(request):
    if request.method == 'POST':
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = contact.objects.all().filter(car_id=car_id, user_id=user_id)
            
            if has_contacted:
                messages.error(request, "You have already inquired about this car. Please wait...")
                return redirect('/cars' + car_id)
                
        contact_instance = contact(
            car_id=car_id, car_title=car_title, user_id=user_id,
            first_name=first_name, last_name=last_name,
            customer_need=customer_need, city=city, state=state,
            email=email, phone=phone, message=message
        )
        
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
                                                   
        send_mail(
                  'New Car Inquiry',
                  'your have a new car inquiry' + car_title + '.please login to your admin panel for  more information..',
                  'waqasaliy2945@gmail.com', 
                  [admin_email],
                  fail_silently=False,

         )

        
        # Save the contact instance to the database
        contact_instance.save()
        
        messages.success(request, 'Your request has been submitted. We will get back to you soon.')
        return redirect('/cars' + car_id)

        
        
        
        
