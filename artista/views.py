from django.shortcuts import render


def index(request):
    return render(request, 'artista/index.html')


def pagina_cadastro(request):
    return render(request, 'artista/pag_cadastro.html')


def login(request):
    return render(request, 'artista/login.html')


def dashboard(request):
    return render(request, 'artista/dashboard.html')
