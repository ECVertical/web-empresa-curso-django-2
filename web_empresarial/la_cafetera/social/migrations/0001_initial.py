# Generated by Django 5.1.1 on 2024-10-23 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Link",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "key",
                    models.SlugField(
                        max_length=100, unique=True, verbose_name="Nombre Clave"
                    ),
                ),
                ("name", models.CharField(max_length=200, verbose_name="Red social")),
                ("url", models.URLField(blank=True, null=True, verbose_name="Enlace")),
                (
                    "created",
                    models.DateField(
                        auto_now_add=True, verbose_name="Fecha de Creacion"
                    ),
                ),
                (
                    "update",
                    models.DateField(
                        auto_now=True, verbose_name="Fecha de actualizacion"
                    ),
                ),
            ],
            options={
                "verbose_name": "Enlace",
                "verbose_name_plural": "Enlaces",
                "ordering": ["name"],
            },
        ),
    ]
