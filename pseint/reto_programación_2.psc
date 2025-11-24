Algoritmo reto_programación_2
	Definir intentos, suma, num_intentos, dado como Entero
	Dimensionar intentos[10]
	suma <- 0
	Escribir ""
	Leer num_intentos
	
	si num_intentos > 0 y num_intentos <= 10 Entonces
		Para dado <- 1 Hasta num_intentos con paso 1 Hacer
			intentos[dado] <- azar(6)+1
			Mostrar "Intento ",[dado], ": ",intentos[dado]
		FinPara
		Para dado <- 1 Hasta num_intentos Con Paso 1 Hacer
			suma <- suma + intentos[dado]
		FinPara
		Mostrar "El puntaje de sus lanzamientos es: ",suma
	SiNo
		Mostrar "ERROR! Datos invalidos!"
	Fin si
FinAlgoritmo