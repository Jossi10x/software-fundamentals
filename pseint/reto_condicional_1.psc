Algoritmo reto_condicional_1
	Definir dado1, dado2 Como Entero
	dado1 <- azar(6)+1
	dado2 <- azar(6)+1
	
	Si dado1 mod 2 = 0 Entonces
		Mostrar "El dado 1 es par"
	SiNo
		Mostrar "El dado 1 es impar"
	FinSi
	
	Si dado2 mod 2 = 0 Entonces
		Mostrar "El dado 2 es par"
	SiNo
		Mostrar "El dado 2 es impar"
	FinSi
	
	Si dado1 == dado2 Entonces
		Mostrar "You Win"
	SiNo
		Mostrar "Game over"
	FinSi
FinAlgoritmo
