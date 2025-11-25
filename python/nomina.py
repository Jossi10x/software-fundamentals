def Genero():
    while True:
        genero = input("Genero (M), (F), (O): ").upper()
        if genero in ["M","F","O"]:
          return genero
        else:
            print("Error! Ingrese M, F u O")


def Validar_salario():
    status = False
    while status == False:
        salario = input("Ingrese su salario: ")
        salario_size = len(salario)
        i = 0
        cont = 0
        while i < salario_size:
            if salario[i] < '0' or salario[i] > '9':
                cont += 1
            i += 1    
        if cont == 0:
            z = int(salario)
            status = True
        else:
            print("No es un numero")
    
    return z

def Validar_ano():
    anio_actual = 2025
    status = False
    while status == False:
        ano_nacimiento = input("Ingrese su año de nacimiento (AAAA): ")
        ano_nacimiento_size = len(ano_nacimiento)
        i = 0
        cont = 0
        while i < ano_nacimiento_size:
            if ano_nacimiento[i] < '0' or ano_nacimiento[i] > '9':
                cont += 1
            i += 1
            
        if cont == 0:
            if len(ano_nacimiento) == 4:
                z = int(ano_nacimiento)
                edad = anio_actual - z
                status = True
            else:
                print("Error! El año debe tener 4 digitos")
        else:
            print("No es un numero")
    return edad

def ValidarTelefono():    
    status = False
    z = 0 
    
    while status == False:
        telefono = input("Ingrese su numero de telefono: ")
        telefono_size = len(telefono)
        i = 0
        cont = 0
        while i < telefono_size:
            if telefono[i] < '0' or telefono[i] > '9':
                cont += 1
            i += 1 
        if cont == 0:
            if len(telefono) == 10:
                z = int(telefono)
                status = True 
            else:
                print("Error! El telefono debe tener 10 digitos.")
        else:
            print("Error! No es un numero valido.")
    
    return z

def Registrar_empleado():
    nombre = str(input("Ingrese su nombre completo: "))
    email = str(input("Ingrese su email: "))
    telefono = ValidarTelefono()
    genero = Genero()
    salario = Validar_salario()
    edad = Validar_ano()
    return nombre, email, telefono, genero, salario, edad

empleados = []
total_edad = 0
total_empleados = 0
total_salario = 0
total_M = 0
total_F = 0
total_O = 0
promedio_edad = 0
promedio_salario = 0

while True:
    option_menu = int(input("Menu\n1. Registrar empleado\n2. Salir\n"))
    if option_menu == 1:
        nombre, email, telefono, genero, salario, edad_empleado = Registrar_empleado()
        empleados.append((nombre, email, telefono, genero, salario, edad_empleado))
        total_empleados += 1
        total_salario += salario
        total_edad += edad_empleado
        if genero == "M":
            total_M += 1
        elif genero == "F":
            total_F += 1
        elif genero == "O":
            total_O += 1
        promedio_edad = total_edad / total_empleados
        promedio_salario = total_salario / total_empleados
    elif option_menu == 2:
        print("Hasta luego, vuelva pronto!")
        print("Empleados registrados: ", total_empleados)
        print("Promedio de salario: ", promedio_salario)
        print("Total de salario: ", total_salario)
        print("Total de hombres: ", total_M)
        print("Total de mujeres: ", total_F)
        print("Total de otros: ", total_O)
        print("Promedio de edad: ", promedio_edad)
        break
    


