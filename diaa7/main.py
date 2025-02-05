# main.py

from estudiante import mostrar_estudiantes, agregar_estudiante, editar_estudiante, eliminar_estudiante

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