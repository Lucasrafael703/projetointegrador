# example/views.py
from datetime import datetime

from django.http import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Sum  # Importe Sum do módulo django.db.models
from .models import Arrecadacao, Arrecadacao_eletrodomestico

def soma_quantidade_arrecadacao(request):
    # Calcula a soma da quantidade de arrecadação
    soma = Arrecadacao.objects.aggregate(soma_quantidade=Sum('quantidade'))['soma_quantidade']
    context = {'soma_quantidade': soma}
    return render(request, 'index.html', context)

def soma_quantidade_eletrodomestico(request):
    # Calcula a soma da quantidade de arrecadação
    soma = Arrecadacao_eletrodomestico.objects.aggregate(soma_quantidade_eletrodomestico=Sum('quantidade'))['soma_quantidade_eletrodomestico']
    context = {'soma_quantidade_eletrodomestico': soma}
    return render(request, 'index.html', context)

def pontos(request):
    return render(request, "pontos.html")


def index(request):
    return render(request, 'index.html')  # Certifique-se de que você tem o template 'index.html'
