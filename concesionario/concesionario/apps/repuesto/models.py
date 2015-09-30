from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

#ATRIBUTOS DE REPUESTO		
#id_repuesto				
#Nombre
#Precio
#Marca
#Clasificación
#Unidad
#Imagen	
#Provedor
#Descripción

#Define la organizacion del los datos de un repuesto en la base de datos
class Repuesto(models.Model):
#Django por defecto, cuando los modelos no tienen primary_key, coloca una llamada "id"

#Nombre del repuesto
nombre = models.CharField(null=True,blank=True,max_length=20)
#precio del repuesto
precio =  FloatField(max_digits=32,decimal_places=2)
#marca del repuesto
marca = models.CharField(null=True,blank=True,max_length=20) 
#categorias de repuesto
AUTOMOTRIZ = 'Automotriz'
FERRETERIA= 'Ferreteria'
PINTURAS='Pinturas'
RODAMIENTOS='Rodamientos'
SOLVENTES='Solventes'
BANDAS_CADENAS='Bandas_cadenas'
LIMPIEZA='Limpieza'
AUTOPARTES='Autopartes'
SELLOS_EMPAQUES='Sellos_empaques'

	tipo_choice = (
		(AUTOMOTRIZ, 'Automotriz'),
		(FERRETERIA, 'Ferreteria'),
		(PINTURAS, 'Pinturas'),
		(RODAMIENTOS, 'Rodamientos'),
		(SOLVENTES, 'Solventes'),
		(BANDAS_CADENAS, 'Bandas_cadenas'),
		(LIMPIEZA, 'Limpieza'),
		(AUTOPARTES, 'Autopartes'),
		(SELLOS_EMPAQUES, 'Sellos_empaques'),
	 )
	 
Clasificacion = models.CharField(max_length=20, choices=tipo_choice,default=SELLOS_EMPAQUES)

#Cantidad disponible de repuesto
unidad =  FloatField(max_digits=3,decimal_places=2)
#Imagen del repuesto
imagen = models.ImageField(null=True,blank=True,upload_to = "imagenes/repuestos/")
	#Thumbnail que permite reducir la imagen del empleado 
	thumbnail = ImageSpecField(source='imagen',
									  processors=[ResizeToFill(100, 50)],
									  format='JPEG',
									  options={'quality': 60})

#Provedor del repuesto
provedor = models.CharField(null=True,blank=True,max_length=20)
#Descripción del repuesto
descripcion = models.CharField(null=True,blank=True,max_length=100)

#Permite hacer modificaciones agregadas a la representacion del modelo 
	class Meta:
		ordering = ['nombre']
		verbose_name_plural = "Repuestos"

	#Permite determinar una representacion en string del objeto repuesto
	def __str__(self):
		return self.nombre

	#Permite determinar una represetacion en string para el objeto (Esto es para versiones de Python 2)
	def __unicode__(self):
		return self.nombre 

