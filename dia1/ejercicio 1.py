######################################3
### NUMEROS DIVISIBLES POR 3 Y 7 ENTRE 1 Y 100
#########################################



# Programa para encontrar números divisibles por 3 y 7 entre 1 y 1000
print("Números divisibles por 3 y 7 entre 1 y 1000:")

# Recorremos los números del 1 al 1000
for num in range(1, 1001):
    # Verificamos si el número es divisible por 3 y por 7
    if num % 3 == 0 and num % 7 == 0:
        print(num)

###Elaborado por Bastos_Thomas c.c 1.091.358.058