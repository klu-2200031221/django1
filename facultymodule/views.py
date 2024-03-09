from django.shortcuts import render, get_object_or_404, redirect
from .models import *
# Create your views here.
def postcourse(request):
    return render(request,'facultymodule/postcourse.html')

def add_coursedetails(request):
    if request.method=='POST':
        courseid=request.POST.get('courseid')
        coursename=request.POST.get('coursename')
        offeredby=request.POST.get('offeredby')
        offeringyear=request.POST.get('offeringyear')
        credits=request.POST.get('credits')

        coursedetails=courseDetails(
          courseid=courseid,
          coursename=coursename,
          offeredby=offeredby,
          offeringyear=offeringyear,
          credits=credits,
    )
        coursedetails.save()
        return render(request,'facultymodule/datainserted.html')
    return render(request,'facultyhomepage.html')

def viewcoursedetails(request):
    coursedetailslist=courseDetails.objects.all()
    return render(request,'facultymodule/viewcoursedetails.html',{'coursedetailslist':coursedetailslist})

def editcoursedetails(request,cid):
    coursedetails = get_object_or_404(courseDetails,id=cid)
    if request.method=='POST':
        coursedetails.courseid = request.POST.get('courseid')
        coursedetails.coursename = request.POST.get('coursename')
        coursedetails.offeredby = request.POST.get('offeredby')
        coursedetails.offeringyear = request.POST.get('offeringyear')
        coursedetails.credits = request.POST.get('credits')

        coursedetails.save()

        return redirect('facultymodule:viewcoursedetails')

    return render(request,'facultymodule/edit.html',{'coursedetails': coursedetails})

def deletecoursedetails(request,cid):
    coursedetails = get_object_or_404(courseDetails, id=cid)
    if request.method == 'POST':
        coursedetails.delete()
        return redirect('facultymodule:viewcoursedetails')

    return render(request, 'facultymodule/delete.html', {'coursedetails': coursedetails})

from studentmodule.models import courseapplication

def courseapplicationlist(request):
    courseapplications = courseapplication.objects.all()
    return render(request, 'facultymodule/courseapplicationlist.html', {'courseapplications': courseapplications})



