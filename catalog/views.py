from .models import (Customer, OrdersHeader,Products, Staff)
#, Valueform)
from django.shortcuts import render, reverse, resolve_url
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect


def index(request):
    """View function for home page of site."""
    num_customers = Customer.objects.all().count()

    # num_instances = BookInstance.objects.all().count()
    # Available books (status = 'a')
    # num_instances_available = BookInstance.objects.filter(status__exact='a').count()\
    # The 'all()' is implied by default.
    # num_authors = Author.objects.count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_customers': num_customers,
    #    'num_instances': num_instances,
    #    'num_instances_available': num_instances_available,
    #    'num_authors': num_authors,
        'num_visits': num_visits,
    }
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


from django.views import generic

class OrdersListView(LoginRequiredMixin,generic.ListView):
    model = OrdersHeader
    template_name = 'catalog/order_list.html'
    paginate_by = 10
    #def get_queryset(self):
    #    return OrdersHeader.object.filter \
    #        (borrower=self.request.user).filter(pickup_status = 'n').order_by('order_date')
    #        (borrower=self.request.user).filter(status__exact='o').order_by('order_date')


class OrderCreate(CreateView):
    model = OrdersHeader
    fields = ['customer_id','pickup_location_id','order_date', 'order_fill_or_shop', 'is_bag_required', 'order_diapers','order_parent_supplies']
    def get_success_url(self):
        return reverse('order_list')  # redirects customer to page after commiting change
    # should have this redirect to order details to continue entries

class OrderUpdate(UpdateView):
    model = OrdersHeader
    fields = ['customer_id','pickup_location_id','order_date', 'order_fill_or_shop', 'is_bag_required', 'order_diapers','order_parent_supplies']
    def get_success_url(self):
        return reverse('order_list') # redirects customer to page after commiting change
    # should have this redirect to order details to continue entries


# mjl 7/31/2024 adding staff and product entry views


class ProductsUpdate(UpdateView):
    model = Products
    fields = ['product_name', 'product_description', 'product_availability','product_quantity']
    def get_success_url(self):
        return reverse('order_list') # redirects customer to page after commiting change

class ProductsCreate(CreateView):
    model = Products
    fields = ['product_name', 'product_description', 'product_availability','product_quantity']
    def get_success_url(self):
        return reverse('order_list')  # redirects customer to page after commiting change

class ProductsListView(LoginRequiredMixin,generic.ListView):
    model = Products
    template_name = 'catalog/products_list.html'
    paginate_by = 10


class StaffUpdate(UpdateView):
    model = Staff
    fields = ['staff_first_name', 'staff_last_name', 'staff_position']
    def get_success_url(self):
        return reverse('order_list')  # redirects customer to page after commiting change

class StaffCreate(CreateView):
    model = Staff
    fields = ['staff_first_name', 'staff_last_name', 'staff_position']
    def get_success_url(self):
        return reverse('order_list')  # redirects customer to page after commiting change

class StaffListView(LoginRequiredMixin,generic.ListView):
    model = Staff
    template_name = 'catalog/staff_list.html'
    paginate_by = 10

# mjl 7/30/2024 trying to allow customer to be chosen during order entry
# https://www.educba.com/django-foreign-key/
# def order_view(request):
#     form = Valueform(request.POST or None)  # see models.py for Valueform def
#     if form.is_valid():
#         post = form.save()
#         post.Creator = request.user
#         print('Creator user stored',request.user)
#         post.save()
#     return  render(request,'ordersheader_form.html', {"form": form})
# def order_edit(request):
#     form = Valueform(request.POST or None)
#     if form.is_valid():
#         post = form.save()
#         post.Creator = request.user
#         print('Creator user updated',request.user)
#         post.save()
#     return  render(request,'ordersheader_form_edit.html', {"form": form})
# def order_update(request):
#     form = Valueform(request.POST or None)
#     if form.is_valid():
#         post = form.save()
#         post.Creator = request.user
#         print('Creator user updated',request.user)
#         post.save()
#     return  render(request,'ordersheader_form_edit.html', {"form": form})

@login_required
def profile(request):
    user = request.user  # Get the current logged-in user
    return render(request, 'catalog/profile.html', {'user': user})
# mjl 7/31/2024 adding delete features for staff and products
def staff_delete(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    try:
        staff.delete()
        messages.success(request, (staff.staff_first_name + ' ' +
                                   staff.staff_last_name +" has been deleted"))
    except:
        messages.success(request, (staff.staff_first_name + ' ' + staff.staff_last_name + ' cannot be deleted.'))
    return redirect('order_list')

def products_delete(request, pk):
    staff = get_object_or_404(Products, pk=pk)
    try:
        products.delete()
        messages.success(request, (Products.product_name +" has been deleted"))
    except:
        messages.success(request, (Products.product_name + ' cannot be deleted.'))
    return redirect('order_list')
