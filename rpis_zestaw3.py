import numpy as np      
import matplotlib.pyplot as plt 
import random

random.seed()

def QuantileFunction(x):
    if 5/6 < x <= 1:
        return 3 - np.sqrt(6 - 6*x)
    if 1/6 < x <= 5/6:
        return 3*x - 1/2
    if 0 <= x <= 1/6:
        return np.sqrt(6*x) - 1

def Generator(x):
    y = [0] * x
    i = 0
    while(i < x):
        z = random.uniform(0,1)
        y[i] = QuantileFunction(z)
        i += 1
    return y

def Histogram(x):
    plt.plot([-1, 0 ,2, 3], [0, 1/3, 1/3, 0], label = 'Funkcja matematyczna')
    plt.hist(x, bins = 60, density = True, label = 'Funkcja eksperymentalna')
    plt.ylabel('Gęstość')
    plt.xlabel('Zmienna losowa')
    plt.title('Porównanie matematycznej i eksperymentalnej funkcji gęstości')
    plt.legend()
    plt.show()

Histogram(Generator(10**3))
Histogram(Generator(10**5))
