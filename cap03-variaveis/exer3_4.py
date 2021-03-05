salario = float(input("Digite o valor do seu salário R$: "))

pagar_imposto = salario > 1200

if salario < 1200:
    print("Devido ao valor do seu salário você não precisa pagar imposto!")
else:
    print("Fique atento, você precisa pagar imposto.")