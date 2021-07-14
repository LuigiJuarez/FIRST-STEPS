import math

def factorial(num1):
    result = 1
    for i in range(num1):
        result *= num1
        num1 -= 1
    return result

def GetE(num1):
    e = 0
    for i in range(num1):
        e += (1/factorial(i))
    return e
    
def triangulo(num1):
    for i in range (num1 + 1):
        print('*' * i)

        
def primo(num1):
    if num1 == 1:
        return False
    for i in range(2, (int)(math.sqrt(num1))+1):
        if num1 % i == 0:
            return False 
    return True  

def Options():
    print('Opciones')
    print('1. Factorial')
    print('2. Calcular numero e')
    print('3. Triangulo')
    print('4. Numero Primo')
    print('5. Salir')
    return int(input('Ingrese la opcion a realizar '))

def GetValues():
    number1= int(input('Ingrese numero 1: '))
    return number1

def GetResult(option, number1):
    result = 0
    if option == 1:
        result = factorial(number1)
    elif option == 2:
        result = GetE(number1)
    elif option == 3:
        result = triangulo(number1)
    elif option == 4:
        result = primo(number1)
    return result

flag = True
while flag:
    option = Options()
    if option == 5:
        flag = False
    elif option > 5:
        print('Opcion invalida')
    else:
        number1 = GetValues()
        print(GetResult(option, number1))