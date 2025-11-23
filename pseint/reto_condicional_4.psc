Funcion Menu
	Mostrar "Math menu"
	Mostrar "1.Add"
	Mostrar "2.Subs"
	Mostrar "3.Mult"
	Mostrar "4.Div"
	Mostrar "5.All"
FinFuncion
	
Funcion Calc(num1,num2,opt)
	Definir add, subs, mult,div como Real
	Segun opt Hacer
		Caso 1:
			add <- num1 + num2
			Mostrar "The result from the add: ",add
		Caso 2:
			subs <- num1 - num2
			Mostrar "The result from the subs: ",subs
		Caso 3:
			mult <- num1 * num2
			Mostrar "The result from the mult: ",mult
		Caso 4:
			Si num2 <> 0 Entonces
				div <- num1 / num2
				Mostrar "The result from the div: ",div
			Sino 
				Mostrar "Cant divided by zero!"
			FinSi
		Caso 5:
			Mostrar "1.Add: ",(num1+num2)," 2.Subs: ",(num1-num2)," Mult: ",(num1*num2)," and Div: ",(num1/num2)
		Caso _:
			Mostrar "Invalid Value"
	FinSegun
FinFuncion

Algoritmo reto_condicional_4
	Definir num1, num2 Como Real
	Definir opt Como Entero
	Mostrar "Enter the first number: "
	Leer num1
	Mostrar "Enter the second number: "
	Leer num2
	
	Menu()
	Leer opt
	
	Si opt > 0 y opt <= 5 Entonces
		Calc(num1,num2,opt)
	Sino
		Mostrar "Invalid value"
	FinSi
FinAlgoritmo
