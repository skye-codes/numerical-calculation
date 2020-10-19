# Como exercício, escreva o sistema de EDO dos modelos compartimentais abaixo:
#           K12*X1
# |     |------------>|     |
# |  x1 |             |  X2 |
# |     |<------------|     |
#           K21 * X2     |
#                        | K20*X2
#                        |
#
#dados: x1(0) = 100, x2(0) = 10, k12= 0.03 , k21= 0.02 e k20= 0.01
# para o exercício a) e para o exercício b) considere os mesmos valores acima e x3(0) = 20
# e k31= 0.08, junto com os gráficos de x1(t), x2(t) e x3(t)v

import math  as math
import matplotlib.pyplot as plt

def main():
    print("\n______________________EDO - MÉTODO DE RUNGE KUTTA______________________________")

    print("#################################################################################")
    print("#################################################################################")
    print("_________________________________________________________________________________\n")
    calculus_runge_kutta()




def k_one1(x1, x2, a, b):
    return a * x2 - b * x1

def k_two1(x1, x2, k1, a, b):
    return a * (x2 + k1/2) - b* (x1 + k1/2)

def k_three1(x1, x2, k2, a, b):
    return a * (x2 + k2/2) - b * (x1 + k2/2)

def k_four1(x1, x2, k3, a, b):
    return a * (x2 + k3) - b * (x1 + k3)

def k_one2(x1, x2, a, b, c):
    return a * x1 - (c + a) * x2

def k_two2(x1, x2, k1, a, b, c):
    return b * (x1 + k1 / 2) - (c + a) * (x2 + k1 / 2)

def k_three2(x1, x2, k2, a, b, c):
    return b * (x1 + k2 / 2) - (c + a) * (x2 + k2 / 2)

def k_four2(x1, x2, k3, a, b, c):
    return b * (x1 + k3) - (c + a) * (x2 + k3)

def calculus_runge_kutta():

    a = 0.02
    b = 0.03
    c = 0.01

    h = 0.001
    t = 0.1

    k11 = 0
    k12 = 0
    k13 = 0
    k14 = 0

    k21 = 0
    k22 = 0
    k23 = 0
    k24 = 0

    x1 = 100
    x2 = 10

    auxa = 0
    auxc = 0

    erro = 500
    time = []
    x_one = []
    x_two = []
    while t < 325:

        auxa = x2
        auxc = x1

        k11 = h*k_one1(x1, x2, a,b)
        k21 = h*k_one2(x1, x2, a,b, c)

        k12 = h*k_two1(x1, x2, k11, a, b)
        k22 = h*k_two2(x1, x2, k21, a, b, c)

        k13 = h* k_three1(x1, x2, k12, a, b)
        k23 = h*k_three2(x1, x2, k22, a, b, c)

        k14 = h*k_four1(x1, x2, k13, a, b)
        k24 = h*k_four2(x1, x2, k23, a, b, c)

        print('t:{} || x1:{} || x2:{} || erro:{}'.format(t,x1,x2,erro))
        time.append(t)
        x_one.append(x1)
        x_two.append(x2)
        x1 = x1 + (k11 + 2 * k12 + 2 * k13 + k14) / 6
        x2 = x2 + (k21 + 2 * k22 + 2 * k23 + k24) / 6
        erro = (x2 - auxa) / auxa + (x1 - auxc) / auxc
        t = t + h
    return ghrafic( x_one, x_two, time)

def ghrafic(x_one, x_two, t):
    plt.ioff()
    print("\nCriando gráfico...")
    fig = plt.figure(figsize=(14, 12))
    plt.title(' Runge Kutta graph')
    plt.legend()
    plt.xlabel('tempo (t)')
    plt.ylabel('valores (x1 e x2)')
    plt.grid(True)
    plt.plot(t,x_one,label='x1', color = "orange")
    plt.plot(t,x_two,label='x2', color = "green")
    fig.savefig('grafico_rk.png', format = 'png', legend = plt.legend())
    print("Grafico criado, arquivo: grafico_rk.png ")
    print("--Finished the program!--")
    plt.show()



if __name__ == "__main__":
    main()
