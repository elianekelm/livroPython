valor_pagar = 0
while True:
    codigo_prod = int(input("Digite o código do produto: "))
    preco = 0
    if codigo_prod == 0:
        break
    elif codigo_prod == 1:
        preco = 0.5
    elif codigo_prod == 2:
        preco = 1.00
    elif codigo_prod == 3:
        preco = 4.00
    elif codigo_prod == 5:
        preco = 7.00
    elif codigo_prod == 9:
        preco = 8.00
    else:
        print("Código Inválido!")

    if preco != 0:
        qtdade = int(input("Quantidade: "))
        valor_pagar = valor_pagar + (preco * qtdade)

print(f"Total a pagar R$ {valor_pagar:5.2f}")