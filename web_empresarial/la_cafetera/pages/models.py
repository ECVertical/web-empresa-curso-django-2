from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.

class Page(models.Model):
    title = models.CharField(verbose_name="Titulo", max_length=200)
    content =CKEditor5Field(verbose_name="Contenido", config_name='extends')
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateField(auto_now_add=True, verbose_name="Fecha de Creacion") 
    update = models.DateField(auto_now=True, verbose_name="Fecha de actualizacion")

    class Meta:
        verbose_name = "pagina"
        verbose_name_plural = "paginas"
        ordering = ["order", "title"]

    def __str__(self):
        return self.title
