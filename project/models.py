from django.db import models

class Faculty(models.Model):
    FId = models.CharField(max_length=3)
    FName = models.CharField(max_length=200)
    FGender = models.CharField(max_length=10)
    FEmail = models.EmailField()
    FDesignation = models.CharField(max_length=150)
    class Meta:
        db_table="Faculty"

# Create your models here.
