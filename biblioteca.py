from math import sin, cos, tan

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

def seno(a):
    return sin(a)

def cosseno(a):
    return cos(a)

def tangente(a):
    return tan(a)

def operacaoTipo1(funcao, a): # Funções tipo 1 possuem 1 operando.
    return funcao(a)

def operacaoTipo2(funcao, a, b): # Funções tipo 2 possuem 2 operandos.
    return funcao(a, b)

def resetaVisor():
    return '0'

def trocaSinalVisor(visor):
    if visor != '0':
        visor = float(visor)
        visor = -visor
    
    return str(visor)

def apagaVisor(visor):
    print('chegou aq')
    
    if len(visor) > 0:
        visor = visor[:len(visor) - 1]

    if visor[len(visor) - 1] == '.':
        visor = visor[:len(visor) - 1]

    if visor == '-' or visor == '0' or len(visor) == 0:
        visor = '0'

    return visor
