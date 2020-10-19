import os
import sys
from integracao_numerica.numericalIntegration import *
from integracao_numerica.functions import  *
def interface():
    print("Escolha uma das funções para calcular a area abaixo da curva do gráfico  ")
    print("_________________________________________________________________________")

    print("         9")
    print("(1)\t\t-∫ √6x-5 dx")
    print("         1")
    print("_________________________________________________________________________")

    print("        0.8")
    print("(2)\t\t ∫ 1/x²-1 dx")
    print("         0")
    print("_________________________________________________________________________")

    print("        0.4")
    print("(3)\t\t ∫ e^x dx")
    print("         0")
    print("_________________________________________________________________________")

    get_op()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    return 0

def get_op():
    op = int(input("Digite a opção: "))
    selecao(op)


def selecao(op):
    f1 = 1
    f2 = 2
    f3 = 3
    while op:
        if op < 1 or op > 3:
            print("Opção inválida, por favor, digite um numero de 1 até 3 ")
            get_op()
        else:
            if op == f1:
                print(printFx())
                a1 = area_exata(-38)
                limites = intervalo(1,9)
                calcula_integral(f,limites,a1,100)

            elif op == f2:
                print(printGx())
                a2 = area_exata(-1.09861)
                limites = intervalo(0,0.8)
                calcula_integral(g,limites,a2,100)

            elif op == f3:
                print(printHx())
                a3 = area_exata(0.49182)
                limites = intervalo(0,0.4)
                calcula_integral(g,limites,a3,100)

            return op

def printFx():
    clear()
    print("Cálculo para: ")
    print("         9")
    print("(1)\t\t-∫ √6x-5 dx")
    print("         1\n")

def printGx():
    print("Cálculo para: ")
    print("        0.8")
    print("(2)\t\t ∫ 1/x²-1 dx")
    print("         0\n")

def printHx():
    print("Cálculo para: ")
    print("        0.4")
    print("(3)\t\t ∫ e^x dx")
    print("         0\n")

