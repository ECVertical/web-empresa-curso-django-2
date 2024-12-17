from django.urls import path
from . import views 
urlpatterns = [
    # Path core
    path("", views.inicio, name="home"),
    path("historia/", views.historia, name="about"),
    path("tienda/", views.visitanos, name="store"),
   
]
