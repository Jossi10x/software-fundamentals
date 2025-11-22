Funcion Lanzamiento(dado1 Por Referencia, dado2 Por Referencia)
	dado1 <- azar(6)+1
	dado2 <- azar(6)+1
FinFuncion

Algoritmo reto_programación_6
	Definir dado1, dado2 Como Entero
	Definir suma_total, total_tiros, cant_pares, cant_impares, suma_lanzamiento como Entero
	Definir continuar Como Entero
	Definir desición Como Entero
	suma_total <- 0
	total_tiros <- 0 
	cant_pares <- 0
	cant_impares <- 0
	continuar <- 1
	
	Mientras continuar = 1
		Mostrar "Bienvenido!"
		Mostrar "1.Lanzar"
		Mostrar "2.Salir"
		Leer desicion
		si desicion = 1 Entonces
				Lanzamiento(dado1,dado2)
				suma_lanzamiento <- dado1 + dado2
				total_tiros <- total_tiros + 1
				suma_total <- suma_total + suma_lanzamiento
				si suma_lanzamiento mod 2 = 0 Entonces
					cant_pares <- cant_pares + 1
				SiNo
					cant_impares <- cant_impares + 1
				FinSi
		SiNo
			Mostrar "Numero de intentos: ",total_tiros
			Mostrar "Puntaje total: ", suma_total
			Mostrar "Cantidad de Pares: ",cant_pares
			Mostrar "Cantidad de Impares: ",cant_impares
			continuar <-  2
		FinSi
	FinMientras
FinAlgoritmo
	