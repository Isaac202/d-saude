from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name='home'),
    path("agenda/", views.agenda, name='agenda'),
    path("login/", views.login_user, name='login'),
    path("logout_user/", views.logout_user, name='logout'),
    path("proficional/", views.proficional, name='proficional'),    
    path("usuario/", views.usuario, name='usuario'),
    path("especialidade/", views.especialidade, name='especialidade'),
    path("empresa/", views.empresa, name='empresa'),
    path("usuario_add/", views.create_user_admin, name='usuario_add'),
    path("edit_user_admin/", views.edit_user_admin, name='edit_user_admin'),    
     
]