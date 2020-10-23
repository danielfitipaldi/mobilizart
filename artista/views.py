from django.contrib import messages
from django.core.validators import validate_email
from django.shortcuts import render, redirect
from .forms import FormArtista


def index(request):
    return render(request, 'artista/index.html')


def login(request):
    return render(request, 'artista/login.html')


def dashboard(request):
    return render(request, 'artista/dashboard.html')


def cadastrar(request):
    if request.method != 'POST':
        form = FormArtista()
        return render(request, 'artista/pag_cadastro.html', {'form': form})

    form = FormArtista(request.POST)

    email = request.POST.get('email')
    cpf = request.POST.get('cpf')

    try:
        validate_email(email)
    except:
        messages.error(request, 'E-mail inválido')
        form = FormArtista()
        return render(request, 'artista/pag_cadastro.html', {'form': form})

    if len(cpf) > 11:
        messages.error(request, 'CPF inválido')
        form = FormArtista()
        return render(request, 'artista/pag_cadastro.html', {'form': form})

    if form.is_valid():
        form.save()
        messages.success(request, 'Usuário cadastrado com sucesso')
        return redirect('cadastrar')
    return render(request, 'artista/pag_cadastro.html', {'form': form})


def mobilize(request):
    return render(request, 'artista/mobilize.html')














