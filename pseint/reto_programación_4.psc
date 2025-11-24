Algoritmo reto_programación_4
	Definir dado1, dado2, contador como Entero
	contador <- 0
	
	Repetir
		contador <- contador + 1
		dado1 <- azar(6) + 1
		dado2 <- azar(6) + 1
		Mostrar "Lanzamiento ", contador, ": Salió ",dado1, " y ",dado2	
	Hasta Que dado1 = 6 y dado2 = 6
		Mostrar "Sacaste un par de 6, juego terminado"
	
FinAlgoritmo
