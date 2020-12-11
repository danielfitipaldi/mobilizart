from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.core.validators import validate_email

from artista.models import Artista
from .forms import FormCategoria
from .models import Categoria
from artista.forms import FormArtista


def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, username=usuario, password=senha)

    if not user:
        messages.error(request, 'Usuário ou senha inválido')
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        messages.success(request, f'Você está logado como {user}')
        return redirect('dash_accounts')


def logout(request):
    auth.logout(request)
    return redirect('login')


def cadastro_accounts(request):
    if request.method != 'POST':
        return render(request, 'accounts/cadastro_accounts.html')

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    if not nome or not sobrenome or not email or not usuario or not senha or not senha2:
        messages.error(request, 'Todos os campos devem ser preenchidos')
        return render(request, 'accounts/cadastro_accounts.html')

    try:
        validate_email(email)
    except:
        messages.error(request, 'E-mail inválido')
        return render(request, 'accounts/cadastro_accounts.html')

    if len(senha) < 6:
        messages.error(request, 'A senha precisa ter pelo menos 6 caracteres')
        return render(request, 'accounts/cadastro_accounts.html')

    if len(usuario) < 6:
        messages.error(request, 'O nome de usuário precisa ter pelo menos 6 caracteres')
        return render(request, 'accounts/cadastro_accounts.html')

    if senha != senha2:
        messages.error(request, 'As senhas não coincidem')
        return render(request, 'accounts/cadastro_accounts.html')

    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Nome de usuário já existe')
        return render(request, 'accounts/cadastro_accounts.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'E-mail já cadastrado')
        return render(request, 'accounts/cadastro_accounts.html')

    messages.success(request, 'Registrado com sucesso. Agora faça o login para entrar')
    user = User.objects.create_user(username=usuario, email=email, password=senha,
                                    first_name=nome, last_name=sobrenome, is_superuser=True)

    user.save()
    return redirect('login')


@user_passes_test(lambda user: user.is_superuser, redirect_field_name='login', login_url='login')
def dash_accounts(request):
    return render(request, 'accounts/dash_accounts.html')


@login_required(redirect_field_name='login', login_url='login')
def nova_categoria(request):
    form = FormCategoria(request.POST)

    nome = request.POST.get('nome')
    if Categoria.objects.filter(nome=nome).exists():
        messages.error(request, 'Categoria já cadastrada')
        form = FormCategoria()
        return render(request, 'accounts/nova_categoria.html', {'form': form})

    if form.is_valid():
        form.save()
        messages.success(request, 'Categoria salva com sucesso!')
        return redirect('dash_accounts')
    return render(request, 'accounts/nova_categoria.html', {'form': form})


@login_required(redirect_field_name='login', login_url='login')
def listar(request):
    artistas = Artista.objects.order_by('-id')

    paginator = Paginator(artistas, 11)

    page = request.GET.get('page')

    artistas = paginator.get_page(page)

    return render(request, 'accounts/lista_usuarios.html', {
        'artistas': artistas
    })


@login_required(redirect_field_name='login', login_url='login')
def detalhe_artista(request, artista_id):
    artista = get_object_or_404(Artista, id=artista_id)

    return render(request, 'accounts/detalhe_artista.html', {
        'artista': artista
    })


@login_required(redirect_field_name='login', login_url='login')
def editar(request, artista_id):
    obj = get_object_or_404(Artista, id=artista_id)

    email = request.POST.get('email')
    cpf = request.POST.get('cpf')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    form = FormArtista(request.POST or None, instance=obj)

    if form.is_valid():

        if senha != senha2:
            messages.error(request, 'Senhas não coincidem')
            form = FormArtista()
            return render(request, 'accounts/edicao_artista.html', {'form': form})

        if len(cpf) != 11:
            messages.error(request, 'CPF inválido')
            form = FormArtista()
            return render(request, 'accounts/edicao_artista.html', {'form': form})

        try:
            validate_email(email)
        except:
            messages.error(request, 'E-mail inválido')
            form = FormArtista()
            return render(request, 'accounts/edicao_artista.html', {'form': form})

        form.save()
        messages.success(request, 'Cadastro atualizado')
        return HttpResponseRedirect('/accounts/lista')

    return render(request, "accounts/edicao_artista.html", {'form': form})


@login_required(redirect_field_name='login', login_url='login')
def deletar_artista(request, artista_id):
    artista = get_object_or_404(Artista, id=artista_id)

    if request.method == "GET":
        artista.delete()
        messages.success(request, 'Usuário apagado com sucesso')
        return HttpResponseRedirect("/accounts/lista")

    return render(request, "accounts/delete_view.html")
