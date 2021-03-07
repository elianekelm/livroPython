print("*** CÁLCULO AUMENTO SALARIAL ***")
wage = float(input("Digite o valor do salário atual: "))

pc_aumento = 0.15

if wage > 1250:
    pc_aumento = 0.1

aumento_wage = wage * pc_aumento
print(f"Aumento salarial: ({pc_aumento * 100}%) R$:{aumento_wage:5.2f}")