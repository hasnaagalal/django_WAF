from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse



def dashboard (request):
    return render (request,'main/dashboard.html',{'title':"dashboard"})

def dashboard_dark (request):
    return render (request,'main/dashboard-dark.html',{'title':"dashboard-dark"})

def log_analysis_light (request):
    return render (request,'main/log-analysis-light.html',{'title':"log-analysis-light"})

def log_analysis_dark (request):
    return render (request,'main/log-analysis-dark.html',{'title':"log-analysis-dark"})

def ip_blocker_light (request):
    return render (request,'main/ip-blocker-light.html',{'title':"ip-blocker-light"})

def ip_blocker_dark (request):
    return render (request,'main/ip-blocker-dark.html',{'title':"ip-blocker-dark"})

def vulnerability_filtering_light (request):
    return render (request,'main/vulnerability-filtering-light.html',{'title':"vulnerability-filtering-light"})

def vulnerability_filtering_dark (request):
    return render (request,'main/vulnerability-filtering-dark.html',{'title':"vulnerability-filtering-dark"})

def Custom_filter_light (request):
    return render (request,'main/Custom-filter-light.html',{'title':"Custom-filter-light"})

def Custom_filter_dark(request):
    return render (request,'main/Custom-filter-dark.html',{'title':"Custom-filter-dark"})

def server_Configurations_light (request):
    return render (request,'main/server-Configurations-light.html',{'title':"server-Configurations-light"})

def server_Configurations_dark (request):
    return render (request,'main/server-Configurations-dark.html',{'title':"server-Configurations-dark"})

def Reporting_light (request):
    return render (request,'main/Reporting-light.html',{'title':"Reporting-light "})

def Reporting_dark (request):
    return render (request,'main/Reporting-dark.html',{'title':"Reporting-dark "})

def Change_password_light(request):
    return render (request,'main/Change-password-light.html',{'title':"Change-password-light"})

def Change_password_dark(request):
    return render (request,'main/Change-password-dark.html',{'title':"Change-password-dark"})

def Users_and_Permissions_light(request):
    return render (request,'main/Users-and-Permissions-light.html',{'title':"Users-and-Permissions-light"})

def Users_and_Permissions_dark(request):
    return render (request,'main/Users-and-Permissions-dark.html',{'title':"Users-and-Permissions-dark"})


def login_light(request):
    return render (request,'main/login-light.html',{'title':" login-light"})

def login_dark(request):
    return render (request,'main/login-dark.html',{'title':" login-dark"})



def Login(request):
    if request.method=="POST":
      username = request.POST.get('username')
      password = request.POST.get('password')
      user = authenticate(request, username=username, password=password)
      if user is not None:
        login(request, user)
        return redirect('main:dashboard')

        
      else:
        return HttpResponse("Username or passward isnot correct ")
    return render (request, 'main/login-light.html')
        






