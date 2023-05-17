from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def profile(request):
    template = loader.get_template('profile.html')
    return HttpResponse(template.render())

def login(request):
    template = loader.get_template('login_signup.html')
    context = {
        'mode' : 'login'
    }
    return HttpResponse(template.render(context, request))