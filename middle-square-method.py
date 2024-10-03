# Librerias
import matplotlib.pyplot as plt
import pandas as pd

# Función para generar números aleatorios
def random(seed, iteration, max_digits):
    valores = []  # Lista para almacenar los números generados
    # Iterar
    for i in range (iteration):

        # Elevar al cuadrado
        seed = seed * seed

        #Extraer digitos centrales
        lon = len(str(seed))
        dif = lon - max_digits

        if(lon <= max_digits):
            #print(seed)
            continue
            
        if(dif % 2 == 0):
            dif = dif // 2
        else:
            seed = '0' + str(seed)
            dif = (dif + 1) // 2

        seed = int(str(seed)[dif:-dif])
        #print(seed)
        # Almacenar el número generado
        valores.append(seed)

    return valores
        
# Guardar los números aleatorios generados en una lista
valores = random(3708, 8, 4)

# Imprimir y graficar los resultados
print(valores)

# Opcional: graficar los resultados
plt.hist(valores, bins=20, edgecolor='black')
plt.title('Histograma de Números Generados')
plt.xlabel('Número')
plt.ylabel('Frecuencia')
plt.show()

# Crear un diagrama de dispersión
plt.scatter(range(len(valores)), valores, color='blue', alpha=0.5)  # Eje X: iteraciones, Eje Y: valores
plt.title('Diagrama de Dispersión de Números Generados')
plt.xlabel('Iteración')
plt.ylabel('Número Generado')
plt.grid(True)
plt.show()