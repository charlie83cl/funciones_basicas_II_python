#Itera a través de un diccionario con valores de listas
#Crea una función printInfo(some_dict)que, 
# dado un diccionario cuyos valores son todas listas, 
# imprima el nombre de cada clave junto con el tamaño de su lista,
#  y luego imprima los valores asociados dentro de la lista de cada clave. 
# Por ejemplo:
def printInfo(algun_dict):
    for key, val in algun_dict.items():
        print(f"{len(val)}{key.upper()}") #el key.upper es solo para darle mayusculas a los valores de key del diccionario
        for i in val:
            print(i)
        
        
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)


# output:
#7 LOCATIONS
#San Jose
#Seattle
#Dallas
#Chicago
#Tulsa
#DC
#Burbank
    
#8 INSTRUCTORS
#Michael
#Amy
#Eduardo
#Josh
#Graham
#Patrick
#Minh
#Devon