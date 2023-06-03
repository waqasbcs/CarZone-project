from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from contacts.models import contact
from django.contrib.auth.decorators import login_required


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,email=email,password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Login successful')
            return redirect('dashboard')   
        else:
            messages.error(request, 'invalid login credentials')
            return redirect('login')         
    return render(request,'accounts/login.html')
  

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password= request.POST['confirm_password']
         # Check if any of the required fields are empty
        if not firstname or not lastname or not email or not password or not confirm_password or not username:
            messages.error(request, 'Please fill all the required fields.')
            return redirect('register')
        
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request,'User name already exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'email already exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname,username=username,email=email,password=password)
                    auth.login(request, user)
                    messages.success(request,'You are now logged in')
                    return redirect('dashboard')
                    user.save()
                    messages.success(request,'you are registered successfully')
                    return redirect('login')
        else:
            messages.error(request,'password does not match')
            return redirect('register') 
    else:
        return render(request,'accounts/register.html')

@login_required(login_url = 'login')
def dashboard(request):
    user_inquiry = contact.objects.order_by('-create_date').filter(user_id=request.user.id)
    data = {
        'inquiries':user_inquiry,
    } 
    return render(request,'accounts/dashboard.html',data)

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return redirect('home')



