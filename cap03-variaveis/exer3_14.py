#Pergunta qtdade de km percorrido por carro aludado, qt dias. Calcule o preço a pagar
#Custo: 60,00 por dia e 0,15 por km rodado
print("***********ALUGUEL DE VEÍCULO **********")
qt_km = int(input("Quantidade de km(s) percorridos com o veículo: "))
qt_dias = int(input("Quantidade de dias: "))

vl_pagar = (qt_dias * 60) + (qt_km * 0.15)

print(f"Valor a pagar R$: {vl_pagar:5.2f}")