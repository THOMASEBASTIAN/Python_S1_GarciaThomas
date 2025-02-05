#Ejercicio 7: Factorial y combinaciones

import math

def factorial(n):
    """Calcula el factorial de un número manejando casos negativos."""
    if n < 0:
        return "Factorial no definido para números negativos"
    return math.factorial(n)

def combinations(n, r):
    """Calcula combinaciones (nCr)."""
    if n < 0 or r < 0 or r > n:
        return "Valores no válidos"
    return factorial(n) // (factorial(r) * factorial(n - r))

def permutations(n, r):
    """Calcula permutaciones (nPr)."""
    if n < 0 or r < 0 or r > n:
        return "Valores no válidos"
    return factorial(n) // factorial(n - r)

# Solicitar entrada del usuario
n = int(input("Ingrese el valor de n: "))
r = int(input("Ingrese el valor de r: "))

print(f"Factorial de {n}: {factorial(n)}")
print(f"Combinaciones de {n} tomados de {r} en {combinations(n, r)}")
print(f"Permutaciones de {n} tomados de {r} en {permutations(n, r)}")
