nombre = ["Jose", "Airam", "Mariam", "Anna", "Sanae"]
edades = [14, 24, 23, 17, 19]
clase = ["Mesa", "Profesor", 12.41, 19, 11.2]

print("Nombres: ")
for item in nombre:
    print(item)

print("----------------------------")
print("Edades: ")
for item in edades:
    print(item)

print("----------------------------")
print("Clase: ")
for item in clase:
    print(item)

lastName = nombre[len(nombre)-1]
lastedad = edades[len(edades)-1]
lastElement = clase[len(clase)-1]
print("----------------------------")
print("El ultimo nombre de la lista de nombres es "+lastName)
print("La ultima edad de la lista de edades es "+str(lastedad))
print("El ultimo elemento de la lista de clase es "+str(lastElement))
print("----------------------------")

peliculas={'1':'El médico', '2': 'Los Goonies', '3': 'El Protector', '4': 'Avatar'}
print("Diccionario:")
print(peliculas)
print("Claves del diccionario:")
for item in peliculas:
    print(item)
print("Valores del diccionario:")
for item in peliculas.values():
    print(item)
