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
#Crear una agenda donde se almacene los nombres y números de telefono de los compañeros del curso. Debe mostrar al usuario un menú con las siguientes acciones:

# Agregar/Cambiar: pide nombre del compañero, si el nombre se encuentra debe mostrar el teléfono y si el teléfono es incorrecto debe permitir cambiarlo. OK
# Si el nombre no se encuentra debe permitir agregarlo. OK
# Buscar: nos pide una cadena de caracteres y nos muestra todos los contactos que coincidan con esta. (utilizar el método startswith) OK
# Eliminar: pide un nombre, si este existe debe preguntar si desea eliminarlo.
# Mostrar ítems: muestra todos los contactos con sus respectivos números.
# Salir: cerrar agenda
# Otra opción por si el usuario escoge una opción distinta a las incluidas en el menú

agenda = {}

while True:
    print("\nAgenda\n"+
          "1. Agregar\n"+
          "2. Buscar\n"+
          "3. Elimiar\n"+
          "4. Mostrar\n"+
          "5. Salir")
    opcion = input("Seleccion una opción: ")
    
    if opcion == "1":
        nombre_estudiante = input("Ingrese el nombre del compañero: ")
        if nombre_estudiante in agenda:
            print("Nombre encontrado, télefono actual: ", agenda[nombre_estudiante])
            cambio = input("¿Desea cambiar el télefono? (s/n): ")
            if cambio.lower() == "s":
                agenda[nombre_estudiante] = input("Ingrese el nuevo número de télefono: ")
        else:
            agenda[nombre_estudiante] = input("Ingrese el número de télefono: ")
    
    elif opcion == "2":
        buscar = input("Ingrese el nombre a buscar: ")
        for nombre_estudiante, telefono in agenda.items():
            if nombre_estudiante.startswith(buscar):
                print("Búsqueda encontrada: \n", "Nombre Estudiante: " , nombre_estudiante, "\n Teléfono Estudiante: ", telefono)
            else:
                print(f"{nombre_estudiante} no existe")
    
    elif opcion == "3":
        nombre_estudiante = input("Ingrese el nombre a borrar: ")
        if nombre_estudiante in agenda:
            confirmacion = input(f"Desea borrar el contacto de {nombre_estudiante} s/n: ")
            if confirmacion.lower() == "s":
                del agenda[nombre_estudiante]
                print(f"{nombre_estudiante} eliminado")
            else:
                print(f"{nombre_estudiante} no encontrado")
    
    elif opcion == "4":
        for nombre_estudiante, telefono in agenda.items():
            print("Datos almacenados: \n", "Nombre Estudiante: " , nombre_estudiante, "\n Teléfono Estudiante", telefono)
        else:
            print("No hay datos almacenados")
    
    elif opcion == "5":
        print("Saliendo...")
        break
    
    else:
        print("Opción no válida. Intentan nuevamente...")