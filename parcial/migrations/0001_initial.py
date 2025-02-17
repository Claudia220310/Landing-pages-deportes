# Generated by Django 5.0.6 on 2024-05-31 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagenes')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Titulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagenHeader', models.ImageField(blank=True, null=True, upload_to='imagenes')),
                ('msj', models.CharField(max_length=200)),
                ('subtitulo', models.CharField(max_length=300)),
            ],
        ),
    ]
