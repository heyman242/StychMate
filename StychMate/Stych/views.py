from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Tailor, Order
from datetime import date
from django.shortcuts import redirect
from django.contrib.auth import logout
from decimal import Decimal
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required


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


def custom_logout(request):
    logout(request)
    return redirect('login')


@login_required
def tailor_dashboard(request, tailor_id):
    tailor = get_object_or_404(Tailor, pk=tailor_id)
    current_work = Order.objects.filter(assigned_hub__hub_location=tailor.tailor_location, order_status='Pending')

    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        order = get_object_or_404(Order, pk=order_id)
        if order.order_status == 'Pending':
            order.order_status = 'Assigned'

            # Check if the tailor has reached the limit of 10 assigned work per day
            today = date.today().strftime('%Y-%m-%d')
            assigned_work_count = Order.objects.filter(assigned_hub__hub_location=tailor.tailor_location,
                                                       order_status='Assigned',
                                                       assigned_date=today).count()
            if assigned_work_count < 10:
                order.assigned_date = today
                order.save()
            else:
                # Handle the case when the limit is reached
                # You can display an error message or redirect the user to a different page
                return HttpResponse("You have reached the daily limit of assigned work.")

        elif order.order_status == 'Assigned':
            payout = order.sku.sku_price * Decimal(0.16)
            tailor.tailor_payout += payout
            tailor.save()
            order.delete()

    assigned_work = Order.objects.filter(assigned_hub__hub_location=tailor.tailor_location, order_status='Assigned')

    # Limit completed work per day to 10
    today = date.today().strftime('%Y-%m-%d')
    assigned_work_count = Order.objects.filter(assigned_hub__hub_location=tailor.tailor_location,
                                               order_status='Assigned',
                                               assigned_date=today).count()
    remaining_work_count = 10 - assigned_work_count

    context = {
        'tailor': tailor,
        'current_work': current_work,
        'assigned_work': assigned_work,
        'payouts': tailor.tailor_payout,
        'remaining_work_count': remaining_work_count,

    }

    return render(request, 'tailor_dashboard.html', context)
