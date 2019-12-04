from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about.html', views.about, name="about"),
    path('location', views.location, name="location"),
    #path('form_submission', views.form_submission, name="form_submission"),
    #path('register', views.register, name="register"),
]