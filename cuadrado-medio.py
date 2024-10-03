# Función para generar números aleatorios
def random(seed, iteration, max_digits):
    # Iterar
    for i in range (iteration):

        # Elevar al cuadrado
        seed = seed * seed

        #Extraer digitos centrales
        lon = len(str(seed))
        dif = lon - max_digits

        if(dif % 2 == 0):
            dif = dif // 2
        else:
            dif = (dif + 1) // 2

        seed = int(str(seed)[dif:-dif])

    return seed
print(random(154, 3, 5))
        
