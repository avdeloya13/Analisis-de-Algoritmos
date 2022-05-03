import sys
import random
"""
Análisis de Algoritmos.
Programa 2: Búsquedas.
Alumna: Ana Valeria Deloya Andrade
"""

def arreglo_sin_repetidos(n):
#Crea un arreglo sin elementos repetidos A[0...n-1] de n enteros, con |A[i] − A[i + 1]| = 1.
  A = []
  for i in range (n):
    A.append(i)
  return(A)


def arreglo_con_repetidos(A):
#Crea un arreglo con elementos repetidos A[0...n-1] de n enteros, con |A[i] − A[i + 1]| ≤ 1.
  j = 0
  
  for i in range(len(A)):
    opcion = random.randint(0,1)
    
    if opcion == 0:
      A[i] = j
      j = j+1
       
    if opcion == 1:
      A[i] = j
      
  return(A)
 

def busqueda_aux(A, x, y, z):
#Búsqueda de forma recursiva. Auxiliar para localizar al índice tal que A[indice] = z
  
  mitad = (x+y)//2
  
  if x > y  or mitad > len(A)-1:
    return -1
  else:
    if A[mitad] == z:
      return mitad
    elif A[mitad] > z:
      return busqueda_aux(A, x, mitad-1, z)
    else:
      return busqueda_aux(A, mitad+1, y, z)


def busqueda(A, z):   
  #Con un método auxiliar, localiza al índice tal que A[indice] = z
  return busqueda_aux(A, 0, len(A), z) 

  
#Para recibir el entero n dado por el usuario
n = sys.argv[1]
n = int(n)
if(n < 0):
  print("Debes poner números positivos.")
else:
  opcion = random.randint(0,1)

  if opcion == 0:
    print("El arreglo A: ")
    a = arreglo_sin_repetidos(n)
    print(str(a))
  
    z = random.randint(0,n-1)
    print("El elemento z: ")
    print(str(z))
  
    print("La posición de z en el arreglo A:")
    print(str(busqueda(a,z)))                
       
  if opcion == 1:
    print("El arreglo A: ")
    b = arreglo_con_repetidos( arreglo_sin_repetidos(n) )
    print(str(b))
  
    z = random.randint(0,n-1)
    print("El elemento z: ")
    print(str(z))
  
    print("La posición de z en el arreglo A:")
    print(str(busqueda(b,z)))