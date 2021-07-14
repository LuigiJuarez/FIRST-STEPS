#teorema de pitagoras
# la suma del cuadrado de lo catetos es igual a cuadrado de la hipotenusa
# hipotenusa al cuadrado = cateto 1 al cuadrado + cateto 2 al cuadrado
# h**2 = c1**2 +c2**2
import math

h = 0
c1 = int(input("ingrese el cateto 1: "))
c2 = int(input("ingrese el cateto 2: "))
h = c1**2 + c2**2
print("la hipotenusa es: ", math.sqrt(h))