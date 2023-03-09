from django.urls import path
from . import views

app_name='main'

urlpatterns = [
    path('', views.Login,name='login-light'),
    path('login-dark/', views.Login_dark,name='login-dark'),
    
    path('dashboard/', views.view_dashboard,name='dashboard'),  
    path('dashboard-dark/', views.view_dashboard_dark,name='dashboard-dark'),
    
    path('Change-password-light/', views.change_password,name='Change-password-light'),
    
    
    
    
    
    path('Change-password-dark/', views.Change_password_dark,name='Change-password-dark'),
    path('log-analysis-light/', views.log_analysis_light,name='log-analysis-light'),  
    path('log-analysis-dark/', views.log_analysis_dark,name='log-analysis-dark'),  
    path('ip-blocker-light/', views.ip_blocker_light,name='ip-blocker-light'),  
    path('ip-blocker-dark/', views.ip_blocker_dark,name='ip-blocker-dark'), 
    path('vulnerability-filtering-light/', views.vulnerability_filtering_light,name='vulnerability-filtering-light'),  
    path('vulnerability-filtering-dark/', views.vulnerability_filtering_dark,name='vulnerability-filtering-dark'),  
    path('Custom-filter-light/', views.Custom_filter_light,name='Custom-filter-light'),  
    path('Custom-filter-dark/', views.Custom_filter_dark,name='Custom-filter-dark'),  
    path('server-Configurations-light/', views.server_Configurations_light,name='server-Configurations-light'),  
    path('server-Configurations-dark/', views.server_Configurations_dark,name='server-Configurations-dark'),  
    path('Reporting-light/', views.Reporting_light,name='Reporting-light'),  
    path('Reporting-dark/', views.Reporting_dark,name='Reporting-dark'),  
    path('Users-and-Permissions-light/', views.Users_and_Permissions_light,name='Users-and-Permissions-light'),
    path('Users-and-Permissions-dark/', views.Users_and_Permissions_dark,name='Users-and-Permissions-dark'),






]
