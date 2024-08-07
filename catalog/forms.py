from django import forms
from .models import Demographics, Profile
from django.contrib.auth.models import User

class DemographicsForm(forms.ModelForm):
    class Meta:
        model = Demographics
        fields = ['user_id', 'user_secondary_email','user_NUID','user_grad','user_affiliation',
                  'is_international_student','is_first_gen', 'user_class_standing', 'user_occupation',
                  'user_transportation', 'user_living_status', 'user_transportation', 'user_employment',
                  'user_ethnicity', 'user_age', 'user_gender_identity', 'user_marital_status',
                  'has_dependents', 'user_number_dependents', 'user_wgec', 'user_zip_code', 'user_allergies',
                  'user_household_size',]
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(DemographicsForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['user_id'].initial = user.id
            self.fields['user_id'].widget = forms.HiddenInput()

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'image', 'private']