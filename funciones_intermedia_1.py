import random
def randInt(min= 0 , max= 100):
    num = round(random.random() * (max-min) + min )    
    return num

def loteria():
    numeros = []
    numeros.append(randInt(1,36))
    while len(numeros) < 6:
        numero = randInt(1,36)
        flag = False
        for j in range(0,len(numeros)):
            if numeros[j] == numero:
                flag = True
                j = len(numeros)     
        if flag == False:          
            numeros.append(numero)

    numeros.sort(reverse=False)
    return numeros



print(randInt()) 		    # debería imprimir un número aleatorio entre 0 a 100
print(randInt(max=50)) 	    # debería imprimir un número aleatorio entre 0 a 50
print(randInt(min=50)) 	    # debería imprimir un número aleatorio entre 50 a 100
print(randInt(min=50, max=500))    # debería imprimir un número aleatorio entre 50 y 500
print(loteria())
print(randInt(min=100,max=50))

#ejercicio resuelto en clases con el profesor, esta muy interesante la aplicacion del random 
#randInt es solo una variable la verdadera funcion de sistema es Random