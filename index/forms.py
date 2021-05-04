from django import forms
from .models import doctor_reservation
class reservation_form(forms.ModelForm):
        date_reservation1=forms.DateField(widget=forms.DateInput(attrs={'id':'checkin_date'}))
        #time_reservation=forms.TimeField(widget=forms.TimeInput(attrs={'id':'checkin_time'}))
        class Meta:
            model=doctor_reservation
            fields='__all__'
            exclude=['name','email']