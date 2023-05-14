from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.tailor_dashboard, name='tailor_dashboard'),
    path('logout/', views.logout_view, name='logout'),
]
