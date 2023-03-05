lenguajes=['Pythhon','Kotlin','Java','JavaScript']

print(lenguajes)

#Los arrays (list) comienza en la posicion 0
print(lenguajes[0])

#ordenar los elementos
lenguajes.sort()
print(lenguajes)

#Acceder a un elemento dentro de un texto
aprendiendo= f'Estoy aprendiendo {lenguajes[3]}'
print(aprendiendo)

#Modifica valores de un arreglo
lenguajes[2]='PHP'
print(lenguajes)

#Agregar elementos a un arreglo(List)
lenguajes.append('Ruby')
print(lenguajes)

#Eliminar de un arreglo(List)
del lenguajes[0]
print(lenguajes)

#eliminar de un arreglo(list)
lenguajes.pop()#Elimina el ultimo elemento
print(lenguajes)

#Elimina con pop una posicion en especifico
lenguajes.pop(0)
print(lenguajes)

#Eliminar por nombre+
lenguajes.remove('PHP')
print(lenguajes)

