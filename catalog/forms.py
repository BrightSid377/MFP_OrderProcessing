from django import forms
from .models import Demographics, Profile
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

def validate_age(value):
    try:
        age = int(value)
    except ValueError:
        raise ValidationError('Age must be a valid integer.')

    if not (0 <= age <= 120):
        raise ValidationError('Age must be between 0 and 120.')

def validate_NUID(value):
    if not value.isdigit() or len(value) != 8:  # Adjust length as per your requirement
        raise ValidationError('NUID must be a 8-digit number.')

def validate_zip_code(value):
    import re
    if not re.match(r'^\d{5}(-\d{4})?$', value):
        raise ValidationError('Enter a valid ZIP code.')
class DemographicsForm(forms.ModelForm):
    class Meta:
        model = Demographics
        fields = ['user_id', 'user_secondary_email','user_NUID','user_grad','user_affiliation',
                  'is_international_student','is_first_gen', 'user_class_standing',
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

        self.fields['user_age'].validators.append(validate_age)
        self.fields['user_NUID'].validators.append(validate_NUID)
        self.fields['user_zip_code'].validators.append(validate_zip_code)
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'image', 'private']