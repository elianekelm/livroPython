print("**** APROVA EMPRÉSTIMO BANCÁRIO ****")
wage = float(input("Valor do salário bruto R$: "))
vl_casa = float(input("Valor da casa a comprar R$: "))
qt_anos = int(input("Quantidade de anos a pagar: "))

tempo = qt_anos * 12  #12 meses = 1 ano
vl_prestacao = vl_casa / tempo
if vl_prestacao <= wage * 3:
    print(f"\nParabéns, Empréstimo Aprovado! \nValor da Prestação mensal R$ {vl_prestacao:7.2f}")
else:
    print("\nInfelizmente seu empréstimo foi recusado. \n(Valor da prestação excede 30% do salário bruto.)")



