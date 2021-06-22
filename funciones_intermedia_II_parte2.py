#2.Itera a través de una lista de diccionarios
#Crea una función iterateDictionary(some_list)que, 
# dada una lista de diccionarios, la función recorra 
# cada diccionario de la lista e imprime cada clave y el valor asociado. 
# Por ejemplo, dada la siguiente lista:

#aqui agregar una funcion
def iterateDictionary(alguna_lista):
    for i in range(len(alguna_lista)):
        print()
        for key, value in alguna_lista[i].items():
            print(f"{key} {value}") #de esta manera se llama a los valores del diccionario
            #print(f"{key} - {value}, ", end=' ') #asi para imprimir todo en una linea cada dato
        
        else:
            print('Fin de la impresion de elementos enlistados')

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students) 
# La salida debería ser: (Está bien si cada clave y valor quedan en dos líneas separadas)
# Bonus: Hacer que aparezcan exactamente así!
#first_name - Michael, last_name - Jordan
#first_name - John, last_name - Rosales
#first_name - Mark, last_name - Guillen
#first_name - KB, last_name - Tonel

#3.Obtén valores de una lista de diccionarios
#Crea una función iterateDictionary2(key_name, some_list)que, 
# dada una lista de diccionarios y un nombre de clave, la función imprima el valor 
# almacenado en esa clave para cada diccionario. 
# Por ejemplo, iterateDictionary2 ('first_name', students) debería generar:

def iterateDictionary2(key_name, alguna_lista):
    for i in range(len(alguna_lista)):
        print(alguna_lista[i][key_name])

iterateDictionary2('first_name',students)
iterateDictionary2('last_name', students) 
