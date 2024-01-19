from django import forms
from app.models import *

class userForm(forms.ModelForm):
    class Meta():
        model=User
        fields=['username','email','password']
        widgets={'password':forms.PasswordInput}
        help_texts={'username':''}
class ProfileForm(forms.ModelForm):
    class Meta():
        model=Profile
        fields=['address','profile_pic']
        widgets={'address':forms.Textarea(attrs={'cols':23,'rows':5})}
