##vocales

import string

def analizar_cadena(s):
    # Definir las vocales y los dígitos
    vocales = "aeiouAEIOU"
    digitos = "0123456789"
    vocales_count = 0
    consonantes_count = 0
    digitos_count = 0
    caracteres_especiales_count = 0
    conteo_caracteres = {}

    for char in s:
        if char.isalpha():
            if char in vocales:
                vocales_count += 1
            else:
                consonantes_count += 1
        elif char.isdigit():
            digitos_count += 1
        elif char in string.punctuation:
            caracteres_especiales_count += 1
        
        # Contar las ocurrencias de cada carácter
        conteo_caracteres[char] = conteo_caracteres.get(char, 0) + 1
    
    # Encontrar el carácter más frecuente
    char_mas_frecuente = max(conteo_caracteres, key=conteo_caracteres.get, default=None)
    
    return {s}
print( "vocales", vocales_count)
print("consonantes",consonantes_count)
print("digitos",digitos_count)
print("caracteres_especiales", caracteres_especiales_count)
print("caracter_mas_frecuente", char_mas_frecuente)

## desarrolado por Camilo Andres Suarez Fuentes TI1097784213