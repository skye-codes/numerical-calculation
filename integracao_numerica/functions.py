
#"(1) -∫ √6x-5 dx" x E [1,9]
#"(2) ∫ 1/x²-1 dx" x E [0.4,0.8]
#"(3) ∫ e^x dx" x E [0,0.4]


import  math


#functions to calculate the area
def f(x):
    return  (-1*(math.sqrt(6*x -5)))

def g(x):
    return 1 / ( x**2 -1)

def h(x):
    return math.e**x

#second darivation of the functions
# def derivada2_f(x):
#     d = -((27*x -30) / (( 6*x -5) * (math.sqrt(6*x - 5))))
#     return d
#
# def derivada2_g(x):
#     return -1*(2*((-3*x**2 - 1) / ((x**2 - 1)**3)))
#
# def derivada2_h(x):
#     return math.e**x

#limits of the inegration
def intervalo(a,b):
    limites = []
    limites.append(a)
    limites.append(b)
    return limites

def area_exata(a):
    return a
