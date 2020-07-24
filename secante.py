#   Calculo Numerico (SME0602) - Projeto Pratico 1 - Metodo da secante
#   Alunos: Leandro Silva, Marianna Karenina, Marilene Garcia

import math
import numpy as np

def secante( f, x0, x1, e ):
  x = []
  f0 = f(x0)
  f1 = f(x1)

  x2 = x1 - f1 * (x1 -x0) / (f1 - f0)
  x.append(x2)

  while abs(x2 - x1) > e:
    x0 = x1
    f0 = f1

    x1 = x2 
    f1 = f(x1)

    x2 = x1 - f1 * (x1 -x0) / (f1 - f0)
    x.append(x2)
  
  return x