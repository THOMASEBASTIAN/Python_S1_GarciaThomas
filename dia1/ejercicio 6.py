# Empresa ACME
# Programa para calcular salarios, deducciones y estadísticas de empleados.

# Leer la cantidad de empleados
N = int(input("Ingrese la cantidad de empleados: "))

# Inicializar variables
totalBruto = 0
totalEPS = 0
totalPension = 0
totalNeto = 0

mayorSueldo = 0
menorSueldo = float('inf')  # Para asegurar que se actualice con el primer sueldo

nombreMayor = ""
nombreMenor = ""

# Iterar para cada empleado
for i in range(1, N + 1):
    print(f"\nIngrese el nombre del empleado {i}:")
    nombre = input()
    print("Ingrese las horas trabajadas:")
    horas = int(input())
    
    # Calcular salarios y deducciones
    bruto = horas * 20000
    eps = bruto * 0.04
    pension = bruto * 0.04
    neto = bruto - eps - pension

    # Acumular totales
    totalBruto += bruto
    totalEPS += eps
    totalPension += pension
    totalNeto += neto

    # Determinar mayor y menor sueldo
    if neto > mayorSueldo:
        mayorSueldo = neto
        nombreMayor = nombre
    if neto < menorSueldo:
        menorSueldo = neto
        nombreMenor = nombre

    # Imprimir datos del empleado
    print(f"Empleado: {nombre}")
    print(f"Sueldo Bruto: ${bruto}")
    print(f"EPS: ${eps}")
    print(f"Pensión: ${pension}")
    print(f"Sueldo Neto: ${neto}")

# Calcular promedios
promedioBruto = totalBruto / N
promedioNeto = totalNeto / N

# Imprimir resultados finales
print("\nResultados finales:")
print(f"Total Salarios Brutos: ${totalBruto}")
print(f"Total EPS: ${totalEPS}")
print(f"Total Pensión: ${totalPension}")
print(f"Total Salarios Netos: ${totalNeto}")
print(f"Empleado que más gana: {nombreMayor}, con un sueldo neto de ${mayorSueldo}")
print(f"Empleado que menos gana: {nombreMenor}, con un sueldo neto de ${menorSueldo}")
print(f"Promedio Salarios Brutos: ${promedioBruto}")
print(f"Promedio Salarios Netos: ${promedioNeto}")
### HECHO POR Bastos_Thomas / cc 1091358058