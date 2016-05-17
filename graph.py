import matplotlib.pyplot as plt
import numpy
import random
import math

def function(x):
    try:
        return abs(math.sin(x**x)/((x**x-math.pi)))
    except:
        print('Informe um domínio válido')
        exit()

def generatey(x):
    y = [function(i) for i in x]
    return y

def generatex(start, end):
    x = numpy.linspace(start, end, (end-start)*100)
    return x

def plotgf(x, y):
    plt.grid(True)
    plt.axis([-0.5, 3.5, -0.5, 1.5])
    plt.plot(x, y, 'r-')
    plt.show()

if __name__ == '__main__':
    x = generatex(0, 3)
    y = generatey(x)
    plotgf(x, y)
