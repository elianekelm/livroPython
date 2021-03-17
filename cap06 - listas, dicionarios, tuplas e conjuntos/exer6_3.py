lista1 = []
lista2 = []
while True:
    n = int(input("Digite um valor para a 1ª lista ou pressione 0 (zero) para sair: "))
    if n == 0:
        break
    lista1.append(n)

while True:
    n = int(input("Digite um valor para a 2ª lista ou pressione 0 (zero) para sair: "))
    if n == 0:
        break
    lista2.append(n)

#Adicionando a lista1 e a lista2 na lista3
lista3 = lista1[:]  #Faz a copia dessa lista
lista3.extend(lista2)  #Copia todos os elementos da lista2 para a lista3

lista_vl_unicos = list(set(lista3)) #Cria uma nova lista sem elementos repetidos
print(lista_vl_unicos)