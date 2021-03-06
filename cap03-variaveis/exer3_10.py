#Programa que calcula aumento de um salário. Solicita o valor e a porcentagem e exibe resultado
wage = float(input("Digite o valor do salário R$: "))
percent = float(input("Digite o aumento percentual (%): "))

new_increase = wage * percent/100
new_wage = new_increase + wage
print(f"\nValor do aumento R$: {new_increase:5.2f}"
      f"\nNovo Salário R$: {new_wage:5.2f}")