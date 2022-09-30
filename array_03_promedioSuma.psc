// Karla Díaz Aguilar
// ARREGLO 3: Con el arreglo del ejercicio 1 obtener la media de todos los elementos 

Algoritmo array_03
	Definir N, sum, average Como Real;
	N <- 10;			// Array size
	sum <- 0;		// Array sum
	average <- 0;	// Array promedio
	Dimension array[N];
	
	Escribir "Array de 10 posiciones (0-9)"
	// FOR to add numbers to array
	Para i <- 1 Hasta N Con Paso 1 Hacer;
		array[i] <- i-1;
		sum <- sum + array[i];	// Make the sum of every index from the array
		Escribir "Array element", "(", i , "): ", array[i]   	//Shows the array
	FinPara
	
	Escribir "<< Promedio de todos los elementos"
	average <- sum/N
	Escribir "ARRAY AVERAGE:= ", average
	
FinAlgoritmo
