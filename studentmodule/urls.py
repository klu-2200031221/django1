from django.contrib import admin
from django.urls import path,include
from .import views


app_name='studentmodule'

urlpatterns = [
   path('viewcourse/',views.viewcourse,name='viewcourse'),
   path('coursedetails',views.coursedetails,name='coursedetails'),
   path('submit_form/',views.submit_form,name='submit_form'),
   path('addstudentprofile/',views.addstudentprofile,name='addstudentprofile'),
   path('applycourse/<int:cid>/', views.applycourse,name='applycourse'),
]
