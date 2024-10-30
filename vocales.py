# Pedimos la frase al usuario
frase = input("Por favor, ingresa una frase: ") 

# Inicializamos el contador de vocales y el arreglo para almacenarlas
vocales_encontradas = []
contador_vocales = 0

# Definimos las vocales
vocales = "aeiouAEIOU"

# Recorremos cada letra en la frase
for letra in frase:
    # Verificamos si la letra es una vocal
    if letra in vocales:
        vocales_encontradas.append(letra)
        contador_vocales += 1

# Mostramos los resultados
print("Cantidad de vocales encontradas:", contador_vocales)
print("Vocales específicas encontradas:", vocales_encontradas)
