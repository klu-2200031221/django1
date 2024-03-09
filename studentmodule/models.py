from django.db import models

# Create your models here.
class Applicant(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=10)
    address = models.TextField()
    tenthmarks = models.CharField(max_length=10)
    twelfthmarks = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

from facultymodule.models import courseDetails
class courseapplication(models.Model):
    coursedetails = models.ForeignKey(courseDetails, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    certificate = models.FileField(upload_to='certificate/')

    def __str__(self):
        return f"{self.name} - {self.coursedetails}"  # Adjust this line as needed
