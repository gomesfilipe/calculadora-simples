from math import sin, cos, tan, sqrt

def soma(a, b):
    return str(float(a) + float(b))

def subtracao(a, b):
    return str(float(a) - float(b))

def multiplicacao(a, b):
    return str(float(a) * float(b))

def divisao(a, b):
    return str(float(a) / float(b))

def seno(a):
    return str(sin(float(a)))

def cosseno(a):
    return str(cos(float(a)))

def tangente(a):
    return str(tan(float(a)))

def quadrado(a):
    return str(float(a) ** 2)

def raiz(a):
    if float(a) < 0:
        return 'Entrada inválida'
    
    return str(sqrt(float(a)))

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
    if len(visor) > 0:
        visor = visor[:len(visor) - 1]

    if len(visor) > 0:
        if visor[len(visor) - 1] == '.':
            visor = visor[:len(visor) - 1]

    if visor == '-' or visor == '0' or visor == '':
        visor = '0'

    return visor

def ehOperacaoTipo1(event):
    if event == 'sin(x)' or event == 'cos(x)' or event == 'tan(x)' or event == 'x²' or event == '√x':
        return True
    
    return False