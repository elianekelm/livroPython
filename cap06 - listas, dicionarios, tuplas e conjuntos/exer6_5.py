último = 10
fila = list(range(1, último+1))
while True:
    print(f"\nClientes na fila: {len(fila)} ")
    print("Fila atual:", fila)
    print("Digite: \nF - Adicionar cliente na fila \nA - Atender cliente \nS - Sair")
    operação = input("Operação (F, A ou S):")
    x = 0
    sair = False
    while x < len(operação):
        if operação[x] == "A":
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} atendido")
            else:
                print("Fila vazia! Ninguém para atender.")
        elif operação[x] == "F":
            último += 1  # Incrementa o ticket do novo cliente
            fila.append(último)
        elif operação[x] == "S":
            sair = True
            break
        else:
            print(f"Operação inválida: {operação[x]} na posição {x}! Digite apenas F, A ou S!")
        x = x + 1
    if sair:
        break