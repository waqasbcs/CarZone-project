from django.shortcuts import render, redirect
from . models import Team
from cars.models import car
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages
from base64 import encodebytes
from base64 import b64encode




# Create your views here.

#homepage: 
def home(request):
    teams = Team.objects.all()
    featured_cars = car.objects.order_by('-created_date').filter(is_feature=True)
    all_cars = car.objects.order_by('-created_date')

    model_search = car.objects.values_list('model',flat=True).distinct()
    city_search = car.objects.values_list('city',flat=True).distinct()
    year_search = car.objects.values_list('year',flat=True).distinct()
    body_style_search = car.objects.values_list('body_style',flat=True).distinct()
    
    data = {
        'teams':teams,
        'featured_cars':featured_cars,
        'all_cars':all_cars,
        'model_search':model_search,
        'city_search':city_search,
        'year_search':year_search,
        'body_style_search':body_style_search
        
    }
    return render(request, 'pages/home.html',data)

#about: 
def about(request):
    teams = Team.objects.all()
    data = {
        'teams':teams
    }
    return render(request, 'pages/about.html',data)

#services:
def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        email_subject = 'You have a new message from the CarZone website'
        message_body = f'Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}'

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email

        # Convert initial_response to a string if it's a tuple
        initial_response = admin_email
        if isinstance(initial_response, tuple):
            initial_response = initial_response[0]

        # Encode the initial_response as bytes and convert to string
        encoded_response = b64encode(initial_response.encode('ascii')).decode('ascii')

        send_mail(
            email_subject,
            message_body,
            'waqasaliy2945@gmail.com',
            [admin_email],
            fail_silently=False,
            auth_user=admin_email,
            auth_password=encoded_response,
        )
        # Rest of your code
        messages.success(request,'Thank you for contacting us.we will get back to you shortly')
        return redirect('contact')
    return render(request, 'pages/contact.html')
