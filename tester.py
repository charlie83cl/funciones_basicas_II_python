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

