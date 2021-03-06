#Escreva um programa que leia a quantidade de dias/horas/min/seg.
#Calcule tudo em segundos
dias = int(input("Digite a quantidade de dias: "))
horas = float(input("Digite a quantidade de horas: "))
min = int(input("Digite a quantidade de minutos: "))
seg = int(input("Digite a quantidade de segundos: "))

total_seg = (dias * 24 * 3600) + (horas * 3600) + (min * 60) + seg

print(f"Tempo total em segundos: \n{dias} dia(s), {horas:2.0f}:{min}:{seg} equivale a {total_seg} segundos.")