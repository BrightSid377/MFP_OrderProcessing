from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
from catalog.models import Demographics, Customer

class DemographicsMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            try:
                # get the customer information associated with the logged-in user
                customer = User.objects.get(id=request.user.pk)
                # check to see if the authenticated customer has filled out their demographics information
                if Demographics.objects.filter(customer_id=request.user.pk).exists():
                    # Avoid redirect loop by excluding the demographics and logout paths
                    if request.path not in [reverse('demographics_form'), reverse('logout')]:
                        return redirect('demographics_form')
            except Customer.DoesNotExist:
                # return redirect('register/')
                pass