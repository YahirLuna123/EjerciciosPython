# Programa para contar repeticiones de una letra en una frase
# Modificado para la Práctica 3 - Gestión de la Configuración

frase = input("Ingresa una frase: ")
letra = input("Ingresa una letra: ")

# Convertimos ambos a minúsculas para una búsqueda exacta 
# (Estándar de calidad en procesamiento de texto)
frase_min = frase.lower()
letra_min = letra.lower()

contador = 0

for caracter in frase_min:
    if caracter == letra_min:
        contador += 1

print(f"\nResultado:")
print(f"En la frase: '{frase}'")
print(f"La letra '{letra}' aparece {contador} veces.")


print("Finalizado por Yahir Luna - Local").
