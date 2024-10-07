# Librerias
import matplotlib.pyplot as plt
import pandas as pd
import math

# Función para generar números aleatorios
def random(seed, iteration, max_digits):
    valores = []

    #print(f"| {'n'.center(4)} | {'R(n)'.center(8)} | {'R(n)^2'.center(12)} | {'M.R(n)^2'.center(10)} | {'valores'.center(6)} | {'val2'.center(6)} |")
    #print("-" * 62)  # Línea separadora

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
        # print(f"| {str(i).center(4)} | {str(rn).center(8)} | {str(rn2).center(12)} | {str(mr).center(10)} | {str(seed).center(6)} | {str(aux1).center(6)} |")
    
    return valores

def cal_media(lista):
    return sum(lista) / len(lista)

def cal_mediana(lista):
    lo = sorted(lista)
    n = len(lista)
    if n % 2 == 0:
        mediana = (lo[n//2 - 1] + lo[n//2]) / 2
    else:
        mediana = lo[n//2]
    return mediana

def cal_maximo(lista):
    return max(lista)

def cal_minimo(lista):
    return min(lista)

def cal_desviacion_estandar(lista):
    media = cal_media(lista)
    sumdc = sum((x - media) ** 2 for x in lista)
    varianza = sumdc / len(lista)
    desviacion_estandar = math.sqrt(varianza)
    return desviacion_estandar

valores = random(339917332563, 3650, 9)

temperaturas = []

for i in range(len(valores)):
    if len(temperaturas) >= 365: 
        break
    
    numero = str(valores[i])
    
    pdi = int(numero[0])
    sig = 1 if pdi % 2 == 0 else -1
     
    sdi = int(numero[1])
    decimales = 2 if sdi % 2 == 0 else 1
    
    udi = int(numero[-2:]) 

    if 20 <= udi <= 40:
        
        if decimales == 2:
            temperatura = udi * sig  
        else:
            udi = int(str(udi)[-1])
            temperatura = udi * sig
        
        if temperatura < -20:
            temperatura = abs(temperatura)
        
        if temperatura != '':
            temperaturas.append(temperatura)

print("Temperaturas Generadas: ")
print("\n")
print(temperaturas)

media = cal_media(temperaturas)
mediana = cal_mediana(temperaturas)
maximo = cal_maximo(temperaturas)
minimo = cal_minimo(temperaturas)
desviacion_estandar = cal_desviacion_estandar(temperaturas)

# Imprimir los resultados en formato de tabla
print("\n")
print("| Cálculo               | Resultado           ")
print("|-----------------------|---------------------")
print(f"| Media                 | {media}          ")
print(f"| Mediana               | {mediana}        ")
print(f"| Máximo                | {maximo}             ")
print(f"| Mínimo                | {minimo}             ")
print(f"| Desviación Estándar   | {desviacion_estandar} ")