from django.urls import path
from . import views

app_name='main'

urlpatterns = [
    path('dashboard/', views.dashboard,name='dashboard'),  
    path('dashboard-dark/', views.dashboard_dark,name='dashboard-dark'),
    path('log-analysis-light/', views.log_analysis_light,name='log-analysis-light'),  
    path('log-analysis-dark/', views.log_analysis_dark,name='log-analysis-dark'),  
    path('ip-blocker-light/', views.ip_blocker_light,name='ip-blocker-light'),  
    path('ip-blocker-dark/', views.ip_blocker_dark,name='ip-blocker-dark'), 
    path('vulnerability-filtering-light/', views.vulnerability_filtering_light,name='vulnerability-filtering-light'),  
    path('vulnerability-filtering-dark/', views.vulnerability_filtering_dark,name='vulnerability-filtering-dark'),  
    path('Custom-filter-light/', views.Custom_filter_light,name='Custom-filter-light'),  
    path('Custom-filter-dark/', views.Custom_filter_dark,name='Custom-filter-dark'),  



 


    

  


]
