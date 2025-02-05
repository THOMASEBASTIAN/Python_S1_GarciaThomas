###hecho por Bastos_Thomas 
# Punto 2: Construya un programa tal que lea un número entero N,
# muestre la cantidad de términos y el resultado
# de la siguiente serie: 1 - 1/2 + 1/3 .... +- 1/n

# Leer la cantidad de términos
cantidad_terminos = int(input("Ingrese la cantidad de términos: "))
print("La cantidad de términos son:", cantidad_terminos)

# Validar si la cantidad de términos es menor o igual a 0
if cantidad_terminos <= 0:
    print(0)
else:
    # Inicializar la sumatoria
    sumatoria = 0
    
    # Calcular la serie
    for i in range(1, cantidad_terminos + 1):
        if i % 2 == 0:  # Si i es par, restar
            sumatoria -= 1 / i
        else:  # Si i es impar, sumar
            sumatoria += 1 / i
    
    # Mostrar el resultado
    print("La sumatoria dio:", sumatoria)

    ###hecho por Bastos_Thomas ·· c.c 1091358058