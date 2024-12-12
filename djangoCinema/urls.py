from django.contrib import admin
from django.urls import path, include
from api import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('cinema/', include('cinema.urls')),
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutPage, name='logout'),
    path('login/', views.loginPage, name='login'),
    path('create_ticketUser/', views.create_ticketUser, name='create_ticketUser'),
]
