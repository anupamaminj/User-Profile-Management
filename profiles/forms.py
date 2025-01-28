from django import forms
from .models import UserProfile
import re

class LoginForm(forms.Form):
    mobile_number = forms.CharField(max_length=10, required=True, 
                                    widget=forms.TextInput(attrs={'placeholder': 'Enter Mobile Number'}))

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email', 'pan_card', 'city', 'state', 'occupation', 'gender']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Enter Email'}),
            'pan_card': forms.TextInput(attrs={'placeholder': 'Enter PAN Card'}),
        }

def clean_pan_card(self):
    pan_card = self.cleaned_data.get('pan_card')
    if pan_card and not re.match(r'^[A-Z]{5}\d{4}[A-Z]{1}$', pan_card):
        raise forms.ValidationError('Invalid PAN card format.')
    return pan_card


