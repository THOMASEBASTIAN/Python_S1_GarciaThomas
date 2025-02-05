from gestion_json import guardar_datos, cargar_datos

def calcular_precio(inmueble):
    antiguedad = 2025 - inmueble['año']
    base = (inmueble['metros'] * 1000 + inmueble['habitaciones'] * 5000 + (15000 if inmueble['garaje'] else 0))
    precio = base * (1 - antiguedad / 100)
    if inmueble['zona'] == 'B':
        precio *= 1.5
    return round(precio, 2)

def inmuebless(inmuebles):
    try:
        año = int(input("Año: "))
        metros = int(input("Metros cuadrados: "))
        habitaciones = int(input("Número de habitaciones: "))
    except ValueError:
        print("Error: Ingresa valores numéricos válidos.")
        return
    
    garaje = input("¿Tiene garaje? (s/n): ").strip().lower() == 's'
    zona = input("Zona (A/B): ").strip().upper()

    if zona not in ('A', 'B'):
        print("Zona inválida. Debe ser 'A' o 'B'.")
        return

    inmuebles.append({'año': año, 'metros': metros, 'habitaciones': habitaciones, 'garaje': garaje, 'zona': zona})
    
    guardar_datos(inmuebles)


def listar_inmuebles(inmuebles):
    if not inmuebles:
        print("No hay inmuebles registrados.")
        return
    for i, inmueble in enumerate(inmuebles, 1):
        print(f"{i}. {inmueble}")

def actualizar_inmueble(inmuebles):
    listar_inmuebles(inmuebles)
    try:
        idx = int(input("Seleccione el número del inmueble a actualizar: ")) - 1
        if not (0 <= idx < len(inmuebles)):
            raise ValueError
        inmuebles[idx]['metros'] = int(input("Nuevos metros cuadrados: "))
        inmuebles[idx]['habitaciones'] = int(input("Nuevo número de habitaciones: "))
        inmuebles[idx]['garaje'] = input("¿Tiene garaje? (s/n): ").strip().lower() == 's'
        zona = input("Nueva zona (A/B): ").strip().upper()
        if zona in ('A', 'B'):
            inmuebles[idx]['zona'] = zona
        else:
            print("Zona inválida. No se realizaron cambios en la zona.")
        guardar_datos(inmuebles)
    except ValueError:
        print("Selección inválida.")

def eliminar_inmueble(inmuebles):
    listar_inmuebles(inmuebles)
    try:
        idx = int(input("Seleccione el número del inmueble a eliminar: ")) - 1
        if not (0 <= idx < len(inmuebles)):
            raise ValueError
        inmuebles.pop(idx)
        guardar_datos(inmuebles)
    except ValueError:
        print("Selección inválida.")

def buscar_por_presupuesto(inmuebles):
    try:
        presupuesto = float(input("Ingrese su presupuesto: "))
        resultado = [dict(inmueble, precio=calcular_precio(inmueble)) for inmueble in inmuebles if calcular_precio(inmueble) <= presupuesto]
        if not resultado:
            print("No hay inmuebles dentro del presupuesto.")
        else:
            print("Inmuebles dentro del presupuesto:")
            for r in resultado:
                print(r)
    except ValueError:
        print("Presupuesto inválido.")