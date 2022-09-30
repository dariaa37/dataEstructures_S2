// Karla Díaz Aguilar
// ARREGLO 2: Con el arreglo anterior, obtener la suma de todos los elementos

Algoritmo array_02
	Definir N, sum Como Real;
	N <- 10;			// Array size
	sum <- 0;		// Array sum
	
	Dimension array[N];
	
	Escribir "Suma de elemeentos de un rray de 10 posiciones (0-9)"
	// FOR to add numbers to array
	Para i <- 1 Hasta N Con Paso 1 Hacer;
		array[i] <- i-1;
		sum <- sum + array[i];	// Make the sum of every index from the array
		Escribir "Array element", "(", i , "): ", array[i]   	//Shows the array
	FinPara
	
	Escribir "<< Suma de elementos del array"
	Escribir "ARRAY ELEMNENTS SUM = ", sum
	
FinAlgoritmo
