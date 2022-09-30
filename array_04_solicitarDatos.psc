// Karla Díaz Aguilar
// ARREGLO 4: Solicitar valores numéricos mediante consola para dos arreglos diferentes 
// y guardar el valor de cada elemento en cada posición (posición 0 arreglo 1, posición 0 del arreglo 2 y así sucesivamente)
// 1. Realizar en un tercer arreglo la suma de cada una de las posiciones ingresadas manualmente 

Algoritmo Array_02
	Definir size, num1, num2, sum Como Real
	// Variable declarations
	size <- 6;	num1 <- 0;
	num2 <- 0;	sum <- 0
	
	// Arrays dimension
	Dimensión array1[size]
	Dimension array2[size]
	Dimension array3[size]
	
	// For adding numbers to Array1 and 2
	Escribir "Ingresa los valores para:"
	Para i <- 1 Hasta size Con Paso 1 Hacer 
		Escribir "ARREGLO 1 - Indice (", i, "):"	// 1,2,3,4,5,6
		Leer num1
		array1[i] <- array1[i] + num1
		
		Escribir "ARREGLO 2 - Indice (", i, "):"	// 7,8,9,10,11,12
		Leer num2
		array2[i] <- array2[i] + num2
		
		// Sum array1 and array2
		sum <- array1[i] + array2[i]			
		
		array3[i] <- array3[i] + sum
	FinPara
	
	// For to show Array 3 elements
	Escribir "<< TERCER ARRAY >>"
	Para i <- 1 Hasta size Con paso 1 Hacer
		Escribir array3[i]
	FinPara

	
FinAlgoritmo
