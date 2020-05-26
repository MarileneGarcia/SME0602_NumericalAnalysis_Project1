#   Calculo Numerico (SME0602) - Projeto Pratico 1 - Metodo de Newton
#   Alunos: Leandro Silva, Marianna Karenina, Marilene Garcia
#
#   Para rodar (no terminal linux): python newton.py

import math
import numpy as np

def newton( f, x0, e ):
    x = []
    x.append(x0)
    x_now = x0 - f(x0)/f_der(f,x0)
    x_previous = x0

    while abs(x_now - x_previous) > e:
        if(f_der(f,x_now) != 0):
            x_next = x_now - f(x_now)/f_der(f,x_now)

        x.append(x_now)
        x_previous = x_now
        x_now = x_next

    return x

def f1( x ):
    return math.cos(x)

def f2( x ):
    return x/2 - 2

def f_der( f, x ):
    h = 1e-5
    return (f(x+h)-f(x-h))/(2*h)

def main(): 

    #print( newton(f1,45,0.000001) )
    
    print( newton(f2,854242,0.000001) )


if __name__ == "__main__":
    main()

