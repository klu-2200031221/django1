from django.contrib import admin
from django.urls import path,include
from . import views


app_name = 'facultymodule'

urlpatterns = [
    path('course/',views.postcourse,name='postcourse'),
    path('add_coursedetails/',views.add_coursedetails,name='add_coursedetails'),
    path('view/',views.viewcoursedetails,name='viewcoursedetails'),
    path('edit/<int:cid>/', views.editcoursedetails, name='editcoursedetails'),
    path('delete/<int:cid>/', views.deletecoursedetails, name='deletecoursedetails'),
    path('courseapplicationlist/',views.courseapplicationlist,name='courseapplicationlist')

]
