#!/usr/bin/python
#coding: utf-8

#   Calculo Numerico (SME0602) - Projeto Pratico 1 
#   Alunos: Leandro Silva, Marianna Karenina, Marilene Garcia
#
#   Para rodar (no terminal linux): python main.py
#   Os resultados sao salvos no arquivo resultados.txt

import bisseccao
import secante
import newton
import halley
import math


def main():
    # Salvar os resultados em um txt
    resultados_bisseccao( )
    resultados_secante( ) 
    resultados_newton( )
    resultados_halley( )


# x = 0.739085
def f1( x ):
    return x - math.cos(x)

# x = 3.0
def f2( x ):
    return x**3 - (9* x**2) + 27 * x - 27

# x = 0; x = -1.232695..; x = -7.85359...; ...
def f3( x ):
    return math.exp(x) - math.cos(x)


def resultados_bisseccao( ):
    f = open("resultados", "w+")
    f.write("Resultados Bissecção: \n\n")
    resultados = []
    precisao_absoluta = 1e-16

    # Resultados do metodo da bisseccao
    f.write("Primeira Função: \n")
    resultados = bisseccao.bisseccao(f1, 0.0, math.pi, precisao_absoluta)
    f.write(str(resultados) + "\n")
    f.write("Aprox. Inicial: " + str(resultados[0]) + "\n")
    f.write("Aprox. Final: " + str(resultados[len(resultados) - 1]) + "\n\n")

    f.write("Segunda Função: \n")
    resultados = bisseccao.bisseccao(f2, 1.0, 5.0, precisao_absoluta)
    f.write(str(resultados) + "\n")
    f.write("Aprox. Inicial: " + str(resultados[0]) + "\n")
    f.write("Aprox. Final: " + str(resultados[len(resultados) - 1]) + "\n\n")
    
    f.write("Terceira Função: \n")
    resultados = bisseccao.bisseccao(f3, -2.0, 2.0, precisao_absoluta)
    f.write(str(resultados) + "\n")
    f.write("Aprox. Inicial: " + str(resultados[0]) + "\n")
    f.write("Aprox. Final: " + str(resultados[len(resultados) - 1]) + "\n\n")

    f.close

def resultados_secante( ):
    f = open("resultados", "a")
    f.write("\nResultados Secante: \n\n")
    resultados = []
    precisao_absoluta = 1e-16

    # Resultados do metodo da secante
    f.write("Primeira Função: \n")
    resultados = secante.secante(f1, 0.0, math.pi, precisao_absoluta)
    f.write(str(resultados) + "\n")
    f.write("Aprox. Inicial: " + str(resultados[0]) + "\n")
    f.write("Aprox. Final: " + str(resultados[len(resultados) - 1]) + "\n\n")

    f.write("Segunda Função: \n")
    resultados = secante.secante(f2, 1.0, 5.0, precisao_absoluta)
    f.write(str(resultados) + "\n")
    f.write("Aprox. Inicial: " + str(resultados[0]) + "\n")
    f.write("Aprox. Final: " + str(resultados[len(resultados) - 1]) + "\n\n")
    
    f.write("Terceira Função: \n")
    resultados = secante.secante(f3, -2, 2, precisao_absoluta)
    f.write(str(resultados) + "\n")
    f.write("Aprox. Inicial: " + str(resultados[0]) + "\n")
    f.write("Aprox. Final: " + str(resultados[len(resultados) - 1]) + "\n\n")

    f.close()

def resultados_newton( ):
    f = open("resultados", "a")
    f.write("\nResultados Newton: \n\n")
    resultados = []
    precisao_absoluta = 1e-16

    # Resultados do metodo da secante
    f.write("Primeira Função: \n")
    resultados = newton.newton(f1, math.pi, precisao_absoluta)
    f.write(str(resultados) + "\n")
    f.write("Aprox. Inicial: " + str(resultados[0]) + "\n")
    f.write("Aprox. Final: " + str(resultados[len(resultados) - 1]) + "\n\n")

    f.write("Segunda Função: \n")
    resultados = newton.newton(f2, 1.0, precisao_absoluta)
    f.write(str(resultados) + "\n")
    f.write("Aprox. Inicial: " + str(resultados[0]) + "\n")
    f.write("Aprox. Final: " + str(resultados[len(resultados) - 1]) + "\n\n")
    
    f.write("Terceira Função: \n")
    resultados = newton.newton(f3, -2, precisao_absoluta)
    f.write(str(resultados) + "\n")
    f.write("Aprox. Inicial: " + str(resultados[0]) + "\n")
    f.write("Aprox. Final: " + str(resultados[len(resultados) - 1]) + "\n\n")

    f.close()

def resultados_halley( ):
    f = open("resultados", "a")
    f.write("\nResultados Halley: \n\n")
    resultados = []
    precisao_absoluta = 1e-16

    # Resultados do metodo da secante
    f.write("Primeira Função: \n")
    resultados = halley.halley(f1, math.pi, precisao_absoluta)
    f.write(str(resultados) + "\n")
    f.write("Aprox. Inicial: " + str(resultados[0]) + "\n")
    f.write("Aprox. Final: " + str(resultados[len(resultados) - 1]) + "\n\n")

    f.write("Segunda Função: \n")
    resultados = halley.halley(f2, 1.0, precisao_absoluta)
    f.write(str(resultados) + "\n")
    f.write("Aprox. Inicial: " + str(resultados[0]) + "\n")
    f.write("Aprox. Final: " + str(resultados[len(resultados) - 1]) + "\n\n")
    
    f.write("Terceira Função: \n")
    resultados = halley.halley(f3, -2, precisao_absoluta)
    f.write(str(resultados) + "\n")
    f.write("Aprox. Inicial: " + str(resultados[0]) + "\n")
    f.write("Aprox. Final: " + str(resultados[len(resultados) - 1]) + "\n\n")

    f.close()



if __name__ == "__main__":
    main()

