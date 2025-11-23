def Add(num1,num2):
    add = num1 + num2
    return add

def Subs(num1,num2):
    subs = num1 - num2
    return subs

def Mult(num1,num2):
    mult = num1 * num2
    return mult

def Div(num1,num2):
    if num2 != 0:
        div = num1 / num2
        return div
    else:
        return f"¡ERROR! Can't divided by zero!"    

mientras = True

while mientras == True:
    print("Welcome to calc v2!\n1.Add\n2.Subs\n3.Mult\n4.Div\n5.Exit")
    opt = int(input("Select your option: "))

    if opt >=1 and opt <=4:
        num1 = float(input("Enter the fisrt number: "))
        num2 = float(input("Enter the second number: "))

    match (opt):
        case 1:
            print(f"The result is ",Add(num1,num2))    
        case 2:
            print(f"The result is ",Subs(num1,num2))
        case 3:
            print(f"The result is ",Mult(num1,num2))
        case 4:
            resultado = Div(num1,num2)
            if isinstance(resultado, float):
                print(f"The result is ",resultado)
            else:
                print(resultado)
        case 5:
            print("Good Bye!")
            break
        case _:
            print("Invalid Value!")

        
