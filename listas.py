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

#Ejercicio de Listas
#Crea dos lista vacía llamada departamentos Colombia y la otra Capital, pida al usuario la cantidad de departamentos a ingresar, a través de un ciclo for pida al usuario que ingrese el departamento de Colombia que desee y su capital, agregue esta información a la lista y luego esta sea ordenada en orden descendente. a. Se debe imprimir la lista con los valores organizados de forma descendentes. b. Debe imprimir además los 2 últimos departamentos ingresados. c. Mostar los departamentos ingresados y su capital

departamentos_colombia = []
capitales = []

cantidad_departamentos = int(input("Ingrese la cantidad de departamentos a ingresar: "))

for i in range (cantidad_departamentos):
    departamento = input(f"Ingrese el nombre del departamento {i + 1} de Colombia: ")
    capital = input(f"Ingrese el nombre de la capital de {departamento} de Colombia: ")
    departamentos_colombia.append(departamento)
    capitales.append(capital)

print("\nLos 2 ultimos departamentos ingresados son: ", departamentos_colombia[-2:])
for departamento in departamentos_colombia[-2:]:
    print(departamento)

departamentos_colombia.sort(reverse=True)
capitales.sort(reverse=True)

print("\nLista de departamentos de Colombia en orden descendente: ") 
for departamento in departamentos_colombia:
    print(departamento)

print("\nLista de capitales de Colombia en orden descendente:")
for capital in capitales:
    print(capital)

print("\nDepartamentos ingresados y sus capitales")
for i in range(len(departamentos_colombia)):
    print(f"{departamentos_colombia[i]}:{capitales[i]}")