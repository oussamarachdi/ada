from django.urls import path, include
from ada_app import views 

urlpatterns = [
        path('', views.index, name='index'),
        path('register/', views.register, name='register')
]