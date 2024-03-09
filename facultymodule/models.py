from django.db import models
class courseDetails(models.Model):
    courseid=models.CharField(max_length=10)
    coursename=models.CharField(max_length=255)
    OFFEREDBY=[
        ('CSE', 'CSE'),
        ('ECE', 'ECE'),
        ('AIDS', 'AIDS'),
        ('CSIT', 'CSIT'),
        ('BIO-TECH', 'BIO-TECH'),
    ]
    offeredby=models.CharField(max_length=20,choices=OFFEREDBY)
    offeringyear=models.CharField(max_length=225)
    credits=models.CharField(max_length=225)

    def __str__(self):
        return self.courseid
# Create your models here.
