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
    
    elif opcion == "5":
        print("Saliendo...")
        break
    
    else:
        print("Opción no válida. Intentan nuevamente...")