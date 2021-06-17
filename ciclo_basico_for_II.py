#1. Tamaño grande: dada una lista, escriba una función que cambie 
# todos los números positivos de la lista a "big".
#Ejemplo: biggie_size ([- 1, 3, 5, -5]) devuelve la misma lista, pero cuyos valores son 
#ahora [-1, "big", "big", -5]

def big_size(lista):
    for i in range(len(lista)):
        print({lista[i]})
lista = [4,5,6,3]
big_size(lista)


#2. Contar positivos : dada una lista de números, 
# cree una función para reemplazar el último valor 
# con el número de valores positivos. 
# (Tenga en cuenta que cero no se considera un número positivo).
#Ejemplo: count_positives([- 1, 1, 1,1 ]) cambia la lista original
#  a [-1, 1, 1, 3] y la devuelve
#Ejemplo: count_positives([1, 6, -4, -2, -7, -2]) cambia la lista 
# a [1, 6, -4, -2, -7, 2] y la devuelve


def contPositivos(lista):
    positivos = 0
    for num in lista:
        if num > 0:
            positivos += 1
    lista[len(lista)-1] = positivos
    return lista

lista = [5,-6,2,-7,15,-12,3]
print(contPositivos(lista))

#3 Suma total : crea una función que toma una lista y devuelve 
# la suma de todos los valores de la matriz.
#Ejemplo: sum_total ([1,2,3,4]) debería devolver 10
#Ejemplo: sum_total ([6,3, -2]) debería devolver 7

def suma_total(lista):
    suma=0
    for num in lista:
        suma += num
    return suma
print(suma_total(lista))

#4 Promedio : crea una función que toma una lista y devuelve el promedio de todos los valores.
#Ejemplo: el promedio ([1,2,3,4]) debería devolver 2.5

def promedio(lista):
    return suma_total(lista)/len(lista)
print(promedio(lista))

#5 Longitud : crea una función que toma una lista y devuelve la longitud de la lista.
#Ejemplo: la longitud ([37,2,1, -9]) debería devolver 4
#Ejemplo: longitud ([]) debería devolver 0

def longitud(lista):
    count =0
    for num in lista:
        count +=1
    return count
lista = [5,-6,2,-7,15,-12,4,8]
print(longitud(lista))

#6 Mínimo : crea una función que tome una lista de números y devuelva 
# el valor mínimo en la lista. Si la lista está vacía, 
# haga que la función devuelva False.
#Ejemplo: mínimo ([37,2,1, -9]) debería devolver -9
#Ejemplo: mínimo ([]) debería devolver False

#funcion06
def min(lista):
    if lista == 0:
        return False
    
    else:
        menor = lista[0]
        for num in lista:       # es igual a esto de aca en mas lineas
            if num < menor:
                menor = num
            else:
                menor = menor

            #menor = (num if num < menor else num) #esto es lo mismo que lo de arriba, esta es operacion ternaria. asi se llama

        return menor

lista = [5,-7,-10,1,-88,100,1]
print({min(lista)})



#7 Máximo : crea una función que toma una lista y devuelve el valor máximo en la matriz. 
# Si la lista está vacía, haga que la función devuelva False.
#Ejemplo: máximo ([37,2,1, -9]) debería devolver 37
#Ejemplo: máximo ([]) debería devolver False

def max(lista):
    if len(lista) == 0:
        return False
    
    else:
        mayor = lista[0]
        for num in lista:       
            if num > mayor:
                mayor = num

        return mayor

lista = [5,-7,-10,1,-88,100,1]
print({max(lista)})


#8 Análisis final : crea una función que tome una lista y devuelva un diccionario que 
# tenga la suma total, promedio, mínimo, máximo y longitud de la lista.
#Ejemplo: ultimate_analysis ([37,2,1, -9]) debería devolver 
# {'total': 31, 'promedio': 7.75, 'minimo': -9, 'maximo': 37, 'longitud': 4}

def analisis(lista):
    analisis ={
        "suma": suma_total(lista),
        "promedio": promedio(lista),
        "minimo": min(lista),
        "maximo": max(lista),
        "longitud": longitud(lista)
        }

    return analisis


#9 Lista inversa : crea una función que tome una lista y 
# la devuelva con los valores invertidos. Haz esto sin crear una segunda lista. 
# (Se sabe que este desafío aparece durante las entrevistas técnicas básicas).
#ejemplo: reverse_list ([37,2,1, -9]) debería devolver [-9,1,2,37]

