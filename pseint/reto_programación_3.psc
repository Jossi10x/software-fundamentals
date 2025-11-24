Algoritmo reto_programación_3
	Definir dado, contadores, num_intentos Como Entero
	Dimensionar contadores[6]
	
	Para i <- 1 Hasta 6 Con Paso 1 Hacer
		contadores[i] <- 0
	FinPara
	
	Escribir "Cuantas veces quieres lanzar el dado (Máximo 100 veces): "
	Leer num_intentos
	
	Si num_intentos > 0 y num_intentos <= 100 Entonces
		Para i <- 1 Hasta num_intentos Con Paso 1 Hacer
			dado <- azar(6)+1
			contadores[dado] <- contadores[dado] + 1
			Mostrar "Dado ",[i], ": ",[dado]
		FinPara
		
		Para i <- 1 Hasta 6 con paso 1 Hacer
			Mostrar "Dado ",[i], " Salió ",contadores[i], " veces"
		FinPara
	SiNo
		Mostrar "El número de intentos no es válido!"
	FinSi
FinAlgoritmo
