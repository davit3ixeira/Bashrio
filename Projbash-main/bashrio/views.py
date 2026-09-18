from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib import messages
from .models import Evento, Organizador, Perfil
from django.conf import settings


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        return redirect('home')
    return render(request, "login.html")

def processar_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if not email or not password:
            messages.error(request, 'Por favor, preencha todos os campos.')
            return redirect('login')
        
        try:
            user = User.objects.get(username=email)
            user = authenticate(request, username=email, password=password)
            
            if user is not None:
                login(request, user)
                Perfil.objects.get_or_create(user=user)
                messages.success(request, f'Bem-vindo, {user.first_name or user.username}!')
                return redirect('home')
            else:
                messages.error(request, 'Email ou senha incorretos.')
                return redirect('login')
        except User.DoesNotExist:
            user = User.objects.create_user(username=email, email=email, password=password)
            user = authenticate(request, username=email, password=password)
            if user:
                login(request, user)
                Perfil.objects.get_or_create(user=user)
                messages.success(request, 'Usuário criado e logado com sucesso!')
                return redirect('home')
            else:
                messages.error(request, 'Erro ao criar usuário.')
                return redirect('login')
    
    return redirect('login')

def home(request):
    username = request.user.username if request.user.is_authenticated else 'Visitante'
    return render(request, "paghome.html", {"username": username})

def addEventos(request):
    eventos = Evento.objects.all().order_by('-criado_em')
    return render(request, "add_eventos.html", {"eventos": eventos})

def cadastrar_evento(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        cidade = request.POST.get('city')
        local = request.POST.get('local')
        preco = request.POST.get('prices')
        data = request.POST.get('data')
        hora = request.POST.get('hora')
        duracao = request.POST.get('duracao')
        informacoes = request.POST.get('info')
        imagem = request.FILES.get('imagem')
        
        if not titulo:
            messages.error(request, 'O título do evento é obrigatório.')
            return render(request, "cadastrar_evento.html")
        
        evento = Evento(
            titulo=titulo,
            cidade=cidade,
            local=local,
            preco=preco,
            data=data if data else None,
            hora=hora if hora else None,
            duracao=duracao if duracao else None,
            informacoes=informacoes,
            imagem=imagem if imagem else None
        )
        evento.save()
        
        messages.success(request, 'Evento publicado com sucesso!')
        return redirect('add_eventos')
    
    return render(request, "cadastrar_evento.html")

def inicio_conta(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para acessar esta página.')
        return redirect('login')
    
    perfil, created = Perfil.objects.get_or_create(user=request.user)
    
    return render(request, "inicio_conta.html", {"perfil": perfil})

def alterar_senha(request):
    return render(request, "alterar_senha.html")

def esqueci_senha(request):
    return render(request, "esqueci_senha.html")

def logout_view(request):
    logout(request)
    messages.success(request, 'Você foi desconectado com sucesso.')
    return redirect('home')

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        cpf = request.POST.get('CPF')
        data_nascimento = request.POST.get('data')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        
        if not email or '@' not in email:
            messages.error(request, 'Por favor, insira um email válido com @.')
            return render(request, "cadastro.html")
        
        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, 'Por favor, insira um email válido.')
            return render(request, "cadastro.html")
        
        if password != password_confirm:
            messages.error(request, 'As senhas não coincidem.')
            return render(request, "cadastro.html")
        
        if len(password) < 6:
            messages.error(request, 'A senha deve ter pelo menos 6 caracteres.')
            return render(request, "cadastro.html")
        
        if User.objects.filter(username=email).exists():
            messages.error(request, 'Este email já está cadastrado.')
            return render(request, "cadastro.html")
        
        try:
            user = User.objects.create_user(
                username=email,
                email=email,
                password=password
            )
            user.first_name = nome
            user.save()
            
            cpf_limpo = cpf.replace('.', '').replace('-', '').replace(' ', '') if cpf else None
            
            perfil = Perfil.objects.create(
                user=user,
                telefone=telefone,
                cpf=cpf_limpo,
                data_nascimento=data_nascimento if data_nascimento else None
            )
            
            messages.success(request, 'Cadastro realizado com sucesso! Faça login para continuar.')
            return redirect('login')
        except Exception as e:
            messages.error(request, f'Erro ao criar conta: {str(e)}')
            return render(request, "cadastro.html")
    return render(request, "cadastro.html")