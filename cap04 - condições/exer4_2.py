print("\n***** VERIFICAÇÃO DE VELOCIDADE *****")
speed = float(input("Digite a velocidade do carro (Km/h): "))

if speed >= 80:
    multa = (speed - 80) * 5
    print(f"Multa R$ {multa:3.2f} - (Ultrapassar a velocidade permitida)")
else:
    print("Velocidade confirmada. Prossiga a viagem com cuidado.")