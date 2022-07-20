from audioop import reverse
from codecs import namereplace_errors
import email
from email.mime import image
from hashlib import new
from imaplib import _Authenticator
import json
from multiprocessing import context
import random
from sqlite3 import connect
import string
from types import new_class
from urllib import request
from django.forms import EmailInput
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mass_mail


from django.shortcuts import get_object_or_404, redirect, render
# import idna

# from urllib3 import Retry
from .models import *

from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework import status, viewsets
# from .serializers import CourseRatingSerializer, CollegeCategorySerializer, LessonDetailSerializer, LessonSerializer, CourseCategorySerializer, CourseDetailSerializer, CourseSerializer, CitySerializer, GetCollegeSerializer, CollegeSerializer, SkillSerializer, UserSerializer,login_serializers,QuizeSerializer
from django.db.models import Q
from django.conf import settings
from django.core.mail import send_mail
from rest_framework.response import Response
import random
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login as auth_login , logout
from django.db.models import Count
from django.http import HttpResponseRedirect, Http404, FileResponse





def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

@csrf_exempt
def register(request):
    if request.method =="POST":
        name=request.POST.get('username')
        name_value = name.split()
        if len(name_value) > 1:
            
            fname=name_value[0]
            lname=name_value[1]

        else:

            fname = name
            lname = ""
        
        email = request.POST.get('email')
        contact = request.POST.get('contact_number')
        password = request.POST.get('password')
        image = 'blog_image/no_image.jpg'
        otp = random.randint(1000,9999)
        
        if User.objects.filter(email=email) :  
            messages.success(request, 'This email id already register', extra_tags="success_msg")
            return redirect('/signup/')
        
        domain_name = get_current_site(request).domain
        token = str(random.random()).split('.')[1]
        message = 'please paste the link for verification'+ " " + f'http://{domain_name}/verify/{token}'
        subject = 'your account needs to be verified'
        from_email = str(settings.EMAIL_HOST_USER)
        recipient_list = [email]
        
        user = User.objects.create(username=name+str(otp), email=email, first_name = fname, last_name = lname)
        print(user)
        user.set_password(password)
        user.save()
        newuser = Registeruser(user=user,contact=contact,token=token,connect=email,image=image)
        print(newuser)
        newuser.save()
        send_mail(subject, message, from_email, recipient_list)    
        user.save()
        messages.success(request, 'We have sent an email to you Please check your mail' , extra_tags="email")

        return redirect( '/login/')
        # return redirect('login')
def varify(request, token):
    
    user = Registeruser.objects.get(token = token)
    # user1 = User.objects.get(email = user.connect)
    

    if user:
        user.is_verified = True
        user.save()
        messages.success(request, 'You are registerd successfully your email has been verified', extra_tags="success_msg")
        message = 'You are registerd successfully your email is getting verified....Thankyou!'
        subject = 'WELCOME ON CODERDAILY'    
        from_email = str(settings.EMAIL_HOST_USER)
        recipient_list = [user.connect]
        send_mail(subject, message, from_email, recipient_list)  
        return redirect('/login/') 
    
@csrf_exempt       
def login_user(request):
   
    if request.method=='POST':
        email  = request.POST.get('email')
        password  = request.POST.get('password')
        
        
    if User.objects.filter(email=email).exists() :   
        
        data = User.objects.get(email=email)
       
        data1 = Registeruser.objects.get(connect=email)
        
        value = check_password(password, data.password)
        
        user = authenticate(request, username=data,password=password)
        
        if value and data1.is_verified:
            
            auth_login(request, user)
            
            request.session['email'] = data.email
            request.session['name'] = data.username
            request.session['fname'] = data.first_name
            request.session['lname'] = data.last_name
            # request.session['id'] = data.id
            request.session['image'] = str(data1.image) 
            request.session['conncet'] = data.email
            
            # return render(request, 'courses')
            
            data1.status = "active"
            data1.save()
            
        
            return redirect('/product/')
        
        elif value == False and data1.is_verified :
            
            messages.success(request, 'Please check your email and password', extra_tags="worng_pass")
            return redirect( '/login/')
        
        
            
        else:
           
            messages.success(request, 'You are registerd successfully your email has been verified', extra_tags="success_msg")
            return redirect( '/login/')
        
    else :    
       
        messages.success(request, 'You are not register', extra_tags="worng_pass")
        return render(request, 'signup.html')

def Contact(request):
    return render(request, 'Contact.html')

def about_us(request):
    return render(request, 'aboutus.html')

def Blog(request):
    return render(request, 'Blog.html')

def product(request):
    return render(request, 'product.html')

def playgroup(request):
    return render(request, 'Playgroup-product.html')

def KG1(request):
    return render(request, 'KG-1.html')

def KG2(request):
    return render(request, 'KG-2.html')

def nursery(request):
    return render(request, 'Nursery.html')

def phonics(request):
    return render(request, 'Phonics.html')

def trackorder(request):
    return render(request, 'TrackOrder.html')

def privacypolicy(request):
    return render(request, 'privacy-policy.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def singleblog(request):
    return render(request, 'singleblog.html')

