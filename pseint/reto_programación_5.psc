Funcion Contador(num_intentos)
	definir dado1, dado2, cont_impares, cont_pares, i Como Entero
	cont_impares <- 0
	cont_pares <- 0
	
	Para i <- 1 Hasta num_intentos Con Paso 1 Hacer
		dado1 <- azar(6) + 1
		dado2 <- azar(6) + 1
		Si dadod1 mod 2= 0 y dado2 mod 2 = 0 Entonces
			cont_pares <- cont_pares + 1
		Sino
			cont_impares <- cont_impares + 1
		FinSi
	FinPara
	Mostrar "Numeros impares obtenidos ", cont_impares
	Mostrar "Numeros pares obtenidos ", cont_pares
FinFuncion

Algoritmo reto_programación_5
	Definir num_intentos como Entero
	Mostrar "Cuantos lanzamientos quieres realizar (Máximo 100): "
	Leer num_intentos
	
	Si num_intentos > 0 y num_intentos <= 100 Entonces
		Contador(num_intentos)
	SiNo
		Mostrar "Numero de intentos no válido!"
	FinSi
FinAlgoritmo
