from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import JsonResponse
from base.models import Orden, Usuarios, Empresa
from django.views.generic import View, TemplateView, FormView, ListView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, get_user_model
# Create your views here.
def empresa(request):
    emp = Empresa.objects.all()
    return render(request,'admin/empresa.html',{'empresa':emp})

def create_user_admin(request):
    if request.method == "POST":
        nome = request.POST['nome']
        email = request.POST['email']
        cpf = request.POST['cpf']
        cnpj = request.POST['cnpj']
        senha = request.POST['senha']
        user = Usuarios(nome_completo=nome,username=email, email_user=email, cnpj=cnpj,cpf=cpf, password=senha, criado_por = email)
        print(user)
        user.save()
        return redirect('/dashboard/login/')
    
    return render(request,'admin/usuario_add.html')

def login_user(request):
    if request.method == "POST":
        email = request.POST['email']
        senha = request.POST['password']
        print(email, senha)
        authenticate(username=email, password=senha)
       
        return redirect('/dashboard/')
    return render(request,'admin/login.html')

def home(request):
    #user = request.user.id
    #usere = list(Usuarios.objects.filter(id=user).values('empresa'))
    #empresa = usere[0]['empresa']
    #print(user, )
    order = Orden.objects.all() 
    if request.method == "POST":
        print(request.POST)
        return JsonResponse({'status':1})

    print(request.build_absolute_uri())   
    return render(request,'admin/index.html',{'order':order})

def create_order(request):
    
    return render(request,'admin/index.html')

def agenda(request):
    
    return render(request,'admin/agenda.html')

def proficional(request):
    
    return render(request,'admin/proficional.html')

def usuario(request):
    
    return render(request,'admin/usuario.html')

def especialidade(request):
    
    return render(request,'admin/especialidade.html')