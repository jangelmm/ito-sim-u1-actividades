# Librerias
import matplotlib.pyplot as plt
import pandas as pd

# Función para generar números aleatorios
def random(seed, iteration, max_digits):
    valores = []

    print(f"| {'n'.center(4)} | {'R(n)'.center(8)} | {'R(n)^2'.center(12)} | {'M.R(n)^2'.center(10)} | {'valores'.center(6)} | {'val2'.center(6)} |")
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
        valores.append(seed)

        # Imprimir en forma de tabla
        print(f"| {str(i).center(4)} | {str(rn).center(8)} | {str(rn2).center(12)} | {str(mr).center(10)} | {str(seed).center(6)} | {str(aux1).center(6)} |")
    
    return valores
        
# Guardar los números aleatorios generados en una lista
valores = random(339917332563, 3650, 9)

# Opcional: graficar los resultados valores 
plt.hist(valores, bins=20, edgecolor='black')

plt.title('Histograma de Números Generados (valores)')
plt.xlabel('Número')
plt.ylabel('Frecuencia')
plt.show()

# Crear un diagrama de dispersión valores
plt.scatter(range(len(valores)), valores, color='blue', alpha=0.5)  # Eje X: iteraciones, Eje Y: valores
plt.title('Diagrama de Dispersión de Números Generados (valores)')
plt.xlabel('Iteración')
plt.ylabel('Número Generado')
plt.grid(True)
plt.show()
