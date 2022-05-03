Análisis de Algoritmos.
Programa 2: Búsquedas.
Alumna: Ana Valeria Deloya Andrade


Para ejecutar el programa, poner en terminal: python3 practica2.py n
	Donde n debe ser un número entero positivo, además de que es el número de 
	elementos que tendrá el arreglo.

Para generar el arreglo, hay dos formas, como tenemos esta condición en el problema:
	|A[i] − A[i + 1]| ≤ 1
Hice dos métodos para rellenar el arreglo, uno en el que |A[i] − A[i + 1]| = 1 sin 
elementos repetidos y otro con |A[i] − A[i + 1]| ≤ 1 donde hay elementos repetidos.
Al momento en el que el usuario pasa el valor de n, el arreglo se puede rellenar de
una de las dos formas, es al azar cuál de los dos será pues utilicé un random.

Para explicar el funcionamiento daré un ejemplo de un arreglo que puede generarse: 
	Con n = 5
		python3 practica2.py 5
	Esto nos va a crear un arreglo de tamaño 5, arreglo que puede verse así:
		A = [0,1,2,3,4]
	
	Y se va a generar un número z al azar que va a ser el que vamos a buscar 
	su posición en el arreglo A. 
	En este ejemplo, z = 3 

		Vamos a tener que el índice del inicio del arreglo es x = 0
		Y que el índice del final del arreglo es y = n-1
		
		En el algoritmo tenemos comienza con el siguiente método:
		Va a encontrar la posición de z en A con la ayuda de un método auxiliar 
			def busqueda(A, z):   
    			   return busqueda_aux(A, 0, len(A), z) 

		Este es el método auxiliar, que es el que hace la búsqueda del elemento z:
			def busqueda_aux(A, x, y, z):
  
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


      
	 Siguiendo con el ejemplo, sería entonces z = 3
		def busqueda(A, 3):   
    			   return busqueda_aux(A, 0, len(A), 3) 

	Ahora, siguiendo con el método que hace la búsqueda, trabaja de la siguiente
	forma:
	
	Con: 
		A = [0,1,2,3,4], x = 0, y = 5, z = 3
		

	*******************************************************************************************
	En el ejemplo: 
	
		Dividimos a la mitad el arreglo:
			mitad = (0+5)//2 = 2
		
		
		PRIMER IF
		Y la primer condición sería: if x > y  or mitad > len(A)-1:
					     if 0 > 4 o 2 > 4:
		Con = len(A)-1 = 5 - 1 = 4	
		Como no se cumple, pasamos a la siguiente condición.
		
		SEGUNDO IF
		La condición sería: if A[2] == 3
				         2  == 3
		Como no se cumple, pasamos a la siguiente condición.

		TERCER IF
		La condición sería: if A[mitad] > z:
      				  return busqueda_aux(A, x, mitad-1, z)
    				else:
      				  return busqueda_aux(A, mitad+1, y, z)

				    if A[2] > 3
				         2  > 3
	 	Y como no se cumplió pues A[mitad] es menor que z, pasamos al else.
		Haciendo recursión.
		Como mitad es menor que z, vamos a aumentar a x en 1 para hacer la recursión:
		x = mitad + 1 = 2 + 1 = 3 
				else:
      				  return busqueda_aux(A, 3, 5, 3)
		
	*******************************************************************************************
	Dividimos a la mitad el arreglo:
			mitad = (3+5)//2 = 4
		
		
		PRIMER IF
		Y la primer condición sería:if x > y  or mitad > len(A)-1: 
				            if 3 > 5 o 4 > 4:
		Con = len(A)-1 = 5 - 1 = 4	
		Como no se cumple, pasamos a la siguiente condición.
		
		SEGUNDO IF
		La condición sería: if A[4] == 3
				         4  == 3
		Como no se cumple, pasamos a la siguiente condición.

		TERCER IF
		La condición sería: if A[mitad] > z:
      				  return busqueda_aux(A, x, mitad-1, z)
    				else:
      				  return busqueda_aux(A, mitad+1, y, z)

				    if A[4] > 3
				         4  > 3
	 	Y como se cumplió pues A[mitad] es mayor que z, ya no pasamos al else.
		Haciendo recursión.
		Como mitad es mayor que z, vamos a disminuir a y en 1 para hacer la recursión:
		y = mitad - 1 = 4 - 1 = 3 
      				  return busqueda_aux(A, 3, 3, 3)
	
	*******************************************************************************************
	Dividimos a la mitad el arreglo:
			mitad = (3+3)//2 = 3
		
		
		PRIMER IF
		Y la primer condición sería:if x > y  or mitad > len(A)-1: 
					    if 3 > 3 o 3 > 4:
		Con = len(A)-1 = 5 - 1 = 4	
		Como no se cumple, pasamos a la siguiente condición.
		
		SEGUNDO IF
		La condición sería: if A[3] == 3
				         3  == 3
		Como se cumplió, ya pasamos a las siguientes condiciones.
		Encontramos la posición de z. Regresamos entonces el valor de mitad = 3
	
	Termina el programa.
	*******************************************************************************************

	Y efectivamente, z = 3 está en la posición 3 del arreglo:
		A = [0,1,2,3,4]
		
	Al terminar la ejecución del programa, en terminal va a mostrarse el arreglo A,
	el elemento z que vamos a buscar su posición y su posición en A.
	
	En este ejemplo se mostraría en terminal:
	
	-----------------------------------
	El arreglo A: 
	[0, 1, 2, 3, 4]
	El elemento z: 
	3
	La posición de z en el arreglo A:
	3
	-----------------------------------

	El algoritmo lo que hace para encontrar la posición de z es ir diviendo a la mitad y comparando
	si el elemento a la mitad del arreglo es mayor, menor o igual a z. Y de acuerdo con 
	eso vemos si aumentar a x, disminuir a y, o si es que ya encontramos la posición de z.



  
