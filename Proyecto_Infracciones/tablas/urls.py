from django.conf.urls import include, url

from . import views

urlpatterns = [
	url(r'^$', views.inicio),
	url(r'^usuario/', views.Usuarios),
	url(r'^Administradores/', views.Administradores),
	url(r'^Admins/', views.Admins),
	url(r'^Agentes/', views.Agentes),
	
]