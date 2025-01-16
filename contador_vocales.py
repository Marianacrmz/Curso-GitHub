# Se realizó este comentario para hacer un nuevo commit y realizar una prueba.
# Solicitar una oración al usuario
oracion = input("Por favor ingresa una oracion: ")

# Definir las vocales
vocales = "aeiouAEIOU"

# Contador de vocales
contador = 0

# Recorrer cada caracter de la oración
for caracter in oracion:
    if caracter in vocales:
        contador += 1

# Resultado
print(f"La oracion ingresada tiene {contador} vocales")
