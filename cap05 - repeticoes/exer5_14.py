qt_num = 0
soma = 0
while True:
    num = int(input("Digite um número inteiro ou 0 para sair: "))
    if num == 0:
        break
    soma += num
    qt_num = qt_num + 1

print(f"\nQuantidade de números digitados: {qt_num}")
print(f"Soma Total: {soma}")
print(f"Média Aritmética: {soma/qt_num}")