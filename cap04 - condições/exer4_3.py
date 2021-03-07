print("*** MAIOR? MENOR? ***")
num1 = float(input("Digite o 1° número: "))
num2 = float(input("Digite o 2° número: "))
num3 = float(input("Finalmente, digite o 3° número: "))

maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
else:
    if num3 > num1 and num3 > num2:
        maior = num3

menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
else:
    if num3 < num1 and num3 < num2:
        menor = num3

print(f"\nMaior: {maior} \nMenor: {menor}")
