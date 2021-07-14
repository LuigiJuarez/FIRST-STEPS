"area = base * altura / 2"
"base = b, altura = h"
#area = 0
#b = int
#h = int

#b = int(input("Introduce la base  "))
#h = int(input("Introduce la base  "))
#area = b * h/2
#print("el area del triangulo es ",area)


def triangulo(num1, num2):
    result = 0
    result = num1 * num2/2
    return result


def circulo(num1):
    result = 0
    pi = 3.1416
    result = pi * pow(num1,2)
    return result

def Options():
    print('Opciones')
    print('1. Triangulo')
    print('2. Circulo')
    print('3. Salir')
    return int(input('Ingrese la opcion a realizar '))


def GetValues1():
    number1 = int(input('Ingrese la base: '))
    number2 = int(input('Ingrese la altura: '))
    return number1, number2

def GetValues2():
    number1 = int(input('Ingrese el radio: '))
    return number1


def GetResult1(option, number1, number2):
    result = 0
    if option == 1:
        result = triangulo(number1, number2)
    return result

def GetResult2(option, number1):
    result = 0
    if option == 2:
        result = circulo(number1)
    return result

flag = True
while flag:
    option = Options()
    if option == 3:
        flag = False
    elif option > 3:
        print('Opcion invalida')
    else:
        if option == 1:
            number1, number2 = GetValues1()
            print(GetResult1(option, number1, number2))
        else:
            option == 2
            number1 = GetValues2()
            print(GetResult2(option, number1))



