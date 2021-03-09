print("****** PRODUTO COM SOMA *****")
num1 = int(input("Digite o 1° número: "))
num2 = int(input("Digite o 2° número: "))
x = 1
r = 0
while x <= num2:
    r = r + num1
    x = x + 1
print(f"{num1} x {num2} = {r}")