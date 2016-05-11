from django.contrib import admin

# Register your models here.

from .models import Departamento,Ciudade,Casa,Modelo,Marca,Vehiculo,Tipo_Persona,Persona,Infracciones,Multa

admin.site.register(Departamento)
admin.site.register(Ciudade)
admin.site.register(Casa)
admin.site.register(Modelo)
admin.site.register(Marca)
admin.site.register(Vehiculo)
admin.site.register(Tipo_Persona)
admin.site.register(Persona)
admin.site.register(Infracciones)
admin.site.register(Multa)