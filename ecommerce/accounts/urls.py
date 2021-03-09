from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user),
    path('register', views.register_user),
    path('/login', views.logout_user)
]