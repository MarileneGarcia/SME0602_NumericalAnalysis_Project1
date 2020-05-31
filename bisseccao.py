#   Calculo Numerico (SME0602) - Projeto Pratico 1 - Metodo da Bisseccao
#   Alunos: Leandro Silva, Marianna Karenina, Marilene Garcia

import math
import numpy as np

def bisseccao( f, a, b, e ):
    x = []

    while abs(b-a)/2 > e:
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

