from django.shortcuts import render,redirect
from django.http import HttpResponse
from models import *
from forms import *
# Create your views here.



def clean(Object):
	Dato = Object.cleaned_data
	return Dato

def inicio(request):
	form = login_Usuarios(request.POST or None)
	context = { 
		"form":form
	}
	if form.is_valid():
			Datos = form.cleaned_data.copy()
			request.session['Usuario'] = Datos['ID_Persona']
			return redirect('usuario.index', permanent = True )
	return render(request,"inicio.html",context)

def Usuarios(request):
	context = {}
	try:
		Usuario = request.session.pop('Usuario')
		print Usuario
		ObPersona = Persona.objects.get(ID_Persona = Usuario.get("ID_Persona"))
		ObMultas = Multa.objects.filter(ID_Persona = ObPersona)
		context['Usuario'] = ObPersona
		context['Multas'] = ObMultas		
		return render(request,"usuarios.html", context)
	except:	
		return render(request,"usuarios.html",{})

def usuario_Actualizar(request, id):
	ObMulta = Multa.objects.get(id = id)
	Usuario={}
	Usuario["ID_Persona"]= ObMulta.ID_Persona.ID_Persona
	request.session['Usuario'] = Usuario
	print request.session['Usuario']
	ObMulta.ID_Pago = Pago.objects.get(Estado = 'Pago') 
	ObMulta.save()
	return redirect("usuario.index")


def Administradores(request):
	if 'Agente' in request.POST:
		form_Agentes = login_Agente(request.POST or None)
		form_Admin = login_Admin()
	elif 'Admin' in request.POST:
		form_Agentes = login_Agente()
		form_Admin = login_Admin(request.POST or None)
	else: 
		form_Agentes = login_Agente()
		form_Admin = login_Admin()

	context = { 
		"form_Admin":form_Admin , "form_Agentes":form_Agentes
	}

	if form_Agentes.is_valid():
		Dato = form_Agentes.cleaned_data.copy()
		request.session['Agente'] = Dato["ID_Persona"]
		return redirect('agentes.index',  permanent = True)

	elif form_Admin.is_valid():
		Dato = form_Admin.cleaned_data.copy()
		request.session['Admin'] = Dato["ID_Persona"]
		return redirect('admins.index',  permanent = True)

	else:	
		return render(request,"Administradores.html",context)	

def Admins(request):
	context = {}
	Tipo = Tipo_Persona.objects.get(Nombre = "Admin")
	try:
		Admin = request.session.pop('Admin')
		ObAdmin = Civile.objects.get(ID_Persona = Admin.get("ID_Persona") , ID_Tipo_Persona = Tipo) 
		context['Admin']= ObAdmin
	except:
		pass
	ObMultas = Multa.objects.all()
	context['Multas'] = ObMultas 
	return render(request,"Admins.html",context)

def Admins_Delet(request,id,id_Admin):
	Admin={}
	Admin["ID_Persona"]= id_Admin
	request.session['Admin'] = Admin
	ObMulta = Multa.objects.get(id = id)
	ObMulta.delete()
	return redirect("admins.index")

def Check(request,id):
	Agente={}
	Agente["ID_Persona"]= id
	request.session['Agente'] = Agente
	return redirect("agentes.index")

def Agentes(request):
	context={}
	Tipo = Tipo_Persona.objects.get(Nombre = "Agente")
	try:
		Agente = request.session.pop('Agente')
		ObAgente = Civile.objects.get(ID_Persona = Agente.get("ID_Persona") , ID_Tipo_Persona = Tipo) 
		context['Agente']= ObAgente
	except:
		pass
	form_Multas = MultaForm(request.POST or  None)
	form_Multas.fields['ID_Agente'].queryset=Civile.objects.filter(ID_Tipo_Persona= Tipo)
	context["Multa"] = form_Multas

	if form_Multas.is_valid():
		form_Multas.save()

	return render(request,"Agentes.html",context)