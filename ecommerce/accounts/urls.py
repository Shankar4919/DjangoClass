from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user),
    path('', views.register_user),
    path('', views.logout_user)
]