# Como exercício, escreva o sistema de EDO dos modelos compartimentais abaixo:
#EX02

#           K12*X1
# |     |------------>|     |
# |  x1 |             |  X2 |
# |     |<------------|     |
#    ^      K21 * X2     |
#    |                   |
#    |K31 * X3           |
#    |                   | K20*X2
# |     |                |
# |  X3 |                v
# |     |
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
    get_t()

def get_t():
    t_max = int(input("Digite o tempo de execução em minutos maior ou igual a 5 minutos: "))
    t_seg = t_max * 60
    if t_max < 5:
        print("Valores  para 't' menores do que 5 minutos diminui muito a precisão dos cálculos!")
        return get_t()
    return calculus_runge_kutta(t_seg)

def k_one1(x1, x2, x3, a, b):
    return a * x2 - b * x1

def k_two1(x1, x2, x3, k1, a, b):
    return a * (x2 + k1/2) - b* (x1 + k1/2)

def k_three1(x1, x2, x3, k2, a, b):
    return a * (x2 + k2/2) - b * (x1 + k2/2)

def k_four1(x1, x2, x3, k3, a, b):
    return a * (x2 + k3) - b * (x1 + k3)


def k_one2(x1, x2, a, b, c):
    return a * x1 - (c + a) * x2

def k_two2(x1, x2, k1, a, b, c):
    return b * (x1 + k1 / 2) - (c + a) * (x2 + k1 / 2)

def k_three2(x1, x2, k2, a, b, c):
    return b * (x1 + k2 / 2) - (c + a) * (x2 + k2 / 2)

def k_four2(x1, x2, k3, a, b, c):
    return b * (x1 + k3) - (c + a) * (x2 + k3)

def k_one3(x3, d):
    return d * x3

def k_one3(x3, d):
    return d * x3

def k_two3(x3, k1, d):
    return d * (x3 + k1 / 2)

def k_three3(x3, k2, d):
    return d * (x3 + k2 / 2)

def k_four3(x3, k3, d):
    return d * (x3 + k3)

def calculus_runge_kutta(t_max):
    a = 0.02
    b = 0.03
    c = 0.01
    d = -0.08

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

    k31 = 0
    k32 = 0
    k33 = 0
    k34 = 0
    x1 = 100
    x2 = 10
    x3 = 20
    auxa = 0
    auxb = 0
    auxc = 0
    erro = 0
    time = []
    x_one = []
    x_two = []
    x_three = []


    while t < t_max:
        auxa = x2
        auxb = x1
        auxc = x3

        k11 = h * k_one1(x1, x2, x3, a, b)
        k21 = h * k_one2(x1, x2, a, b, c)
        k31 = h * k_one3(x3, d)

        k12 = h * k_two1(x1, x2, x3, k11, a, b)
        k22 = h * k_two2(x1, x2, k21, a, b, c)
        k32 = h * k_two3(x3,k31, d)

        k13 = h * k_three1(x1, x2, x3, k12, a, b)
        k23 = h * k_three2(x1, x2, k22, a, b, c)
        k33 = h * k_three3(x3, k32, d)

        k14 = h * k_four1(x1, x2, x3, k13, a, b)
        k24 = h * k_four2(x1, x2, k23, a, b, c)
        k34 = h * k_four3(x3, k33 ,d)
        print('t:{} segundos || x1:{} || x2:{} || x3:{} || erro:{}'.format(round(t,0),round(x1,4),round(x2,4), round(x3,4), erro))

        time.append(t)
        x_one.append(x1)
        x_two.append(x2)
        x_three.append(x3)
        x1 = x1 + (k11 + 2 * k12 + 2 * k13 + k14) / 6
        x2 = x2 + (k21 + 2 * k22 + 2 * k23 + k24) / 6
        x3 = x3 + (k31 + 2 * k32 + 2 * k33 + k34) / 6
        erro = ((x2 - auxa) / auxa) + ((x1 - auxb) / auxb) + ((x3 - auxc) / auxc)
        t = t + h
    return ghrafic( x_one, x_two, x_three, time)



def ghrafic(x_one, x_two, x_three, t):
    plt.ioff()
    print("\nCriando gráfico...")
    fig2 = plt.figure(figsize=(14, 12))
    plt.title(' Runge Kutta graph - ex02')
    plt.legend()
    plt.xlabel('tempo (segundos)')
    plt.ylabel('valores (x1, x2 e x3)')
    plt.grid(True)
    plt.plot(t,x_one,label='x1', color = "orange")
    plt.plot(t,x_two,label='x2', color = "green")
    plt.plot(t,x_three,label='x3', color = "red")
    fig2.savefig('grafico2_rk.png', format = 'png', legend = plt.legend())
    print("Grafico criado, arquivo: grafico2_rk.png ")
    print("--Finished the program!--")
    plt.show()

if __name__ == "__main__":
    main()
