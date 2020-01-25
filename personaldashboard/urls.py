from django.urls import path
from . import views

urlpatterns = [
    path('details', views.details, name = "details"),
    path('dashboard', views.dashboard, name = "dashboard"),
    path('remove', views.remove, name = "remove"),
    path('startdiet', views.startdiet, name = "startdiet"),
    path('bathroom', views.bathroom, name = "bathroom"),
    path('disposables', views.disposables, name = "disposables")
 ]
