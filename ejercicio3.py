# Librerias
import matplotlib.pyplot as plt
import pandas as pd
import math

# Función para generar números aleatorios
def random(seed, iteration, max_digits):
    valores = []

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

valores = random(339917332563, 3650, 9)

inversiones = []

for i in range(len(valores)):
    if len(inversiones) >= 100: 
        break
    
    numero = str(valores[i])
    
    pdi = int(numero[0])
    sig = 1 if pdi % 2 == 0 else -1  # Signo positivo si pdi es par, negativo si es impar
     
    sdi = int(numero[1])
    decimales = 2 if sdi % 2 == 0 else 1  # Decimales a usar dependiendo del segundo dígito

    tdi = int(numero[2:4])
    dec = round(tdi * 0.01, 2)  # Limitamos el valor decimal a dos dígitos
    
    udi = int(numero[-2:])  # Últimos dos dígitos del número

    if 5 <= udi <= 10:  # Sólo consideramos valores entre 5 y 10
        
        if decimales == 2:
            inversion = round(udi * sig + dec, 2)  # Calculamos la inversión con 2 decimales
        else:
            udi = int(str(udi)[-1])  # Tomamos el último dígito si sólo es un decimal
            inversion = round(udi * sig + dec, 2)
        
        # Si la inversión es menor a -5, la corregimos
        if inversion < -5:
            inversion = round(abs(inversion) + dec, 2)
        
        # Nos aseguramos de que esté en el rango deseado (-5 a 10)
        if -5 <= inversion <= 10:
            inversiones.append(inversion)

print(inversiones)
