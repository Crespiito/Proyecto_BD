from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Departamento(models.Model):
	Nombre = models.CharField(max_length = 30 )

	def __unicode__(self):
		return self.Nombre


class Ciudade(models.Model):
	Departamento = models.ForeignKey(Departamento)
	Nombre = models.CharField(max_length = 30 )

	def __unicode__(self):
		return self.Nombre


class Casa(models.Model):
	Nombre = models.CharField(max_length = 30)
	Direccion = models.CharField(max_length = 30)

	def __unicode__(self):
		return self.Nombre


class Marca(models.Model):
	ID_Marca = models.CharField(primary_key = True , max_length = 15)
	Nombre = models.CharField(max_length = 30)
	Casa = models.ForeignKey(Casa)

	def __unicode__(self):
		return self.Nombre


class Modelo(models.Model):
	ID_Modelo = models.CharField(primary_key = True, max_length = 15)
	Nombre = models.CharField(max_length = 30)
	Marca = models.ForeignKey(Marca)

	def __unicode__(self):
		return self.Nombre


class Tipo_Persona (models.Model):
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
		return self.Nombre

class Civile(models.Model):
	ID_Persona = models.ForeignKey(Persona)
	Ciudad = models.ForeignKey(Ciudade)
	Tipo_Persona = models.ForeignKey(Tipo_Persona)

	def __unicode__(self):
		return self.ID_Persona.Nombre


class Infracciones(models.Model):
	ID_Infracciones = models.CharField(primary_key=True, max_length = 15)
	Persona = models.ForeignKey(Civile)
	Lugar = models.CharField(max_length = 30)
	Articulo = models.CharField(max_length = 120)
	Costo = models.IntegerField()

	def __unicode__(self):
		return self.Lugar


class Vehiculo(models.Model):
	ID_vehicuo = models.CharField(max_length = 7 , primary_key = True)
	Persona = models.ForeignKey(Persona)
	Modelo = models.ForeignKey(Modelo)
	Fecha_Matriculacion = models.DateTimeField(auto_now = False , auto_now_add = False)

	def __unicode__(self):
			return self.ID_vehicuo



class Multa(models.Model):
	Persona = models.ForeignKey(Civile)
	vehicuo = models.ForeignKey(Vehiculo)
	Fecha = models.DateTimeField(auto_now = False , auto_now_add = False)
	Infracciones = models.ForeignKey(Infracciones)

	def __unicode__(self):
		return self.Articulo




