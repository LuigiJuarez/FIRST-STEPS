# la formula chicharronera
# busca la raices de una ecuacion de segundo grado
# raices = x
# x1 = (-b+raiz cuadrada de (b**2-4*a*c ))/2a
# x2 = (-b-raiz cuadrada de (b**2-4*a*c ))/2a

import math

x1 = 0
x2 = 0
a = int(input("ingrese el valor de a: "))
b = int(input("ingrese el valor de b: "))
c = int(input("ingrese el valor de c: "))
e = 4*a*c
x1 = (-b+math.sqrt((b**2)-e))/(2*a)
x2 = (-b-math.sqrt((b**2)-e))/(2*a)
print("las raices de esta ecuacion son ", x1," y ", x2)
print(e)
print(math.sqrt(b**2-e))