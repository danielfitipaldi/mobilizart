from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('cadastro/', views.cadastrar, name='cadastrar'),
    path('mobilize/', views.mobilize, name='mobilize'),

]