from django.db import models

# Create your models here.

class services(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    subtitle = models.CharField(max_length=200, verbose_name="Subtitulo")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(verbose_name="Imagen", upload_to="services")
    created = models.DateField(auto_now_add=True,verbose_name="Fecha de creación")
    updated = models.DateField(auto_now=True, verbose_name="Fecha de actualozación")

    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"
        ordering = ['-created']

    def __str__(self):
        return self.title
    
    