#   Calculo Numerico (SME0602) - Projeto Pratico 1 - Metodo da Bisseccao
#   Alunos: Leandro Silva, Marianna Karenina, Marilene Garcia
#
#   Para rodar (no terminal linux): python bisseccao.py

import math
import numpy as np

def bisseccao( f, a, b, e ):
    x = []
    while (b - a)/2 > e:
        xi = (a + b)/2
        x.append(xi)

        if f(xi)*f(a) < 0:
            a_next = a 
            b_next = xi
        elif f(xi)*f(b) < 0:
            a_next = xi 
            b_next = b 
        else:
            break

        a = a_next
        b = b_next
    
    return x

def f1( x ):
    return math.cos(x)

def f2( x ):
    return x/2 - 2


def main(): 

    print( bisseccao(f1,0,math.pi,0.000001) )
    
    print( bisseccao(f2,0,25,0.000001) )


if __name__ == "__main__":
    main()

