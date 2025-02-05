from gestion_inmuebles import inmuebless, listar_inmuebles, actualizar_inmueble, eliminar_inmueble, buscar_por_presupuesto
from gestion_json import cargar_datos

def menu():
    inmuebles = cargar_datos()
    while True:
        print("\n1. Agregar inmueble")
        print("2. Listar inmuebles")
        print("3. Actualizar inmueble")
        print("4. Eliminar inmueble")
        print("5. Buscar por presupuesto")
        print("6. Salir")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == '1':
            inmuebless(inmuebles)
        elif opcion == '2':
            listar_inmuebles(inmuebles)
        elif opcion == '3':
            actualizar_inmueble(inmuebles)
        elif opcion == '4':
            eliminar_inmueble(inmuebles)
        elif opcion == '5':
            buscar_por_presupuesto(inmuebles)
        elif opcion == '6':
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu()
