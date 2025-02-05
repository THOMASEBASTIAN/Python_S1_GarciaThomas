nombres = [
    ["Adrián"],
    ["Alejandra"],
    ["Ámbar", "Isabella"],
    ["Andrés", "David"],
    ["Aura", "Camila"],
    ["Camilo", "Andrés"],
    ["Daniel", "Esteban"],
    ["David", "Santiago"],
    ["Edgar", "Leonardo"],
    ["Gerson", "Steven"],
    ["Harley", "Yefrey"],
    ["John", "Stiven"],
    ["Juan", "David"],
    ["Juan", "David"],
    ["Juan", "David"],
    ["Juan", "Eduardo"],
    ["Juan", "Fernando"],
    ["Juan", "Jose"],
    ["Maria", "Juliana"],
    ["Mateo", "Roman"],
    ["Naya", "Zarela"],
    ["Nicolas"],
    ["Omar", "Fernando"],
    ["Santiago"],
    ["Santiago", "Andrés"],
    ["Santiago"],
    ["Sara", "Sofía"],
    ["Sayara", "Yurley"],
    ["Sergio", "Andrés"],
    ["Simón", "Dante"],
    ["Thomas", "Sebastián"],
    ["Vladimir"]
]

apellidos = [
    ["Quintero", "Pinzón"],
    ["Pinzón", "Alvarez"],
    ["Plata", "López"],
    ["Reyes", "Espinel"],
    ["Pico", "Araque"],
    ["Suárez", "Fuentes"],
    ["Guerrero", "Quintero"],
    ["Vera", "Mendez"],
    ["Acevedo", "Arteaga"],
    ["Chaparro", "Martínez"],
    ["Cabrales", "Vargas"],
    ["Negron", "Regalado"],
    ["Saavedra", "Jaimez"],
    ["Santoyo", "Jaimes"],
    ["Vargas", "Soto"],
    ["Pinilla", "Guzmán"],
    ["Umaña", "Barragan"],
    ["Abril", "Roman"],
    ["Saavedra", "Mejia"],
    ["Camargo"],
    ["Lizcano", "Jaimes"],
    ["Chedraui", "Mantilla"],
    ["Granados", "Parra"],
    ["Aguilar", "Vesga"],
    ["Quiñonez", "Sosa"],
    ["Jaimes", "Perez"],
    ["Díaz", "Rodríguez"],
    ["Aparicio", "Arciniegas"],
    ["Rueda", "Hernández"],
    ["Salamanca", "Galvis"],
    ["Bastos", "Garcia"],
    ["Diaz", "Contreras"]
]

def mostrar_estudiantes():
    print("\nLista de estudiantes:")
    for i in range(len(nombres)):
        print(f"{i}: Nombres: {nombres[i]} | Apellidos: {apellidos[i]}")

def agregar_estudiante():
    nuevos_nombres = input("Ingresa los nombres del nuevo estudiante (sepáralos por comas si son varios): ")
    nuevos_apellidos = input("Ingresa los apellidos del nuevo estudiante (sepáralos por comas si son varios): ")
    nombres.append([n.strip() for n in nuevos_nombres.split(",")])
    apellidos.append([a.strip() for a in nuevos_apellidos.split(",")])
    print("\n¡Estudiante agregado con éxito!")

def editar_estudiante():
    mostrar_estudiantes()
    indice = int(input("\nIngresa el índice del estudiante que deseas editar (0 a {}): ".format(len(nombres) - 1)))
    if 0 <= indice < len(nombres):
        nuevos_nombres = input("Ingresa los nuevos nombres (sepáralos por comas si son varios): ")
        nombres[indice] = [n.strip() for n in nuevos_nombres.split(",")]
        nuevos_apellidos = input("Ingresa los nuevos apellidos (sepáralos por comas si son varios): ")
        apellidos[indice] = [a.strip() for a in nuevos_apellidos.split(",")]
        print("\n¡Estudiante editado con éxito!")
    else:
        print("Índice no válido. Por favor, ingresa un índice dentro del rango.")

def eliminar_estudiante():
    mostrar_estudiantes()
    indice = int(input("\nIngresa el índice del estudiante que deseas eliminar (0 a {}): ".format(len(nombres) - 1)))
    if 0 <= indice < len(nombres):
        nombres.pop(indice)
        apellidos.pop(indice)
        print("\n¡Estudiante eliminado con éxito!")
    else:
        print("Índice no válido. Por favor, ingresa un índice dentro del rango.")

def menu():
    while True:
        print("\n--- Menú de Acciones ---")
        print("1. Ver estudiantes")
        print("2. Agregar estudiante")
        print("3. Editar estudiante")
        print("4. Eliminar estudiante")
        print("5. Salir")
        opcion = input("Selecciona una opción (1-5): ")

        if opcion == "1":
            mostrar_estudiantes()
        elif opcion == "2":
            agregar_estudiante()
        elif opcion == "3":
            editar_estudiante()
        elif opcion == "4":
            eliminar_estudiante()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 5.")

# Ejecutar el menú
menu()