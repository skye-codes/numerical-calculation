
import math
from integracao_numerica.interface import *
from integracao_numerica.functions import *

def maior_valor(m):
    return m

def calcula_integral(funcao, intervalo, area_real,n):
    valor_x =[]
    valor_y = []
    valor_derivada = []
    soma = 0
    area = 0
    i = 1
    #limits inferior and superior
    for i in range(len(intervalo) -1):
        a = (intervalo[i])
        b = (intervalo[i +1])

    #large of retangulo (x variation)
    delta_x = ( b - a) / (n - 1)

    #get valuer into the interval using delta_x variation
    for i in range(1,n) :
        x = a + delta_x * i
        y = funcao(x)
        valor_x.append(x)
        valor_y.append(y)
        valor_derivada.append(y)
        i  +=  delta_x

    # valor_derivada = derivada2_f(valor_x)
    for j in range(len(valor_y) - 1):
        soma += valor_y[j] + valor_y[j+1]
        valor_d = valor_y[j]
    area = soma * delta_x /2


    #error
    e = ((b - a) ** 3) / (12* (n**2)) * valor_d

    #print results
    print("\t\tIntervalo: {}".format([a,b]))
    print("\t\tA área EXATA é igual a: {}" .format(area_real), "m²")
    print("\t\tA área CALCULADA é igual a: {}" .format(round(area,4)), "m²")
    print("\t\tValor aproximado do erro final: ± {}" .format(round(e, 5)))
    print("\t\tQuantidade de execuções: {}" .format(n))


