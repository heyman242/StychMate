from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import Tailor, Order, SKU
from django.contrib.auth.models import User
from django.urls import reverse
import random
from django.utils import timezone
from .models import SKU, Tailor, Hub, Order
from django.db.models import Q


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
                        tailor_location=tailor_location)
        tailor.save()
        tailor.tailor_id = f'T-{tailor.pk:04d}'  # use the primary key of the Tailor object
        tailor.save()

        # redirect to login page
        return redirect('login')
    else:
        return render(request, 'signup.html')


from django.shortcuts import render, get_object_or_404
from .models import Tailor, Order

@login_required
def tailor_dashboard(request, tailor_id):
    tailor = get_object_or_404(Tailor, pk=tailor_id)
    current_work = Order.objects.filter(assigned_hub__hub_location=tailor.tailor_location,
                                        order_status='Pending')

    context = {
        'tailor': tailor,
        'current_work': current_work,
        'payouts': tailor.tailor_payout,
    }

    return render(request, 'tailor_dashboard.html', context)
