#1. Actualiza los valores en diccionarios y listas
#Cambia el valor 10 en x a 15. Una vez que haya terminado, 
#x ahora debería ser [[5,2,3], [15,8,9]].
#Cambia el apellido del primer alumno de 'Jordan' a 'Bryant'
#En el directorio sports_directory, cambia 'Messi' a 'Andres'
#Camba el valor 20 en z a 30

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15 #aca se cambia el segundo elemento de la primera lista.
print(x)

students[0]['last_name'] = 'Bryant'# de esta forma se cambia el elemento last_name de la lista 0
#para recorrer un dicconario es recomendado hacerlo por el nombre de los objetos

#students[0].update({'last_name':'Bryant2'}) # esta es una alternativa de como actualizar o cambiar datos dentro de diccionario
print(students)

sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

z[0]['y'] = 30
print(z)





