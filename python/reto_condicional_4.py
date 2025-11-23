def menu():
    print("Math menu")
    print("1.Add")
    print("2.Subs")
    print("3.Mult")
    print("4.Div")
    print("5.All")

def calc(num1,num2,opt):
    if opt > 0 and opt <= 5:
        match opt:
            case 1:
                add = num1 + num2
                print("The result from the add: ",add)
            case 2:
                subs = num1 - num2
                print("The result from the subs: ",subs)
            case 3:
                mult = num1 * num2
                print("The result from the mult: ",mult)
            case 4:
                if num2 != 0:
                    div = num1 / num2
                    print("The result from the div: ",div)
                else:
                    print("Cant divided by zero!")
            case 5:
                print("1.Add: ",num1+num2," 2.Subs: ",num1-num2," Mult: ",num1*num2," and Div: ",num1/num2)
            case _:
                print("Invalid Value")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
menu()
opt = int(input("Enter the option: "))

if opt > 0 and opt <= 5:
    calc(num1,num2,opt)
else:
    print("Invalid Value")      
