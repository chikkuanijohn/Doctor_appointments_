from django.contrib import admin
from .models import Appointment
from.models import *
# Register your models here.
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Contact)
