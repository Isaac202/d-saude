from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from base.models import Orden, Usuarios, Empresa

# Create your views here.
def empresa(request):
    emp = Empresa.objects.all()
    print(emp)
    return render(request,'admin/empresa.html',{'empresa':emp})

def empresa_add(request):
    if request.method == "POST":
        nome = request.POST['nome']
        email = request.POST['email']
        cpf = request.POST['cpf']
        cnpj = request.POST['cnpj']
        print(cpf,cnpj)
        empresa = Empresa(nome=nome,email=email,cnpj=cnpj,cpf=cpf, criado_por= request.user.id)
        print(empresa)
        empresa.save()
        return JsonResponse({'status':1})
    
    return render(request,'admin/empresa_add.html')

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

def create_user(request):
    
    return render(request,'admin/usuario.html')

def create_user_admin(request):
    
    return render(request,'admin/usuario.html')


def agenda(request):
    
    return render(request,'admin/agenda.html')

def proficional(request):
    
    return render(request,'admin/proficional.html')

def usuario(request):
    
    return render(request,'admin/usuario.html')

def especialidade(request):
    
    return render(request,'admin/especialidade.html')