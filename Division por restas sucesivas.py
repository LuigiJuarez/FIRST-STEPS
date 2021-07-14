contador = 0
print('Division por restas sucesivas')
dividendo= int(input('Ingrese numero 1: '))
divisor= int(input('Ingrese numero 2: '))
while (dividendo >= divisor):    
    contador += 1
    dividendo -= divisor
print(contador)