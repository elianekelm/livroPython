print("**** CALCULADORA ****")
num1 = float(input("Digite o 1° número: "))
num2 = float(input("Digite o 2° número: "))

print("\n1 - Adição \n2 - Subtração \n3 - Multiplicação \n4 - Divisão")
tipo_op = int(input("Escolha uma operação (1/2/3/4): "))

if tipo_op == 1:
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif tipo_op == 2:
    result = num1 - num2
    print(f"{num1} - {num2} = {result:5.2f}")
elif tipo_op == 3:
    result = num1 * num2
    print(f"{num1} * {num2} = {result:5.2f}")
elif tipo_op == 4:
    result = num1 / num2
    print(f"{num1} / {num2} = {result:5.2f}")
else:
    print("Operação inválida, tente novamente!")
