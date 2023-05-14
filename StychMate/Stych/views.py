from ipaddress import summarize_address_range
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Tailor, Order, Order_Item, SKU

@login_required
def tailor_dashboard(request, tailor_id):
    tailor = Tailor.objects.get(id=tailor_id)
    current_work = Order_Item.objects.filter(tailor=tailor, order__status='In progress')
    #payouts = Order_Item.objects.filter(tailor=tailor, order__status='Delivered').aggregate(Sum('sku__price'))['sku__price__sum']
    context = {
        'tailor': tailor,
        'current_work': current_work,
       # 'payouts': payouts,
    }
    return render(request, 'tailor_dashboard.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            tailor = Tailor.objects.get(user=user)
            return redirect('tailor_dashboard', tailor_id=tailor.id)
        else:
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')
    
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Tailor

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # create new user
            user = form.save()
            # create new Tailor object
            tailor = Tailor.objects.create(user=user,
                                            tailor_name=form.cleaned_data['tailor_name'],
                                            tailor_location=form.cleaned_data['tailor_location'],
                                            tailor_availability=form.cleaned_data['tailor_availability'],
                                            tailor_payout=form.cleaned_data['tailor_payout'])
            # redirect to login page
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login_view')
