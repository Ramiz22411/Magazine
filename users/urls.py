from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('users_cart/', views.users_cart, name='users_cart'),
    path('logout/', views.logout_user, name='logout'),
]
