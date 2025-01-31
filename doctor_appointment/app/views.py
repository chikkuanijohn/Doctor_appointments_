from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import *
import os
from django.contrib.auth.models import User
from django.conf import settings
from .models import Patient
from django.core.mail import send_mail
from .models import Doctor, Appointment 
from .models import Appointment 
from .forms import ContactForm
# Create your views here.

def doctor_appointment_login(req):
        if 'admin' in req.session:
            return redirect(admin_home)
        if 'user' in req.session:
            return redirect(user_home)
        if req.method=='POST':
            uname=req.POST['uname']
            password=req.POST['password']
            data=authenticate(username=uname,password=password)
            if data:
                login(req,data)
                if data.is_superuser:
        
                    req.session['admin']=uname 
                    return redirect(admin_home)
                else:
                    req.session['user']=uname 
                    return redirect(user_home)
            else:
                messages.warning(req,'invalid username or password')
                return redirect(doctor_appointment_login)  
        else:
            return render(req,'login.html')

def doctor_appointment_logout(req):
    logout(req)
    req.session.flush() 
    return redirect(doctor_appointment_login)
#--------------------admin----------------------
def admin_home(req):
    
    if 'admin' in req.session:
        data=Doctor.objects.all()
    
        return render(req,'admin/home.html',{'Doctor':data})
    else:
       return redirect(doctor_appointment_login)
    
    
def user_home(req):
     if 'user' in req.session:
         data=Doctor.objects.all()
         return render(req,'user/user_home.html',{'Doctor':data})
     else:
          return redirect(doctor_appointment_login)
    
    
       





def register(req):
    if req.method=='POST':
        uname=req.POST['uname']
        email=req.POST['email']
        pswd=req.POST['pswd']
        print(uname,email,pswd)
        try:
            data=User.objects.create_user(first_name=uname,email=email,username=email,password=pswd)
            data.save()
        except:
            messages.warning(req,'invalid username or password')
            return redirect(register)   
        return redirect(doctor_appointment_login) 
    else:
        return render(req,'user/register.html') 
    


def booking(request):
        return render(request,'booking') 
   
def book_appointment(request):
            if request.method=='POST':
                Name=request.POST['name']
                age=request.POST['age']
                Appointmentdate=request.POST['appointmentdate']
                Reasonforappointment=request.POST['reasonforappointment']
                email=request.POST['email']
                data = Appointment(Name=Name,age=age, Appointmentdate=Appointmentdate,Reasonforappointment=Reasonforappointment,email=email)
                data.save()
                return redirect(book_appointment)
            patient=Patient.objects.all()
             
            return render(request,'user/book_appointment.html',{'book_appointment':patient})




# def booking_appointment(request):
#     if request.method == "POST":
#         Name = request.POST.get("name")
#         email = request.POST.get("email")
#         Appointment_date = request.POST.get("appointment_date")
#         Reasonforappointment = request.POST.get("reasonforappointment")
#         token_number = generate_token_number()  
        
            # Send email to the doctor
            # send_mail(
            #     'Appointment Booking Confirmation',
            #     f'Hello Doctor,\n\nAn appointment has been booked successfully.\n\n'
            #     f'Details:\n'
            #     f'Patient Name: {Name}\n'
            #     f'Appointment Date: {Appointment_date}\n'
            #     f' reasonforappointment: {Reasonforappointment}\n'
            #     f'Token Number: {token_number}\n\n'
            #     f'Please be prepared to attend to the patient at the scheduled time.',
            #     'chikkuanijohn1@gmail.com',  # Replace with your email
            #     [email],
            #     fail_silently=False,
            # )
            
            # Send confirmation to the user
    #         messages.success(request, "Appointment booked successfully! The details have been sent to the doctor.")
    #         return redirect('appointment_success')  
    #     else:
    #         messages.error(request, "Please fill all the required fields.")
    #         return redirect('book_appointment') 

    # return render(request, 'book_appointment.html')

