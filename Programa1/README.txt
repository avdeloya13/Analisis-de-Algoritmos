Análisis de Algoritmos.
Programa 1: Problema de adoquinamiento.
Alumna: Ana Valeria Deloya Andrade

Se debe tener instalado NumPy, se puede instalar escirbiendo en terminal lo siguiente:
	sudo apt install python3-pip
Y despues: 
	pip3 install numpy

Este es el link de una página que usé para instalar NumPy:
https://phoenixnap.com/kb/install-numpy  


Para ejecutar el programa, poner en terminal: python3 main.py k
	Donde k debe ser un número entero positivo potencia de 2.

Por ejemplo: python3 main.py 2
	Esto nos va a imprimir un arreglo de tamaño 2 x 2, arreglo que 
	va a contener un cuadro especial representado por un número 5.

Y en general, el cuadro especial es representado por un número 5.

Como la lógica para resolver el problema de adoquinamiento nos dice que debemos
ir dividiendo éste en 4 partes por la mitad vertical y horizontalmente: 

		[1 | 2]         
		-------
		[3 | 4]

Vamos a ver el arreglo dividido en 4 cuadrantes, nombrados como aparecen ahí, el cuadrante 
1,2,3,4.

Si el cuadro especial se encontrara en el cuadrante 1:

		[5 | 2]         
		-------
		[3 | 4]

Se le asigna el número 5 a los cuadrantes 2,3,4:

		[5 | 5]         
		-------
		[5 | 5]

Y al final vamos a tener el arreglo lleno de número 5.

A lo largo de la ejecución en terminal, se va a mostrar primero el arreglo con el primer
cuadro especial asignado y después se van a ir imprimiendo cómo el programa va llenando de
números 5 este arreglo. Nos va imprimiendo en qué cuadrante se encuentra el cuadro especial,
de esta forma: " Cuadro especial en cuadrante: 1 "

Ejemplo:
	En el arreglo:
	|[0 0 0 0]|
	|[0 0 0 5]|
	|[0 0 0 0]|
	|[0 0 0 0]|
	
	Cuadro especial en cuadrante:
	2
	|[0 0 0 0]|
	|[0 5 0 5]|
	|[0 5 5 0]|
	|[0 0 0 0]|

	******************
	(En este caso, tomamos el cuadrante 1 del arreglo impreso en el paso anterior (arriba),
	para llenarlo de 5)

	|[0 0]|
	|[0 5]|

	(El cuadro especial aquí en este sub arreglo de longitud 2 x 2, está en el cuadrante 4)
	Cuadro especial en cuadrante:
	4
	|[5 5]|
	|[5 5]|
	******************
	(Y volvemos al cuadrante 1 del arreglo. Ahora se encuentra ese cuadrante ya completo con 5's)

	Cuadrante 1
	|[5 5 0 0]|
	|[5 5 0 5]|
	|[0 5 5 0]|
	|[0 0 0 0]|
	******************

Y esa es la lógica que sigue y se va imprimiendo en terminal hasta llenar el arreglo.


