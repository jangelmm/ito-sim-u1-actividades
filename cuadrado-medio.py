# Función para generar números aleatorios
def random(seed, iteration):
    # Iterar
    for i in range (iteration):

        # Elevar al cuadrado
        seed = seed * seed

        #Extraer digitos centrales
        val = int(str(seed)[1:-1])

        seed = val
    return seed

print(random(76, 7))
        
