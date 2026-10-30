"""
URL configuration for Hotel_Booking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hotelapp import views
urlpatterns = [
    path('admin/', admin.site.urls),

    # Hotel URLs
    path('hotels/', views.HotelListCreateView.as_view()),
    path('hotels/<int:pk>/', views.HotelRetrieveUpdateDeleteView.as_view()),

    # Room URLs
    path('rooms/', views.RoomListCreateView.as_view()),
    path('rooms/<int:pk>/', views.RoomRetrieveUpdateDeleteView.as_view()),

    # Customer URLs
    path('customers/', views.CustomerListCreateView.as_view()),
    path('customers/<int:pk>/', views.CustomerRetrieveUpdateDeleteView.as_view()),
    
    # Booking URLs
    path('bookings/', views.BookingListCreateView.as_view()),
    path('bookings/<int:pk>/', views.BookingRetrieveUpdateDeleteView.as_view()),
]
