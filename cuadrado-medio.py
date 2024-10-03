# Librerias
import matplotlib.pyplot as plt
import pandas as pd

# Función para generar números aleatorios
def random(seed, iteration, max_digits):
    valores = []  # Lista para almacenar los números generados
    val1 = []
    val2 = []

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
            aux1 = int(str(seed)[dif+1:-dif])
            seed = int(str(seed)[dif:-dif-1])
        else:
            dif = (dif + 1) // 2
            aux1 = 0
            seed = int(str(seed)[dif:-dif])

        
        #print(seed)
        # Almacenar el número generado
        val1.append(seed)
        val2.append(aux1)
    valores.append(val1)
    valores.append(val2)
    return valores
        
# Guardar los números aleatorios generados en una lista
valores = random(154, 12, 4)

# Imprimir y graficar los resultados
print(valores[0])
print(valores[1])

# Opcional: graficar los resultados val1 
plt.hist(valores[0], bins=20, edgecolor='black')
plt.title('Histograma de Números Generados (val1)')
plt.xlabel('Número')
plt.ylabel('Frecuencia')
plt.show()

# Crear un diagrama de dispersión val1
plt.scatter(range(len(valores[0])), valores[0], color='blue', alpha=0.5)  # Eje X: iteraciones, Eje Y: valores
plt.title('Diagrama de Dispersión de Números Generados (val1)')
plt.xlabel('Iteración')
plt.ylabel('Número Generado')
plt.grid(True)
plt.show()

# Opcional: graficar los resultados val2
plt.hist(valores[1], bins=20, edgecolor='black')
plt.title('Histograma de Números Generados (val2)')
plt.xlabel('Número')
plt.ylabel('Frecuencia')
plt.show()

# Crear un diagrama de dispersión val2
plt.scatter(range(len(valores[1])), valores[1], color='blue', alpha=0.5)  # Eje X: iteraciones, Eje Y: valores
plt.title('Diagrama de Dispersión de Números Generados (val2)')
plt.xlabel('Iteración')
plt.ylabel('Número Generado')
plt.grid(True)
plt.show()