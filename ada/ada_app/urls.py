from django.urls import path
from ada_app import views

urlpatterns = [
        path('', views.profile, name='profile'),
        path('register/', views.register, name='register')
]
