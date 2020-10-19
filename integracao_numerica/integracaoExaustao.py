
import matplotlib.pyplot as plt
import matplotlib as mpl
def main():
    print("\n_______INTEGRAÇÃO NÚMERICA - METÓDO DA EXAUSTÃO________________________")
    for i in range(2):
        print("######################################################################")
    #valores de limite inferior, superior e n
    calcula(0,10,1000)
    print("\t\tFinished!")

def f(x):
    return x +x**2

def delta_x(a,b,n):
    d = (b-a) / n
    return d

def erro(area, area_real):
    e = (area - area_real) / area_real
    return e


def calcula(a, b, n):
    soma = 0
    area = 0
    x = []
    area_real = 383.33
    i = 0
    delta = delta_x(a, b,n)
    while i < n:
        a =  a + delta
        y = f(a)
        area += y * delta
        err = erro(area, area_real)
        i += 1
    e = err
    return imprimir(round(area,2), area_real,e, i)

def imprimir(a,ar,e, i):
    print("________________________________________________________________________")
    print("_______Resultados - Area do gráfico para a função: f(x) = x + x²________")
    print("\n\t\tA área calculada é igual a: {}" .format(a), "m²")
    print("\t\tA área real é igual a: {}" .format(ar), "m²")
    print("\t\tValor aproximado do erro final: ± {}" .format(round(e, 5)))
    print("\t\tQuantidade de execuções: {}" .format(i))


main()