# def generate_token_number():
#     """
#     Function to generate a unique token number for the appointment.
#     You can customize this to use more sophisticated logic.
#     """
#     now = appointment_date.now()
#     return f"TOK{now.strftime('%Y%m%d%H%M%S')}"


 
def Contact(request):
    return render(request,'Contact.html')


def check_up_packages(request):
    return render(request,'check_up_packages.html')

def Our_specialities(request):
    return render(request,'Our_specialities.html')

def About(request):
    return render(request,'About.html')

def Testimonals(request):
    return render(request,'Testimonals.html')

def booking(request):
    return render(request,'booking.html')




def view_bookings(request):
    if request.method =='POST':
         Name=request.POST['name']
         age=request.POST['age']
         Appointmentdate=request.POST['appointmentdate']
         Reasonforappointment=request.POST['reasonforappointment']
         email=request.POST['email']

         if Name and age and Appointmentdate and Reasonforappointment and email:
             data = Appointment(Name=Name,age=age, Appointmentdate=Appointmentdate,Reasonforappointment=Reasonforappointment,email=email)
             data.save()
             return redirect('admin_home')
    patient=Patient.objects.all()
    return render(request,'admin/view_bookings.html', {'patient': patient})


        
             


    
   
def view_doc(request):
    return render(request,'view_doc.html')


def add_details(req):

    if 'admin' in req.session:
        if req.method == 'POST':
           
            name = req.POST['name']
            specialty = req.POST['specialty']
             
            available_days = req.POST['available_days']
            available_time_start = req.POST['available_time_start']
            available_time_end= req.POST['available_time_end']
            # file = req.FILES['img']

            data = Doctor.objects.create(
                 name=name, specialty=specialty,  available_days= available_days,
                available_time_start=available_time_start,available_time_end=available_time_end)
               
            data.save()
            return redirect(admin_home)
        else:
            return render(req, 'admin/add_details.html')
    else:
        return redirect(doctor_appointment_login)
    

def edit_details(req, pid):
    if 'admin' in req.session:
        if req.method == 'POST':
            name = req.POST['name']
            specialty = req.POST['specialty']
            available_days = req.POST['available_days']
            available_time_start = req.POST['available_time_start']
            available_time_end = req.POST['available_time_end']
            # file = req.FILES.get('img')  
            # if file:
            #     Doctor.objects.filter(pk=pid).update(name=name,specialty=specialty,available_days=available_days, available_time_start= available_time_start,available_time_end =available_time_end)
            #     data=Doctor.objects.get(pk=pid)
            #     data.img=file
            #     data.save()
            # else:  
            Doctor.objects.filter(pk=pid).update(name=name,specialty=specialty,available_days=available_days, available_time_start= available_time_start,available_time_end =available_time_end)
            data=Doctor.objects.get(pk=pid)
            data.save()
            return redirect(admin_home)
        else:
            data=Doctor.objects.get(pk=pid)
            return render(req,'admin/edit.html',{'data':data})

def delete_details(req,pid):
    data=Doctor.objects.get(pk=pid)
    # file=data.img.url
    # file=file.split('/')[-1]
    # os.remove('media/'+file)
    data.delete()
    return redirect(admin_home)






def book_appointment(request):
    if request.method == 'POST':
        Name = request.POST['name']
        age = request.POST['age']
        Appointmentdate = request.POST['appointmentdate']
        Reasonforappointment = request.POST['reasonforappointment']
        email = request.POST['email']
        
        data = Appointment(Name=Name, age=age, Appointmentdate=Appointmentdate, Reasonforappointment=Reasonforappointment, email=email)
       
        
      
        messages.success(request, '')
        
        return redirect('success')  
    patient = Appointment.objects.all()  
    return render(request, 'user/book_appointment.html', {'book_appointment': patient})


def success(request):
    return render(request, 'success.html')




def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return render(request, 'contact.html', {'form': form, 'message': 'Your message has been sent successfully!'})
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})