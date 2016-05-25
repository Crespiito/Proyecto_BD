from django.conf.urls import include, url ,patterns

from . import views

urlpatterns = [
	url(r'^$', views.inicio),
	url(r'^home/', views.Usuarios, name = 'usuario.index'),
	url(r'^usuario/(?P<id>\d+)/$', views.usuario_Actualizar, name = 'usuario_Actualizar.index'),
	url(r'^Agentes/Check/(?P<id>\d+)/$', views.Check, name = 'Check.index'),
	url(r'^Administradores/', views.Administradores, name='administradores.index' ),
	url(r'^Admins/', views.Admins , name = 'admins.index'),
	url(r'^Delet/(?P<id>\d+)/(?P<id_Admin>\d+)/$', views.Admins_Delet , name = 'admins_Delet.index'),
	url(r'^Agentes/', views.Agentes , name ='agentes.index'),
	
]