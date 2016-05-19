from django import forms
from models import * 

def Get_ID_Persona(Object , Dato , Tipo):
		try:
		 	return Object.objects.get(ID_Persona= Dato.get("ID_Persona") ,Tipo_Persona = Tipo)
		except Object.DoesNotExist:
			return None


class login_Usuarios(forms.Form):
	ID_Persona = forms.CharField(label="ID Persona",max_length = 30)

	def clean_ID_Persona(self):
		Dato = self.cleaned_data
		Tipo = Tipo_Persona.objects.get(Nombre = "Civil")	
		ID = Get_ID_Persona(Civile,Dato,Tipo)
		if ID == None :
			raise forms.ValidationError("No se encontro el dato")
		else:
			return Dato

class login_Agente(forms.Form):
	ID_Persona = forms.CharField(label="ID Agente",max_length = 30)

	def clean_ID_Persona(self):
		Dato = self.cleaned_data
		Tipo = Tipo_Persona.objects.get(Nombre = "Agente")
		ID = Get_ID_Persona(Civile,Dato,Tipo)
		if ID == None :
			raise forms.ValidationError("No se encontro el dato")
		else:
			return Dato

class login_Admin(forms.Form):
	ID_Persona = forms.CharField(label="ID Admin",max_length = 30)

	def clean_ID_Persona(self):
		Dato = self.cleaned_data
		Tipo = Tipo_Persona.objects.get(Nombre = "Admin")
		ID = Get_ID_Persona(Civile,Dato,Tipo)
		if ID == None :
			raise forms.ValidationError("No se encontro el dato")
		else:
			return Dato



class registro(forms.Form):
	ID_Persona = forms.CharField(max_length = 15)
	Nombre = forms.CharField( max_length = 30)
	Apellido = forms.CharField(max_length = 30)
	Direccion = forms.CharField(max_length = 30)
	#Ciudad = forms.ForeignKey(label = "Ciudad" , Ciudade)
	#Tipo_Persona = forms.ForeignKey(label = "Tipo Persona" , Tipo_Persona)

class RegistroForm(forms.ModelForm):
	class Meta:
		model = Persona
		fields = ["ID_Persona","Nombre","Apellido","Direccion"]
