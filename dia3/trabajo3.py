import math


def clasificar_numero(n):
   if n < 0:
       return "El número debe ser no negativo."
  
   # Verificar si es par o impar
   par_impar = "par" if n % 2 == 0 else "impar"
  
   # Verificar si es primo o compuesto
   if n < 2:
       tipo = "no es primo ni compuesto"
   else:
       for i in range(2, int(math.sqrt(n)) + 1):
           if n % i == 0:
               tipo = "compuesto"
               break
       else:
           tipo = "primo"
  
   # Verificar si es un cuadrado perfecto
   raiz = int(math.sqrt(n))
   cuadrado_perfecto = "es un cuadrado perfecto" if raiz * raiz == n else "no es un cuadrado perfecto"
   return f"El número {n} es {par_impar}, {tipo}, y {cuadrado_perfecto}."


# Ejemplo de uso


numero =int(input("Escribe un numero"))
resultado = clasificar_numero(numero)
print(resultado)
### HECHO POR BASTOS_THOMAS / C.C 1091358058
