from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pagina_cadastro/', views.pagina_cadastro, name='pagina_cadastro'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard')
]