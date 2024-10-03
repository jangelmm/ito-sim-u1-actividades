'''
Se tiene una matriz de $n$ x $m$, donde las celdas pueden tomar dos posibles valores $\{0,1\}$.
Cada una de ellas cambiará su valor respecto a un tiempo discreto $(t)$ tomando en cuenta el valor de sus vecinos

- $1 =$ Viva
- $0 =$ Muerta
Reglas
1. Una celda viva seguirá viva si tiene $2$ o $3$ vecinas vivas.
2. Una celda viva morirá por sobrepoblación si tiene más de $3$ vecinas vivas.
3. Una celda viva morirá por soledad si tiene menos de $2$ vecinas vivas.
4. Una celda muerta vivirá si tiene exactamente $3$ vecinas vivas.
Programe el comportamiento de la matriz y ejecute durante un tiempo $T$.

|     |     |     |
| --- | --- | --- |
|     | P   |     |
|     |     |     |
'''
# Paquetes
from random import randint

def mostrarMatriz(matriz):
    for fila in matriz:
        print(fila)
    print()

def contarVecinos(matriz, fila, columna):
    vecinos = 0

    filas = len(matriz)
    columnas = len(matriz[0])

    # Itera sobre los vecinos alrededor de la celda actual genera las posiciones | -1 | 0 | 1 |
    for i in range(-1, 2):
        for j in range(-1, 2):

            if(i == 0 and j == 0):
                continue  # Ignora la propia celda ya que es la del centro
            else:
                # Calcular las coordenadas de la celda vecina
                fila_vecina = fila + i
                columna_vecina = columna + j

                # Verificar si las coordenadas de la celda vecina están dentro de los límites de la matriz True o False
                fila_dentro_limite = (0 <= fila_vecina < filas)
                columna_dentro_limite = (0 <= columna_vecina < columnas)

                # Si ambas coordenadas están dentro de los límites, sumar el valor de la celda vecina
                if fila_dentro_limite and columna_dentro_limite:
                    vecinos += matriz[fila_vecina][columna_vecina]

    return vecinos

# 1. Definir los parametros con los que trabajará la matriz

n = 3
m = 3
t = 2

# 2. Generar la matriz con valores aleatorios

matriz = []

for i in range(n):
    fila = []
    for j in range(m):
        fila.append(randint(0,1))
    matriz.append(fila)

print("Matriz Inicial")
mostrarMatriz(matriz)

# 3. Iterar t periodos de tiempo
for k in range(t):
    nueva_matriz = [fila[:] for fila in matriz]  # Crear una copia de la matriz actual

    # Iterar cada elemento de la matriz, para obtener la posición
    for i in range(n):
        for j in range(m):
            c = matriz[i][j]  # Valor de la celda actual
            vecinos = contarVecinos(matriz, i, j)  # Contar los vecinos vivos

            # Aplicar las reglas del juego de la vida
            if c == 1:
                if vecinos < 2 or vecinos > 3:
                    nueva_matriz[i][j] = 0  # La celda muere
            else:
                if vecinos == 3:
                    nueva_matriz[i][j] = 1  # La celda revive
    
    matriz = nueva_matriz  # Actualizar la matriz para el siguiente paso
    print(f"Tiempo: {k + 1}")
    mostrarMatriz(matriz)
