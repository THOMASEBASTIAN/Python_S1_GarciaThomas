def ordenamiento_burbuja(arr, ascendente=True):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if (arr[j] > arr[j + 1]) == ascendente:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def ordenamiento_seleccion(arr, ascendente=True):
    n = len(arr)
    for i in range(n - 1):
        indice_extremo = i
        for j in range(i + 1, n):
            if (arr[j] < arr[indice_extremo]) == ascendente:
                indice_extremo = j
        arr[i], arr[indice_extremo] = arr[indice_extremo], arr[i]
    return arr

def ordenamiento_insercion(arr, ascendente=True):
    n = len(arr)
    for i in range(1, n):
        clave = arr[i]
        j = i - 1
        while j >= 0 and (arr[j] > clave) == ascendente:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = clave
    return arr

# Solicitar entrada del usuario
entrada = input("Ingrese una lista de números separados por comas: ")
arreglo = [int(x) for x in entrada.split(',')]

# Imprimir resultados de los diferentes métodos de ordenamiento
print("Ordenación por burbuja ascendente:", ordenamiento_burbuja(arreglo.copy(), ascendente=True))
print("Ordenación por burbuja descendente:", ordenamiento_burbuja(arreglo.copy(), ascendente=False))
print("Ordenación por selección ascendente:", ordenamiento_seleccion(arreglo.copy(), ascendente=True))
print("Ordenación por selección descendente:", ordenamiento_seleccion(arreglo.copy(), ascendente=False))
print("Ordenación por inserción ascendente:", ordenamiento_insercion(arreglo.copy(), ascendente=True))
print("Ordenación por inserción descendente:", ordenamiento_insercion(arreglo.copy(), ascendente=False))

## HECHO POR BASTOS_THOMAS/C.C 1091358058