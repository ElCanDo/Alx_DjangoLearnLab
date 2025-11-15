from django.urls import path
from . import views

urlpatterns = [ 
    path("", views.home, name="home"),
    path("example_form/", views.ExampleForm, name="example_form"),
]