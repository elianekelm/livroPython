#Calcular tempo de uma viagem de carro. Input: distancia; velocidade média
import math
km = float(input("Qual a distância total (km) até o destino: "))
speed = float(input("Qual a velocidade média esperada (km/h): "))

tempo = km / speed
total_seg = tempo * 3600   #converte de horas para segundos
horas = math.floor(total_seg/3600) #parte inteira
total_seg = (total_seg % 3600)   # o resto
min = math.floor(total_seg/60)    # minutos é igual a parte inteira dividido por 60
seg = (total_seg % 60)             #segundos é o resto

print(f"Tempo total estimado para essa viagem: {horas}:{min}:{seg:2.0f} ")