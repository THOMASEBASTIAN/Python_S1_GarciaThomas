# Inicializar las variables para el número más grande y más pequeño
grande = None
pequeno = None

# Bucle para leer 10 números
for i in range(1, 11):
    numerito = int(input(f"Ingrese el número {i}: "))

    # Si es la primera iteración, inicializar grande y pequeño
    if grande is None or pequeno is None:
        grande = numerito
        pequeno = numerito
    else:
        # Actualizar el número más grande
        if numerito > grande:
            grande = numerito
        # Actualizar el número más pequeño
        if numerito < pequeno:
            pequeno = numerito

# Mostrar los resultados
print(f"Grande: {grande}")
print(f"Pequeño: {pequeno}")
##3 hecho por Bastos_Thomas  /cc 1091358058