from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('dashboard/', views.dash_accounts, name='dash_accounts'),
    path('cadastro/', views.cadastro_accounts, name='cadastro_accounts'),
    path('categoria/novo/', views.nova_categoria, name='nova_categoria'),
    path('lista/', views.listar, name='listar'),
    path('<int:artista_id>', views.detalhe_artista, name='detalhe_artista'),
    path('editar/<int:artista_id>', views.editar, name='editar'),
    path('deletar/<int:artista_id>', views.deletar_artista, name='deletar_artista'),
    path('logout/', views.logout, name='logout')
]