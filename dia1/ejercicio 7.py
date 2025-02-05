# Algoritmo para verificar si dos números son amigos

# Leer el primer número
n1 = int(input("Ingresa n1: "))

# Leer el segundo número
n2 = int(input("Ingresa n2: "))

# Inicializar las sumas de los divisores
suma1 = 0
suma2 = 0

# Calcular la suma de los divisores propios de n1
for i in range(1, n1):
    if n1 % i == 0:
        suma1 += i

# Calcular la suma de los divisores propios de n2
for i in range(1, n2):
    if n2 % i == 0:
        suma2 += i

# Verificar si son números amigos
if suma1 == n2 and suma2 == n1:
    print(f"{n1} y {n2} son números parcercitos")
else:
    print(f"{n1} y {n2} no son números parcercitos")

    ### hecho por Bastos_Thomas cc 1091358058