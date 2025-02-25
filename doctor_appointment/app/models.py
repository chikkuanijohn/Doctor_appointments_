from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Doctor(models.Model):
    pid=models.TextField()
    name = models.TextField()
    specialty = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    available_day = models.CharField(max_length=100)  
    available_time_start = models.TimeField()
    available_time_end = models.TimeField()
    



class Patient(models.Model):
    Patient_name = models.CharField(max_length=100)
    age  = models.PositiveIntegerField()
    contact_number = models.CharField(max_length=15)




class Appointment(models.Model):
    Name = models.TextField()
    age = models.PositiveIntegerField()
    Appointmentdate = models.CharField(max_length=100)
    Reasonforappointment = models.TextField(max_length=100)
 
    email =models.EmailField() 
    doctor_name = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.appointment_date} with {self.doctor_name}"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()


