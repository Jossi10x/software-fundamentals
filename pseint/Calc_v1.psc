Algoritmo Calc_v1
	//Welcome to my firs program
	//Calculatore
	
	// Menu
	Mostrar "Welcome to calculatore!/"
	Mostrar "Seletct the operation"
	Mostrar "1.Addition"
	Mostrar "2.Substraction"
	Mostrar "3.Multiplication"
	Mostrar "4.Division"
	
	//Variable declaration
	Definir option Como Entero
	Definir num1, num2, result Como Real
	
	//Variable assing
	Escribir "Select the option: "
	Leer option
	Escribir "Enter the first number: "
	Leer num1
	Escribir "Enter the second number: "
	Leer num2
	
	//Conditional structure
	//Operations and outputs
	
	Si option >=1 y option <= 4 Entonces
		si option == 1 Entonces
			result <- num1 + num2 //Addition	
			Mostrar "The result of the sum is: ", result
		FinSi
		si option == 2 Entonces
			result <- num1 - num2 //substraction
			Mostrar "The result of the substraction is: ", result
		FinSi
		si option == 3 Entonces
			result <- num1 * num2 //multiplication
			Mostrar "The result of the multiplication is: ", result
		FinSi
		si option == 4 Entonces
			si num2 <> 0 Entonces
				result <- num1 / num2 //division
				Mostrar "The result of the division is: ", result
			SiNo
				Mostrar "Error! Cannot	be divided by zero!"
			FinSi
		FinSi
	SiNo
		Mostrar "Invalid value"
	FinSi
FinAlgoritmo
