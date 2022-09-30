// Karla Díaz Aguilar
// ARREGLO 1: Crear un arreglo de 10 posiciones y llenarlo del 0 al 9

Algoritmo array_01
	Definir N, num, average Como Real;
	N <- 10;			// Array size
	
	Dimension array[N];
	
	Escribir "Crea un arreglo de 10 posiciones (0 a 9)"
	// FOR to add numbers to array
	Para i <- 1 Hasta N Con Paso 1 Hacer;
		array[i] <- i-1;
		Escribir "Array element", "(", i , "): ", array[i]  	//Shows the array
	FinPara
	
FinAlgoritmo
