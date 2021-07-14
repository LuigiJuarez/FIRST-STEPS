#xi es limite inferior
#xs es limite superior
#xa es la mitad del segmento

def f(x):
    y = pow(x,2)-(3*x)-4
    return (y)

#(xi+xs)/2
def Biseccion(x):
    xi = float(input('Introduce el valor del limite inferior '))
    xs = float(input('Introduce el valor del limite superior '))
    N = int(input('Introduce cuantas iteraciones se van a realizar ')) 
    for i in range(N):
        x = (xi+xs)/2
        if f(x) * f(xs) <0:
            xi=x
        elif f(x) * f(xi) <0:
            xs=x
        else :
            break
        print (i,x,f(x))
        
Biseccion(f)