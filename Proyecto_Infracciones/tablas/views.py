from django.shortcuts import render
from models import *
from forms import *
# Create your views here.


def inicio(request):
	form = login_Usuarios(request.POST or None)
	context = { 
		"form":form
	}
	if form.is_valid():
			return render(request,"usuarios.html",context)
	return render(request,"inicio.html",context)

def Usuarios(request):
	return render(request,"usuarios.html",{})


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
		return render(request,"Agentes.html",context)

	if form_Admin.is_valid():
		return render(request,"Admins.html",context)

	return render(request,"Administradores.html",context)	

def Admins(request):
	return render(request,"Admins.html",{})

def Agentes(request):
	return render(request,"Agentes.html",{})