from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Departamento(models.Model):
	Nombre = models.CharField(max_length = 30)

	def __unicode__(self):
		return self.Nombre


class Ciudade(models.Model):
	ID_Departamento = models.ForeignKey(Departamento)
	Nombre = models.CharField(max_length = 30 )

	def __unicode__(self):
		return self.Nombre


class Casa(models.Model):
	Nombre = models.CharField(max_length = 30)
	Direccion = models.CharField(max_length = 30)
	ID_Ciudad = models.ForeignKey(Ciudade)
	def __unicode__(self):
		return self.Nombre


class Marca(models.Model):
	Nombre = models.CharField(max_length = 30)
	ID_Casa = models.ForeignKey(Casa)

	def __unicode__(self):
		return self.Nombre


class Modelo(models.Model):
	Nombre = models.CharField(max_length = 30)
	ID_Marca = models.ForeignKey(Marca)

	def __unicode__(self):
		return self.Nombre


class Tipo_Persona(models.Model):
	Nombre = models.CharField(max_length = 30)
	Descripcion = models.CharField(max_length =50)

	def __unicode__(self):
		return self.Nombre

class Persona(models.Model):
	ID_Persona = models.CharField(max_length = 15, primary_key = True)
	Nombre = models.CharField(max_length = 30)
	Apellido = models.CharField(max_length = 30)
	Direccion = models.CharField(max_length = 30)

	def __unicode__(self):
		return self.ID_Persona

class Civile(models.Model):
	ID_Persona = models.ForeignKey(Persona)
	ID_Ciudad = models.ForeignKey(Ciudade)
	ID_Tipo_Persona = models.ForeignKey(Tipo_Persona)

	def __unicode__(self):
		return self.ID_Persona.Nombre


class Infracciones(models.Model):
	Articulo = models.CharField(max_length = 120)
	Costo = models.IntegerField()
	
	

	def __unicode__(self):
		return self.Articulo


class Vehiculo(models.Model):
	ID_vehiculo = models.CharField(max_length = 7 , primary_key = True)
	ID_Persona = models.ForeignKey(Persona)
	ID_Modelo = models.ForeignKey(Modelo)
	Fecha_Matriculacion = models.DateTimeField(auto_now_add = True, null = True )

	def __unicode__(self):
			return self.ID_vehiculo


class Pago(models.Model):
	Estado = models.CharField(max_length = 30,)

	def __unicode__(self):
		return self.Estado


class Multa(models.Model):
	Lugar = models.CharField(max_length = 30)
	ID_Persona = models.ForeignKey(Persona)
	ID_Agente = models.ForeignKey(Civile)
	ID_vehicuo = models.ForeignKey(Vehiculo)
	Fecha = models.DateTimeField(auto_now_add = True, null = True )
	ID_Infracciones = models.ForeignKey(Infracciones)
	ID_Pago  = models.ForeignKey(Pago)
	

	def __unicode__(self):
		return self.Lugar




