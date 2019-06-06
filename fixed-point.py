#given a function such as x = g(x)
#is called fixed because x is unchaged while g(x) is applied to it
#many iterative algorithms for solving nonlinear equations can be written as follow
#open - iterative - efficient 
#rewrite by adding/substracting x
#if g'(x)<0 it will converge 
#overall x(n+1) = g(x)
import numpy
from matplotlib import pyplot as plt
import math

def fixed_point(f, g, x, t):
    #Definimos todas las variables
    xn = 0 
    e = 1
    i = 0
    #mientras el error sea mayor a la tolerancia, seguiremos iterando
    while e > t:
        #xn debe ser el valor de la función g(x) evaluada en x viejo
        xn = g(x)
        #para la siguiente iteración, x viejo será xn
        x = xn
        #verificando que el error sea haya satisfacido en f(x)
        e = abs(f(xn))
        #contador de iteraciones ++
        i+=1
    #devolvemos el valor último de xn y el número de iteraciones
    return xn,i

def g(x):
    return 5/(math.pow(math.e,0.5*x)+1.2)
    #return 1+2/x

def f(x):
    return x*math.pow(math.e, x*0.5)+1.2*x-5
    #return x**2-x-2

def f1(x):
    return x

def zero(x):
    return 0

print(fixed_point(f, g, 1, 0.0001))

#Gráfica
a1 = 1
b1 = 3
paso = 0.1
x=numpy.arange(a1, b1, paso)
x1=numpy.arange(a1, b1, paso)


Y_F = [f(i) for i in x1]
Y_G = [g(i) for i in x]
Y_F1 = [f1(i) for i in x]
Y_0 = [zero(i) for i in x]

fig1=plt.figure()
axe=fig1.add_subplot(1,1,1)    
axe.plot(x1,Y_F,'b',label='f(x)')
axe.plot(x,Y_G, 'y', label='g(x)',  linestyle='--')
axe.plot(x,Y_F1, 'r', label='x',  linestyle='--')
axe.plot(x,Y_0, 'g')

axe.legend()
plt.ylabel("y")
plt.xlabel("x")
plt.title("fixed-point")
plt.show()