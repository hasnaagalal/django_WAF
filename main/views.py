from django.shortcuts import render

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
