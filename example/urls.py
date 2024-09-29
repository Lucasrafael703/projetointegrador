# example/urls.py
from django.urls import path
from example.views import index, soma_quantidade_arrecadacao, pontos
from example.views import soma_quantidade_arrecadacao, pontos

urlpatterns = [
    path('', index, name='index'),  # Define a página inicial
    path('arrecadacao/', soma_quantidade_arrecadacao, name='soma_arrecadacao'),  # Corrige a rota duplicada e define um nome significativo
    path('pontos/', pontos, name='pontos'),  # Rota para 'pontos'
]

