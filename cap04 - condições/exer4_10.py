print("*** CÁLCULO ENERGIA ELÉTRICA ***")
qt_kw = int(input("Digite a quantidade de kWh consumida: "))
print("Tipo de instalação: \nR - Residencial \nI - Industrial \nC - Comercial")
tp_inst = input("Digite o tipo de instalação (R/I/C): ")

if tp_inst.upper() == "R":
    if qt_kw <= 500:
        price = 0.40
    else:
        price = 0.65
elif tp_inst.upper() == "C":
    if qt_kw <= 1000:
        price = 0.55
    else:
        price = 0.6
elif tp_inst.upper() == "I":
    if qt_kw <= 5000:
        price = 0.55
    else:
        price = 0.6
else:
    price = 0
    print("Tipo de instalação inválida! Tente novamente.")

vl_pagar = qt_kw * price
print(f"Valor a pagar R$: {vl_pagar:7.2f}")
