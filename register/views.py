from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.models import User, Group





# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            form.save()
            # get the new user info and set the group for this user to LibraryMember
            user = User.objects.get(username=uname)
            # mjl 7/29/2024  updated from LibraryrMember to prototypes Customer group for default security
            # this registration attempt was otherwise throwing an error as user group LibraryMember did not exist
            lib_group = Group.objects.get(name='Customer')
            user.groups.add(lib_group)
            user.save()
            return redirect('login')

        return redirect("index")
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})

def orders(request):
    packing_orders = Order.objects.filter(status=Order.PACKING)
    current_orders = Order.objects.filter(status=Order.PICKUP)
    old_orders = Order.objects.filter(status=Order.RETURNS)

    context = {
        'packing_orders': packing_orders,
        'current_orders': current_orders,
        'old_orders': old_orders,
    }

    return render(request, 'orders.html', context)