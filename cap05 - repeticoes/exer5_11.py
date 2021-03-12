print("****** POUPANÇA ******")
vlInicial = float(input("Valor inicial do depósito R$: "))
tx = float(input("Valor da taxa de juros mensal (%): "))

x = 1  #mês
saldo= vlInicial
while x <= 24:
    saldo = saldo + (saldo * (tx/100))
    print(f"Saldo do mês {x} é R$: {saldo:5.2f}")
    x = x + 1
print(f"Total de Ganho com juros no período: {saldo-vlInicial:7.2f}")
