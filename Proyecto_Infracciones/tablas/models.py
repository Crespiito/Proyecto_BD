from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Departamento(models.model):
	ID_Departamento = models.AutoField(Primary_key = True )
	Nombre = models.charfield(max_length = 30 )


class Ciudad(models.model):
	ID_Ciudad = models.AutoField(Primary_key = True)
	ID_Departamento = models.ForeignKey(Departamento)
	Nombre = models.charfield(max_length = 30 )


class Casa(models.model):
	ID_Casa = models.AutoField(Primary_key = True)
	Nombre = models.charfield(max_length = 30)
	Direccion = models.charfield(max_length = 30)


class Marca(models.model):
	ID_Marca = models.AutoField(Primary_key = 30)
	Nombre = models.charfield(max_length = 30)
	ID_Casa = models.ForeignKey(Casa)


class Modelo(models.model):
	ID_Modelo = models.AutoField(Primary_key = 30)
	Nombre = models.charfield(max_length = 30)
	ID_Marca = models.ForeignKey(Marca)


class Tipo_Persona (models.model):
	ID_Tipo_Persona = models.charfield(max_length = 15 , Primary_key = True)
	Nombre = models.charfield(max_length = 30)
	Descripcion = models.charfield(max_length =50)


class Persona(models.model):
	ID_Persona = models.charfield(max_length = 15, Primary_key = True)
	Nombre = models.charfield(max_length = 30)
	Apellido = models.charfield(max_length = 30)
	Direccion = models.charfield(max_length = 30)
	ID_Ciudad = models.ForeignKey(Ciudad)
	ID_Tipo_Persona = models.ForeignKey(Tipo_Persona)


class Infracciones(models.model):
	ID_Infracciones = models.AutoField(Primary_key=True)
	ID_Persona = models.ForeignKey(Persona)
	Lugar = models.charfield(max_length = 30)


class Vehiculo(models.model):
	ID_vehicuo = models.charfield(max_length = 7 , Primary_key = True)
	ID_Persona = models.ForeignKey(Persona)
	ID_Modelo = models.ForeignKey(Modelo)
	Fecha_Matriculacion = models.charfield(max_length = 8)


class Multa(models.model):
	ID_Multa = models.AutoField(Primary_key = True)
	ID_Persona = models.ForeignKey(Persona)
	ID_vehicuo = models.ForeignKey(Vehiculo)
	Fecha = models.charfield(max_length = 8)
	Articulo = models.charfield(max_length = 120)
	Costo = models.IntegerField()
	ID_Infracciones = models.ForeignKey(Infracciones)





