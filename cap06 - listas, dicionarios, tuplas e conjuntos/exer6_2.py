lista1 = []
lista2 = []
while True:
    n = int(input("Digite um valor para a 1ª lista (Ou 0 para sair): "))
    if n == 0:
        break
    lista1.append(n)
while True:
    n = int(input("Digite um valor para a 2ª lista (Ou 0 para sair: "))
    if n == 0:
        break
    lista2.append(n)
lista3 = lista1[:]  #Copia todos os elementos da lista 1
lista3.extend(lista2)  #Adiciona os elementos da lista 2 (se fosse append() adicionaria a lista 2 como apenas 1 elemento)

print(lista3)