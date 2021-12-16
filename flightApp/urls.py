from django.urls import path
from . import views

urlpatterns = [
    path('passdtl/', views.passenger_list, name= 'pass_list'),
    path('passdtl/<int:id>', views.passenger_details,name= 'pass_details'),
]