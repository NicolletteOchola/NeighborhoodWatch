from django import forms
from .models import Profile, Business, Profile

class NewBusinessForm(forms.Form):
  class Meta:
    model = Business
    exclude = ['bs_user','bs_location']

class NewPostForm(forms.ModelForm):
  class Meta:
     model = Profile
     exclude = ['bs_user','bs_location']

class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    exclude = ['user']