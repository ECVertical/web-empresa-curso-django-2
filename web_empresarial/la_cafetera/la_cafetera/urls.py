"""
URL configuration for la_cafetera project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    # Path core
    path("", include('core.urls')),
    # Path services
    path("servicios/", include('services.urls')),
    # Path blog
    path("blog/", include('blog.urls')), 
    # Path pages
    path("page/", include('pages.urls')), 
    # Path contact
    path("contacto/", include('contact.urls')),
    # django-ckeditor-5
    path("ckeditor5/", include("django_ckeditor_5.urls")),
    # Path admin
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    

# Custom titles for admin
admin.site.site_title = "Admin La Cafetera"  # Título en la pestaña del navegador
admin.site.site_header = "Admin La Cafetera"  # Título en la parte superior de la página
admin.site.index_title = "Administrador de la Cafetera"  # Título de la pantalla principal