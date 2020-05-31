#   Calculo Numerico (SME0602) - Projeto Pratico 1 - Ordem de Convergencia
#   Alunos: Leandro Silva, Marianna Karenina, Marilene Garcia

import math
import numpy as np

def ordem_convergencia( x, x_right ):
    tam = len(x)
    e = []
    p = 0.0

    for i in range(0, tam):
        e.append( abs(x[i] - x_right) )
    
    #print(e)
    
    for j in range(1, tam-1):
        n = math.log( (e[j+1]/e[j]) ,10)
        d = math.log( (e[j]/e[j-1]) ,10)
        if(d != 0):
            p =  n / d

    c = e[tam-1] / pow(e[tam-2],p)

    return c
        

