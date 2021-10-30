from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name='home'),
    path("agenda/", views.agenda, name='agenda'),
    path("proficional/", views.proficional, name='proficional'),    
    path("usuario/", views.usuario, name='usuario'),
    path("especialidade/", views.especialidade, name='especialidade'),
    path("empresa/", views.empresa, name='empresa'),
    path("empresa_add/", views.empresa_add, name='empresa_add'),
     
]