from django.urls import path
from . import views 
urlpatterns = [
    # Path  contact
    path("", views.contacto, name="contact"),

]