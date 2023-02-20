from django.db import models


# creamos los models 


class Libro(models.Model):
    titulo=models.CharField(max_length=40)
    autorLib=models.CharField(max_length=40)
    autor=models.CharField(max_length=40)
    año=models.IntegerField()
    puntaje=models.IntegerField()
    reseña=models.CharField(max_length=300)
    
class Novedad(models.Model):
    
    titulo=models.CharField(max_length=40)
    año=models.IntegerField()
    imagen=models.ImageField(upload_to = 'novedades', null=True)
    
#por defecto Django tiene campos de usuario