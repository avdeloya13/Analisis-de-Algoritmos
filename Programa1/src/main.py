import numpy as np
import random
from math import log, floor
import sys
from time import sleep 

"""
Análisis de Algoritmos.
Programa 1: Problema de adoquinamiento.
Alumna: Ana Valeria Deloya Andrade
"""

def potencia(numero):
#Verifica que numero sea potencia de 2
  if numero < 1:
    return False
  i = log(numero, 2)
  return 0 == (i - floor(i))


def dimensiones(k):
#Crea un arreglo con dimensiones que sean
#potencia de 2
  if potencia(k):
    cuadricula = [[0]* k for x in range(k)]
    t = random.randint(0,k-1)
    s = random.randint(0,k-1)
    #El cuadro especial va a ser representado con: 5
    cuadricula[t][s] = 5
    cuadricula = np.array(cuadricula)
    return cuadricula
  else: 
    return "No es potencia de 2"


def cuadro_especial(arreglo):
  #La cuadricula (el arreglo) se divide en 4 cuadrantes, 
  #esta funcion lo que hace es ubicar en cuál de esos      
  #cuadrantes se encuentra el cuadro especial.
  i, j = np.where(arreglo == 5)
  i = int(i)+1
  j = int(j)+1
  m = len(arreglo)//2
  if i <= m and j <= m:
    return 1
  if i <= m and j > m:
    return 2
  if i > m and j <= m:
    return 3
  if i >= m and j >= m:
    return 4  
  else:
    return 13


def imprime(arreglo):
#Para imprimir arreglos
  for i in range(len(arreglo)):
    print("|" + str(arreglo[i]) + "|")


def adoquinar(arreglo):
  m = len(arreglo)
  #cuadrante en el que está el cuadro especial
  ce = cuadro_especial(arreglo)
  
  #CASO BASE
  if(m == 1):
    return arreglo

  #CASO BASE
  if(m == 2):
    imprime(arreglo)
    if(ce == 1):
      arreglo[0][1] = 5
      arreglo[1][0] = 5
      arreglo[1][1] = 5

    if(ce == 2):
      arreglo[0][0] = 5
      arreglo[1][0] = 5
      arreglo[1][1] = 5

    if(ce == 3):
      arreglo[0][0] = 5
      arreglo[0][1] = 5
      arreglo[1][1] = 5

    if(ce == 4):
      arreglo[0][0] = 5
      arreglo[0][1] = 5
      arreglo[1][0] = 5
    sleep(2)
    print("Cuadro especial en cuadrante:")
    print(ce)
    imprime(arreglo)
    print("******************")
    
  else:
    #CASO RECURSIVO
    if(ce == 1):
      arreglo[m//2][m//2] = 5
      arreglo[(m//2)-1][m//2] = 5
      arreglo[m//2][(m//2)-1] = 5

    if(ce == 2):
      arreglo[m//2][m//2] = 5
      arreglo[m//2][(m//2)-1] = 5
      arreglo[(m//2)-1][(m//2)-1] = 5
      
    if(ce == 3):
      arreglo[m//2][m//2] = 5
      arreglo[(m//2)-1][m//2] = 5
      arreglo[(m//2)-1][(m//2)-1] = 5

    if(ce == 4):
      arreglo[(m//2)-1][m//2] = 5
      arreglo[m//2][(m//2)-1] = 5
      arreglo[(m//2)-1][(m//2)-1] = 5
    print("Cuadro especial en cuadrante:")
    print(ce)
    imprime(arreglo)
    print("******************")

    #Cortamos el arreglo en las
    #dimensiones de los 4 cuadrantes
    c_1 = arreglo[0: m//2, 0: m//2]
    adoquinar(c_1)
    if(m != 2):
      print("Cuadrante 1 completado")
      imprime(arreglo) 
      print("******************")
       
    c_2 = arreglo[0: m//2, m//2: m] 
    adoquinar(c_2)
    if(m != 2):
      print("Cuadrante 2 completado")
      imprime(arreglo) 
      print("******************")
        
    c_3 = arreglo[m//2: m, 0: m//2]
    adoquinar(c_3)
    if(m != 2):
      print("Cuadrante 3 completado")
      imprime(arreglo)  
      print("******************")
        
    c_4 = arreglo[m//2: m, m//2: m]
    adoquinar(c_4)
    if(m != 2):
      print("Cuadrante 4 completado")
      imprime(arreglo)
      print("******************")
      
    sleep(2)


def main(k):
#Funcion principal, manda a llamar las otras funciones
  if(potencia(k)):
    arr = dimensiones(k)
    print("ARREGLO:")
    imprime(arr)
    print("")
    adoquinar(arr)
  else:
    print(dimensiones(k))

#Para recibir el numero dado por el usuario
#El número k a recibir debe ser potencia de 2
k = sys.argv[1]
k = int(k)
if(k < 0):
  print("Debes poner números positivos.")
else:
  main(k)
  