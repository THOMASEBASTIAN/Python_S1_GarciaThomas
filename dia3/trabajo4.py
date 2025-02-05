import random
import string

def contraseña_random(length=12, exclude_chars="", min_upper=1, min_lower=1, min_digits=1, min_symbols=1):
    """Genera una contraseña aleatoria con los requisitos dados."""
    
    # Definir los grupos de caracteres
    upper = [random.choice(string.ascii_uppercase) for _ in range(min_upper)]
    lower = [random.choice(string.ascii_lowercase) for _ in range(min_lower)]
    digits = [random.choice(string.digits) for _ in range(min_digits)]
    symbols = [random.choice(string.punctuation) for _ in range(min_symbols)]
    
    # Construir el conjunto de caracteres permitidos, excluyendo los especificados
    all_chars = set(string.ascii_letters + string.digits + string.punctuation) - set(exclude_chars)
    
    if not all_chars:
        raise ValueError("Todos los caracteres han sido excluidos. No se puede generar la contraseña.")
    
    # Calcular cuántos caracteres adicionales se necesitan
    remaining_length = length - (min_upper + min_lower + min_digits + min_symbols)
    
    if remaining_length < 0:
        raise ValueError("La longitud es demasiado corta para cumplir con los requisitos mínimos de caracteres.")
    
    # Seleccionar caracteres adicionales de la lista permitida
    remaining_chars = random.choices(list(all_chars), k=remaining_length)
    
    # Mezclar todos los caracteres y formar la contraseña
    password_list = upper + lower + digits + symbols + remaining_chars
    random.shuffle(password_list)
    
    return ''.join(password_list)

# Prueba del código
password = contraseña_random(length=16, exclude_chars="lIO0", min_upper=2, min_lower=2, min_digits=2, min_symbols=2)
print(password)
 ## hecho por Bastos_Thomas / 1091358058