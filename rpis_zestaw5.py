import numpy as np  
import math 
import matplotlib.pyplot as plt 
import random

random.seed()

def Poisson(x):
    q = (math.e)**(-x)
    k = 0
    s = float(q)
    p = float(q)
    u = random.random()
    while(u > s):
        k += 1
        p = (p*x)/k
        s += p
    return k

def Generator(x):
    y = [0] * x
    i = 0
    while(i < x):
        y[i] = Poisson(4)
        i += 1
    return y

def Hist(z):
    plt.subplot(1, 2, 1)
    count, bins, ignored = plt.hist(z, 14, density=True)
    plt.title('Algorytm z wykładu')
    plt.ylabel('P(k)')
    plt.xlabel('k')

    s = np.random.poisson(4, 10000)
    plt.subplot(1, 2, 2)
    count, bins, ignored = plt.hist(s, 14, density=True, color ='green')
    plt.title('Funkcja biblioteczna')
    plt.ylabel('P(k)')
    plt.xlabel('k')
    plt.show()

Hist(Generator(10000))



