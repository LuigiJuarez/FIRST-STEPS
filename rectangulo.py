def rectangulo(num1):
    for i in range(num1):
        matriz = ''
        for j in range(int(num1), i, -1):
            matriz += '*'
        for k in range(0, i):
            matriz += '*'
        print(matriz)

def base2(num1):
    divisor = 2
    residuos = []
    while num1 != 0:
        residuo = num1 % divisor
        cociente = num1 // divisor
        residuos.append(residuo)
        num1 = cociente
        base2 = residuos[::-1]
        print(base2)


def Options():
    print('Opciones')
    print('1. Rectangulo')
    print('2. Base 10 a base 2')
    print('3. Salir')
    return int(input('Ingrese la opcion a realizar '))


def GetValues():
    number1 = int(input('Ingrese numero: '))
    return number1


def GetResult(option, number1):
    result = 0
    if option == 1:
        result = rectangulo(number1)
    elif option == 2:
        result = base2(number1)


flag = True
while flag:
    option = Options()
    if option == 3:
        flag = False
    elif option > 3:
        print('Opcion invalida')
    else:
        number1 = GetValues()
        print(GetResult(option, number1))







