import math as Math
import matplotlib.pyplot as plt

def main():
    print("\n______________________EDO - MÉTODO DE RUNGE KUTTA______________________________")

    print("#################################################################################")
    print("#################################################################################")
    print("_________________________________________________________________________________\n")
    calculus()

def kUm1(t,  c,  a):
    return c / (Math.exp(t) - 1) + 2 * Math.sin(t) * a / (Math.cos(t) * (1 + Math.exp(-t)))

def kDois1(t,  c,  a,  k1,  h):
    return (c + k1 / 2) / (Math.exp(t + h / 2) - 1) + 2 * Math.sin(t + h / 2) * (a + k1 / 2) / (Math.cos(t + h / 2) * (1 + Math.exp(-(t + h / 2))))

def kTres1(t,  c,  a,  k2,  h):
    return (c + k2 / 2) / (Math.exp(t + h / 2) - 1) + 2 * Math.sin(t + h / 2) * (a + k2 / 2) / (Math.cos(t + h / 2) * (1 + Math.exp(-(t + h / 2))))

def kQuatro1(t, c, a, k3, h):
    return (c + k3) / (Math.exp(t + h / 2) - 1) + 2 * Math.sin(t + h / 2) * (a + k3) / (Math.cos(t + h / 2) * (1 + Math.exp(-(t + h / 2))))

def kUm2(t,  c,  a):
    return 2 * a / (Math.exp(2 * t) - 1) - 2 * (1 + Math.exp(-t)) * Math.cos(t) * c / Math.sin(t)

def kDois2(t,  c,  a,  k1,  h):
    return 2 * (a + k1 / 2) / (Math.exp(2 * (t + h / 2)) - 1) - 2 * (1 + Math.exp(-(t + h / 2))) * Math.cos(t + h / 2) * (c + k1 / 2) / Math.sin(t + h / 2)

def kTres2(t,  c,  a,  k2,  h):
    return 2 * (a + k2 / 2) / (Math.exp(2 * (t + h / 2)) - 1) - 2 * (1 + Math.exp(-(t + h / 2))) * Math.cos(t + h / 2) * (c + k2 / 2) / Math.sin(t + h / 2)

def kQuatro2(t,  c,  a,  k3,  h):
    return 2 * (a + k3) / (Math.exp(2 * (t + h / 2)) - 1) - 2 * (1 + Math.exp(-(t + h / 2))) * Math.cos(t + h / 2) * (c + k3) / Math.sin(t + h / 2)


def calculus():
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
    c = 0.94845796
    a = 179.4625887
    auxa = 0
    auxc = 0
    erro =0

    plt.ioff()

    at=[]
    aa=[]
    ac=[]

    while t<4:
        auxa = a
        auxc = c
        k11 = h*kUm1(t, c, a)
        k21 = h*kUm2(t, c, a)

        k12 = h*kDois1(t, c, a, k11, h)
        k22 = h*kDois2(t, c, a, k21, h)

        k13 = h*kTres1(t, c, a, k12, h)
        k23 = h*kTres2(t, c, a, k22, h)

        k14 = h*kQuatro1(t, c, a, k13, h)
        k24 = h*kQuatro2(t, c, a, k23, h)
        print('t:{} || c:{} || a:{}'.format(t,c,a))
        at.append(t)
        aa.append(a)
        ac.append(c)
        c = c + (k11 + 2 * k12 + 2 * k13 + k14) / 6
        a = a + (k21 + 2 * k22 + 2 * k23 + k24) / 6
        erro = (a - auxa) / auxa + (c - auxc) / auxc
        t = t + h
    print("--Finished the program!--")
    return graphic(at,aa,ac)


def graphic(t,a,c):
    plt.title('Runge Kutta graph')
    plt.xlabel('tempo (t)')
    plt.ylabel('valores (c e a)')
    plt.grid(True)
    plt.plot(t,c,label='coelho', color = "green")
    plt.plot(t,a,label='ave', color = "orange")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()

