from django.db import models

class Titulo(models.Model):
    imagenHeader = models.ImageField(upload_to='imagenes', null=True, blank=True)
    msj = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=300)
    
    def __str__(self):
        return self.msj + ' - ' + self.subtitulo

class Deporte(models.Model):
    imagen = models.ImageField(upload_to='imagenes', null=True, blank=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=300)
    
    def __str__(self):
        return self.nombre + ' - ' + self.descripcion

class Galeria(models.Model):
    imagen1 = models.ImageField(upload_to='imagenes', null=True, blank=True)
    imagen2 = models.ImageField(upload_to='imagenes', null=True, blank=True)
    imagen3 = models.ImageField(upload_to='imagenes', null=True, blank=True)
    imagen4 = models.ImageField(upload_to='imagenes', null=True, blank=True)
    
    def __str__(self):
        return "Galería con id: " + str(self.id)

class Contenido(models.Model):
    imagenE3 = models.ImageField(upload_to='imagenes', null=True, blank=True)
    tituloE3 = models.CharField(max_length=200)
    paisE3 = models.CharField(max_length=200)
    descripcionE3 = models.CharField(max_length=300)

    def __str__(self):
        return (
            f"Imagen E3: {self.imagenE3}\n"
            f"Titulo E3: {self.tituloE3}\n"
            f"Pais E3: {self.paisE3}\n"
            f"Descripcion E3: {self.descripcionE3}"
        )

