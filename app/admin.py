from django.contrib import admin
from .models import Appointment

# Register your models here.
# def download_csv(self, request, queryset):
#     import csv
#     f = open('Appointments.csv', 'w')
#     writer = csv.writer(f)
#     writer.writerow(["first_name", "last_name", "date", "time", "presciption","status"])
#     for s in queryset:
#         writer.writerow([s.first_name, s.last_name, s.date, s.time, s.presciption, s.status])

class AppointmentAdmin(admin.ModelAdmin):
    fields = ['first_name','last_name','date','time','presciption','status']
    readonly_fields = ['date','time']
    list_display = ['first_name', 'last_name','date','time','status']
    # actions = [download_csv]

admin.site.register(Appointment,AppointmentAdmin)