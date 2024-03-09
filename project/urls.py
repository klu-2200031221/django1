from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.projecthomepage,name='projecthomepage'),
    path('adminhomepage',views.adminhomepage,name='adminhomepage'),
    path('studenthomepage',views.studenthomepage,name='studenthomepage'),
    path('facultyhomepage',views.facultyhomepage,name='facultyhomepage'),
    path('register',views.register,name='register'),
    path('register1', views.register1, name='register1'),
    path('login', views.login, name='login'),
    path('login2', views.login2, name='login2'),
    path('logout', views.logout, name='logout'),



]
