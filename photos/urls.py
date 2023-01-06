from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register, name = 'register'),
    path('',views.loginPage,name = 'login'),
    path('gallery/', views.gallery, name='gallery'),
    path('photo/<str:pk>/',views.viewPhoto, name = 'photo'),
    path('add/', views.addPhoto, name='add'),
    path('delete/<str:pk>/',views.delete, name='delete'),
    path('logout/',views.logoutPage,name = 'logout'),
    
] 