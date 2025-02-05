def fibonacci(n):
    """G##Ejercicio 6: Serie de Fibonacci
enera la secuencia de Fibonacci hasta n términos."""
    sequence = [0, 1]
    for i in range(n - 2):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

def even_fibonacci(n):
    """Retorna solo los números pares de la secuencia de Fibonacci hasta n términos."""
    return [num for num in fibonacci(n) if num % 2 == 0]

def sum_fibonacci_range(start, end):
    """Calcula la suma de los números de Fibonacci dentro del rango especificado."""
    sequence = fibonacci(end)  # Obtener la secuencia hasta el límite superior
    return sum(num for num in sequence if start <= num <= end)





n_terms =int(input("Escribe un numero"))
print("Fibonacci:", fibonacci(n_terms))
print("Even Fibonacci:", even_fibonacci(n_terms))
print("Sum of Fibonacci in range (5, 50):", sum_fibonacci_range(5, 50))
