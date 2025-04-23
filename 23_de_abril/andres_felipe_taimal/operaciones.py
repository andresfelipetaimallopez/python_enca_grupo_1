'''
crear las funciones suma,resta,multiplicacion,divsion(validar o  denominador),division piso
crear una funcion que genere un numero aleatorio (import random)
crear una funcion modulo(%)
'''
import random

def suma(a,b):
    return a+b

def resta (a,b):
    return a-b

def multiplicacion(a,b):
    return a*b

def division(a,b):
    if b==0:
        return "no divide por cero"

    return a/b
    
def division_piso(a,b):
    return a//b

def numero_aleatorio():
    return random.random()

def numero_aleatorio():
    return round(random.random(),2)

def modulo(a,b):
    return a%b