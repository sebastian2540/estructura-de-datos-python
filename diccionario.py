#Diccionarios
"""
dic = {}
diccionarios almacen la información o cada elemento
dicc = {clave:valor}
clave: únicas, necesarios para acceder a un elemento o valor.
Las claves pueden tener 1 o varios valores.
Dinamicos: crecer o decrecer
"""

"""datos = {
    "nombre":"Karina",
    "apellido":"Valencia",
    "edad":"15",
    "sexo":"F"
}"""

"""datos_personales = dict(
    nombre = "Pepito",
    apellido = "Perez",
    edad = 39,
    sexo = "M"
)

print(type(datos_personales))"""

#Acceder a un valor
"""print(datos["edad"])"""
#get()
"""print(datos.get("edad"))"""
#Modificar un valor
"""datos["edad"]  = 39
print(datos)"""
#Modificar clave inexistente en el diccionario
"""datos["fecha_nac"] = "01-01-1984"
print(datos)"""
#Eliminar elementos:
#popitem(): elimina el ultimo elemento del diccionario insertado
"""datos.popitem()
print(datos)"""
#clear(): elimina todos los elementos del diccionario
"""datos.clear()
print(datos)"""
#pop(): elimina el elemento que contiene la clave pasada como argumento
"""datos.pop("edad")
print(datos)"""

#Crear un diccionario vacio, solicitar al usuario que ingrese la cantidad de elementos y la información que usted desee, validar si alguna clave ya existe debe mostrar el respectivo mensaje, de lo contrario debe ingresar el elemento.

"""vehiculo = {}
cantidad = int(input("Ingrese la cantidada de marcas: "))

for marca in range(cantidad):
    marca = input("Ingrese el nombre del vehículo: ")
    if marca in vehiculo:
        print(f"La marca {marca} ya existe en el elemento")
    else:
        precio = int(input(f"Ingrese el precio de la {marca}: "))
        vehiculo[marca] = precio
print(vehiculo)"""
#Obtener las claves del diccionario: keys()
datos = {
    "nombre":"Karina",
    "apellido":"Valencia",
    "edad":"15",
    "sexo":"F"
}

"""for clave in datos.keys():
    print(clave)
print("--------------")
for c in datos:
    print(c)
"""
#obtener solos los valores del diccionario: values()
"""print("Con metodo")
for valor in datos.values():
    print(valor)
print("--------------")
print("Sin metodo")
for v in datos:
    print(datos[v])"""

#Obtener claves y valores: items()

"""for clave, valor in datos.items():
    print(f"{clave}={valor}")"""

#Ejercicio de Diccionario