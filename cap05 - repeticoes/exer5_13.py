divida = float(input("Valor total da dívida: "))
tx = float(input("Taxa de juros mensal (% a.m): "))
pgto_mensal = float(input("Valor mensal do pagamento: "))

mes = 1
if divida * (tx/100) > pgto_mensal:
    print("Sua dívida nunca poderá ser paga! Os juros são superiores ao pagamento mensal.")
else:
    saldo = divida
    juros_pagos = 0
    while saldo > pgto_mensal:
        juros = saldo * tx/100   #Juros é igual a dívida x taxa de juros
        saldo = saldo + juros - pgto_mensal
        juros_pagos = juros_pagos + juros
        print(f"Saldo da dívida no mês {mes}: R$ {saldo:6.2f}")
        mes = mes + 1

    print(f"\nTotal de meses para pagar: {mes - 1}")
    print(f"Total de juros pagos R${juros_pagos:7.2f} ")
    print(f"Saldo residual do último mês: R${saldo:8.2f}")

