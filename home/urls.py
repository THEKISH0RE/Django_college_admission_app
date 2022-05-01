
from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('form/', views.form, name='form'),
    path('form/final/', views.final, name='final'),
]