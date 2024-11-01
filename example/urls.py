from django.urls import path
from example.views import index, soma_quantidade_arrecadacao, soma_quantidade_eletrodomestico, pontos, adicionar_doacao

urlpatterns = [
    path('', index, name='index'),
    path('arrecadacao/', soma_quantidade_arrecadacao, name='soma_arrecadacao'),
    path('arrecadacao_eletrodomestico/', soma_quantidade_eletrodomestico, name='soma_quantidade_eletrodomestico'),
    path('pontos/', pontos, name='pontos'),
    path('adicionar_doacao/', adicionar_doacao, name='adicionar_doacao'),
]
