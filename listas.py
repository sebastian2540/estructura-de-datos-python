# Estructura de datos
#Son objetos que permiten almacenar en una sola variable.

"""fruta1 = "Manzana"
fruta2 = "Mango"
frutas = ["Manzana","Mango","Fresa"]"""

#Listas
"""
Listas = []
Permite cualquier tipo de datos
Son mutables: crecer, decrecer, agregar, cambiar, eliminar elementos
Son indexadas
"""
#Atributos
#len(), pop(), remove(), clear(), index(), del, sort(), reverse, extende(), zip()

"""deportes = ["futbol","tenis","basquetboll","voleibol","patinaje","natación"]
#cantidad de elementos de la lista: len()
print(len(deportes))

texto = "SebastianVilladaJaramillo"
print(len(texto))

#acceder algún deporte, ejemplo Voleibol
print(deportes[3])
print(deportes[-3])

#agregar deportes a la lista:
#append(elemento): insertar al final de la lista
deportes.append("atletismo")
print(deportes)
#insertar(indice, elemento): insertar en una posicion determinada
deportes.insert(2, "golf")
print(deportes)
#modificar o cambiar un deporte
deportes[2] = "esgrima"
print(deportes)"""
#crear 2 lista, una vacia y otra lista numerica. Validar que numeros son impares y agregalos a la lista vacia. Mostrar lista con los numeros impares

"""impares = []
numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,15,17,18,19,20]
print(len(numeros))

for n in numeros:
    if n % 2 !=0:
        impares.append(n)
print(impares)"""

#Eliminar elementos
#pop(indice): Elimina elementos en la posicion especificada
#pop(): elimina el ultimo elemento y muestra el elemento eliminado
#remove(elemento): elimna elemento pasado como argumento
#clear(): elimina los elementos de la lista
#del nombre_lista: elimina el objeto, es decir, la lista

#Conocer la posición de un elemento
"""deporte = ["futbol","tenis","basquetboll","voleibol","patinaje","natación"]
posicion = deporte.index("patinaje")
print(posicion)"""

#crear 2 listas, una vacia y una numerica, eliminar de la lista numerica los multiplos de 7 y almacenar en la lista los numeros eliminados. Mostrar las 2 listas, la de numeros eliminados y la numerica con los numeros restantes.

"""multiplos = []
numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,15,17,18,19,20,21]

for n in numeros:
    if n % 7 == 0:
        multiplos.append(n)
        numeros.remove(n)
print("Numeros eliminados: ", multiplos)
print("Lista: ", numeros)"""

#Organizar de forma ascendente y descendente: sort()
#(), reverse(), soporte(reverse=True)

"""num = [1,25,3,8,100,40,14,2,38,0,5,54]
#ascendente: de menor a mayor
num.sort()
print(num)
#descendente: de mayor a menor
num.sort(reverse=True)
print(num)

num.reverse()
print(num)

num.reverse()
print(num)"""