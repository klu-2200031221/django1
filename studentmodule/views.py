from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *
def viewcourse(request):
    return render(request,'studentmodule/viewcourse.html')

from facultymodule.models import courseDetails
def coursedetails(request):
    coursedetailslist = courseDetails.objects.all()
    return render(request,'studentmodule/viewcourse.html',{'coursedetailslist': coursedetailslist})
# Create your views here.

def addstudentprofile(request):
    return render(request,'studentmodule/profile.html')

def submit_form(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname', '')
        lastname = request.POST.get('lastname', '')
        phonenumber = request.POST.get('phonenumber', '')
        address = request.POST.get('address', '')
        tenthmarks = request.POST.get('tenthmarks', '')
        twelfthmarks = request.POST.get('twelfthmarks', '')

        # Check if all required fields are present
        if firstname and lastname and phonenumber and address and tenthmarks and twelfthmarks:
            applicant = Applicant(firstname=firstname,
                                  lastname=lastname,
                                  phonenumber=phonenumber,
                                  address=address,
                                  tenthmarks=tenthmarks,
                                  twelfthmarks=twelfthmarks)
            applicant.save()
            return render(request, 'studenthomepage.html')

    return render(request, 'studenthomepage.html')

from django.shortcuts import render,redirect
from .forms import *
from django.core.mail import send_mail
def applycourse(request,cid):
    coursedetails=get_object_or_404(courseDetails,id=cid)
    if request.method=='POST':
        form=courseapplicationform(request.POST, request.FILES)
        if form.is_valid():
            courseapplication = form.save(commit=False)
            courseapplication.coursedetails = coursedetails
            courseapplication.save()

            subject = 'Course Details Received'
            message = 'Thank You for registering. Your application is received and will be sent to next process'
            from_email='sanjana031103@gmail.com'
            recipient_list = [courseapplication.email]
            send_mail(subject,message,from_email,recipient_list)
        return redirect('studentmodule:coursedetails')
    else:
        form=courseapplicationform()
    return render(request,'studentmodule/applycourse.html',{'coursedetails':coursedetails, 'form': form})
