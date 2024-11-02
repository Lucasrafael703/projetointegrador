from django.urls import path
from . import views
from example.views import index, soma_quantidade_arrecadacao, soma_quantidade_eletrodomestico, pontos, adicionar_doacao

urlpatterns = [
    path('', views.index, name='index'),  # URL para a página inicial
    path('adicionar_doacao/', views.adicionar_doacao, name='adicionar_doacao'),
    path('arrecadacao/', views.soma_quantidade_arrecadacao, name='soma_arrecadacao'),
    path('arrecadacao_eletrodomestico/', views.soma_quantidade_eletrodomestico, name='soma_quantidade_eletrodomestico'),
    path('pontos/', views.pontos, name='pontos'),
]
