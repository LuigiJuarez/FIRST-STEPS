print('Multiplicacion por sumas sucesivas')
numero1= int(input('Ingrese numero 1: '))
numero2= int(input('Ingrese numero 2: '))
respuesta = 0
for i in range(numero2):    
    respuesta += numero1
print(respuesta)

