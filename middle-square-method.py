import matplotlib.pyplot as plt
import pandas as pd

# Función para generar números aleatorios
def random(seed, iteration, max_digits):
    valores = []  # Lista para almacenar los números generados
    for _ in range(iteration):
        # Elevar al cuadrado
        seed = seed * seed
        
        # Extraer dígitos centrales
        lon = len(str(seed))
        dif = lon - max_digits
        
        # Asegúrate de no cortar la secuencia prematuramente
        if dif < 0:
            # Si la longitud es menor que max_digits, ajustar dif
            dif = 0
        
        # Ajustar el índice para la extracción
        start = dif // 2
        seed = int(str(seed)[start:start + max_digits])  # Extraer max_digits
        
        # Almacenar el número generado
        valores.append(seed)

    return valores

# Guardar los números aleatorios generados en una lista
valores = random(154, 100, 4)

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