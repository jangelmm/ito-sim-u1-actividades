# Función para generar números aleatorios
def random(seed, iteration, max_digits):
    # Iterar
    for i in range (iteration):

        # Elevar al cuadrado
        seed = seed * seed

        #Extraer digitos centrales
        lon = len(str(seed))
        dif = lon - max_digits

        if(lon <= max_digits):
            print(seed)
            continue
            
        if(dif % 2 == 0):
            dif = dif // 2
        else:
            dif = (dif + 1) // 2

        seed = int(str(seed)[dif:-dif])
        print(seed)

    return seed

random(12, 15, 3)
        
