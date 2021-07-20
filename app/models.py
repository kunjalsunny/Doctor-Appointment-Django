from django.db import models

# Create your models here.

STATUS_CHOICES=(
    ('Pending','Pending'),
    ('Completed','Completed'))

class Appointment(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=12,null=False)
    date=models.DateField(null=True)
    time=models.TimeField(default="10:00")
    presciption = models.TextField(max_length=100,default="Write here")
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default="Pending")

    def __str__(self):
        return self.first_name + self.last_name 