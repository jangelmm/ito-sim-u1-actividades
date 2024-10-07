import matplotlib.pyplot as plt
import pandas as pd

# Función para generar números aleatorios
def random(seed, iteration, max_digits):
    valores = [] # Lista que contendrá las listas a retornar
    val1 = []
    val2 = []

    print(f"| {'n'.center(4)} | {'R(n)'.center(8)} | {'R(n)^2'.center(12)} | {'M.R(n)^2'.center(10)} | {'val1'.center(6)} | {'val2'.center(6)} |")
    print("-" * 62)  # Línea separadora

    for i in range (iteration):
        rn = seed

        # Elevar al cuadrado
        seed = seed ** 2
        rn2 = seed

        #Extraer digitos centrales
        lon = len(str(seed))
        dif = lon - max_digits

        if(lon <= max_digits):
            continue
        if(dif % 2 == 0):
            dif = dif // 2

            mr = int(str(seed)[dif:-dif])
            aux1 = int(str(seed)[dif+1:-dif])
            seed = int(str(seed)[dif:-dif-1])
        else:
            dif = (dif + 1) // 2

            mr = int(str(seed)[dif:-dif])
            aux1 = 0
            seed = int(str(seed)[dif:-dif])

        # Almacenar el número generado
        val1.append(seed)
        val2.append(aux1)

        # Imprimir en forma de tabla
        print(f"| {str(i).center(4)} | {str(rn).center(8)} | {str(rn2).center(12)} | {str(mr).center(10)} | {str(seed).center(6)} | {str(aux1).center(6)} |")
    
    valores.append(val1)
    valores.append(val2)
    return valores

# Guardar las temperaturas
temperaturas = []

numeros = random(6832, 200, 4)
