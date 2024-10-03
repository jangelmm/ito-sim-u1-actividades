# Librerias
import matplotlib.pyplot as plt
import pandas as pd

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
            #print(seed)
            continue
            
        if(dif % 2 == 0):
            dif = dif // 2
        else:
            dif = (dif + 1) // 2

        seed = int(str(seed)[dif:-dif])
        #print(seed)

    return seed
        
# Guardar los numéros aleatorios generados en una lista

valores = []

for i in range (400):
    valores.append(random(154, i, 4))

print(valores)

# Crear gráfico de frecuencias

# Crear un DataFrame a partir de la lista
df = pd.DataFrame(valores, columns=['Numeros'])

# Calcular la frecuencia de cada número
frecuencias = df['Numeros'].value_counts().sort_index()

# Graficar el gráfico de frecuencias
plt.figure(figsize=(10, 6))
frecuencias.plot(kind='bar', color='skyblue')

# Personalizar el gráfico
plt.title('Gráfico de Frecuencias')
plt.xlabel('Números')
plt.ylabel('Frecuencia')
plt.xticks(rotation=0)  # Rotar las etiquetas del eje x
plt.grid(axis='y')  # Añadir una cuadrícula en el eje y

# Mostrar el gráfico
plt.show()