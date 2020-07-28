from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('port',views.port,name='port'),

    path('airtel',views.airtel,name='airtel'),
    path('emaildone',views.emaildone,name='emaildone'),









]
