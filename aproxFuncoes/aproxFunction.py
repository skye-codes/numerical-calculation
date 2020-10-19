import matplotlib.pyplot as plt
import pandas as pd

#data source: IBGE
# https://seriesestatisticas.ibge.gov.br/series.aspx?no=4&op=0&vcodigo=PD330&t=taxa-analfabetismo-pessoas-10-anos-mais
data = pd.read_csv("analfabetismoIBGE.csv")


def main():
    print("\n______________________TAXA DE ANALFABETISMO NO BRASIL ENTRE OS ANOS DE 1992 E 2011________")
    print("_________________________________________APROXIMAÇÃO DE FUNÇÕES_____________________________")
    print("_________________________________________FONTE DE DADOS: IBGE_______________________________")
    print("############################################################################################")
    print("############################################################################################\n")

    print(data,'\n')
    approxFunction()

def sumOne(x):
    i = len(x)
    c = 0
    aux = 0
    while True:
        if c == i:
            break
        aux += x[c]
        c += 1
    return aux


def sumTwo(x, y):
    i = len(x)
    c = 0
    aux = 0
    while True:
        if c == i:
            break
        aux += x[c] * y[c]
        c += 1
    return aux


def straightEquation(g, x, a, b):
    i = len(x)
    c = 0
    while True:
        if c == i:
            break
        g.append(b * x[c] + a)
        c += 1
    return g


def residual(f, g):
    i = len(f)
    c = 0
    aux = 0
    while True:
        if c == i:
            break
        aux += (f[c] - g[c]) ** 2
        c += 1
    return aux

def approxFunction():
    year =[]
    fx = []
    for index, row in data.iterrows():
        year.append(int(row['Período']))
        fx.append(float(row['Taxa de Analfabetismo']))
        # print(fx)
        # print ("data[" + str(index) + "]" + "   " + str(row['Período']) + " = " + str(row['Taxa de Analfabetismo']))



    count = len(year)
    sum_x = sumOne(year)
    sum_x2 = sumTwo(year, year)
    sum_y = sumOne(fx)
    sum_xy = sumTwo(year, fx)



    alpha = (-1) * count / sum_x
    b = (alpha * sum_xy + sum_y) / (alpha * sum_x2 + sum_x)
    a = (sum_y - sum_x * b) / count

    gx = []
    gx = straightEquation(gx, year, a, b)

    print("\n##################################################################\n")
    print("Equação da reta g(x): {}x + ({})".format(round(b, 4),round(a,4)))
    print("f'Resíduo Quadrático: r2(x) = {}".format(round(residual(fx, gx), 4)))


    print()
    print('Prospectiva da taxa de analfabetismo no Brasil')
    print(f'2020: {b * 2020 + a :.4}%')
    graphic(year, fx, gx, a, b)

def graphic(x, fx, gx, a, b):
    plt.ioff()
    plt.title('Aproximação de funções - Prospectiva da taxa de analfabetismo no Brasil')
    plt.scatter(x, fx, label='F(x)', color = 'red')
    plt.plot(x, gx, label=f'G(x): {b:.4}x + ({a:.4})')
    plt.xlabel('Ano')
    plt.ylabel('Analfabetismo (%)')
    plt.legend()
    plt.show()
if __name__ == "__main__":
    main()