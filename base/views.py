from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import JsonResponse, HttpResponseRedirect
from base.models import Orden, Servico, Usuarios, Empresa
from django.views.generic import View, TemplateView, FormView, ListView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, get_user_model



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
        user = Usuarios.objects.create_user(nome_completo=nome,
                                            username=email,
                                            email_user=email,
                                            cnpj=cnpj,
                                            cpf=cpf,
                                            tipo_user = '1',
                                            password=senha,
                                            criado_por = email,
                                            cnpj_empresa = cnpj,
                                            empresa_id = cnpj
                                            )
        print(user)
        user.save()
        return redirect('/dashboard/login/')
    
    return render(request,'admin/usuario_add.html')



def edit_user_admin(request):
    
    usuario = Usuarios.objects.filter(email_user = request.user.username)
    print(usuario)
    if request.method == "POST":
        nome = request.POST['nome']
        email = request.POST['email']
        cpf = request.POST['cpf']
        cnpj = request.POST['cnpj']
        senha = request.POST['senha']
        user = Usuarios.objects.filter(email_user = request.user.username).update(nome_completo=nome,
                                            username=email,
                                            email_user=email,
                                            cnpj=cnpj,
                                            cpf=cpf,
                                            tipo_user = '1',
                                        
                                            criado_por = email,
                                            cnpj_empresa = cnpj,
                                            empresa_id = cnpj
                                            )
        u = User.objects.get(username=request.user.username)
        u.set_password(senha)
        u.save()
        print(user)
       
        return redirect('/dashboard/edit_user_admin/')
    
    return render(request,'admin/edit_user_admin.html',{
        'usuario':usuario
    })


def create_proficional(request):
    if request.method == "POST":
        nome = request.POST['nome']
        email = request.POST['email']
        cpf = request.POST['cpf']
        cnpj = request.POST['cnpj']
        senha = request.POST['senha']
        especialidades = request.POST['senha']
        user = Usuarios.objects.create_user(nome_completo=nome,
                                            username=email, 
                                            email_user=email,
                                            cnpj=cnpj,
                                            cpf=cpf,
                                            tipo_user = '3',
                                            password=senha,
                                            criado_por = email,
                                            especialidade_user = especialidades,
                                            )
        print(user)
        user.save()
        return JsonResponse({'status':1}) 
    return render(request,'admin/usuario_add.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['email']
        senha = request.POST['senha']
        print(username, senha)
        user = authenticate( request,username=username, password=senha)
        if user is not None:
            login(request, user)
            print('LOgado')
            return redirect('/dashboard/')
    return render(request,'admin/login_user.html')


def logout_user(request):
    logout(request)
    return redirect('/dashboard/login/')
   

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
    if request.method == "POST":
        user = request.user.id
        usere = list(Usuarios.objects.filter(id=user).values('empresa_id'))
        empresa = usere[0]['empresa_id']
        nome = request.POST['nome']
        imagem = request.POST['img']
        empresa = ''
        criado_por= ''
     
        servico = Servico(nome=nome,
                       empresa=empresa,
                       imagem=imagem,
                       criado_por = criado_por)
        print(servico)
        servico.save()
        return JsonResponse({'status':1})
    return render(request,'admin/especialidade.html')