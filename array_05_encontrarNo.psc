// Karla Díaz Aguilar
// ARREGLO 5: Solicitar valores numericos mediante teclado para un arreglo.
//Buscar un elemento dentro del arreglo e indicar la posición donde se encuentra.
//Si se ingresan valores repetidos, debera indicar las posiciones del valor buscado.
// En caso de quue no exista el elemento solicitado, mostrar el mensaje "No se a encontrado ningun elemento con el valor ingresado"
Algoritmo Array_03
	Definir size Como Entero
	size = 6
	thereIsNot = 0
	Dimension array[size]
	
	Escribir "Solicitar valores numericos mediante teclado para un arreglo"
	Escribir "<< Ingresa un No. al Array >>"
	Para i <- 1 Hasta size Con Paso 1 Hacer
		Escribir "Número ", i, ":"
		Leer num
		array[i] <- array[i] + num
	FinPara
	
	Escribir "<< Ingresa el número a buscar >>"
	Leer n_search
	
	Para i <- 1 Hasta size Con Paso 1 Hacer
		Si array[i] = n_search Entonces
			Escribir "El valor ingresado ", n_search, " se encuentra en la posición ", i
		SiNo
			thereIsNot = thereIsNot + 1
		FinSi
	FinPara
	
	Si thereIsNot = size Entonces
		Escribir "No se a encontrado ningun elemento con el valor ingresado"
	FinSi
	FinAlgoritmo
