from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ["first_name","last_name","phone_number","date","time"]
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'e.g., Max'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'e.g., Pratt'}),
            'phone_number':forms.TextInput(attrs={'class':'form-control','placeholder':'e.g., 7643154765'}),
            'date':forms.TextInput(attrs={'class':'form-control','placeholder':'Date'}),
            'time':forms.TextInput(attrs={'class':'form-control','placeholder':'Time'}),
        }