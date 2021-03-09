print("***** TABUADA MALUCA *****")
n = int(input("Tabuada de: "))
inicio = int(input("Digite o valor inicial para a tabuada: "))
fim = int(input("Digite o valor final para a tabuada: "))

x = inicio
while x <= fim:
    print(f"{n} * {x} = {n * x}")
    x = x + 1