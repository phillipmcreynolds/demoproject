from django import forms

from .models import Booking

class DemoForm(forms.Form):
    menu_name = forms.CharField(widget=forms.Textarea)

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"