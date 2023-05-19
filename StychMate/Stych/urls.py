from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('tailor_dashboard/<int:tailor_id>/', views.tailor_dashboard, name='tailor_dashboard'),
    path('logout/', views.custom_logout, name='logout'),
]
