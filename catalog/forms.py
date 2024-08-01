from django import forms
from .models import Demographics

class DemographicsForm(forms.ModelForm):
    class Meta:
        model = Demographics
        fields = ['customer_id', 'customer_secondary_email','customer_NUID','customer_grad','customer_affiliation',
                  'is_international_student','is_first_gen', 'customer_class_standing', 'customer_occupation',
                  'customer_transportation', 'customer_living_status', 'customer_transportation', 'customer_employment',
                  'customer_ethnicity', 'customer_age', 'customer_gender_identity', 'customer_marital_status',
                  'has_dependents', 'customer_number_dependents', 'customer_wgec', 'customer_zip_code', 'customer_allergies',
                  'customer_household_size',]