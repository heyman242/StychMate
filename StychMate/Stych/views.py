from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import Tailor, Order, Order_Item, SKU
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            tailor = Tailor.objects.get(user=user)
            tailor_id = int(request.user.tailor.tailor_id[2:])
            tailor_dashboard_url = reverse('tailor_dashboard', args=[tailor_id])
            

            return redirect(tailor_dashboard_url)
        else:
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        tailor_name = request.POST.get('tailor_name')
        tailor_location = request.POST.get('tailor_location')
        tailor_availability = request.POST.get('tailor_availability')
        tailor_payout = request.POST.get('tailor_payout')

        # check if passwords match
        if password1 != password2:
            return render(request, 'signup.html', {'error': 'Passwords do not match.'})

        # create user instance
        user = User.objects.create_user(username=username, password=password1)
        user.is_tailor = True
        user.save()

        # create tailor instance
        tailor = Tailor(user=user,
                        tailor_name=tailor_name,
                        tailor_location=tailor_location,
                        tailor_availability=tailor_availability,
                        tailor_payout=tailor_payout)
        tailor.save()
        tailor.tailor_id = f'T-{tailor.pk:04d}'  # use the primary key of the Tailor object
        tailor.save()

        # redirect to login page
        return redirect('login')
    else:
        return render(request, 'signup.html')


@login_required
def tailor_dashboard(request, tailor_id):
    tailor = Tailor.objects.get(pk=tailor_id)
    context = {
        'tailor_id': tailor_id,
    }
    return render(request, 'tailor_dashboard.html', context)

