#Solicitar preço de uma mercadoria e desconto. Exibir vl desconto e preço a pagar
price = float(input("Digite o valor da mercadoria R$: "))
percent = float(input("Digite o percentual de desconto (%): "))

discount = price * percent/100
new_price = price - discount

print(f"\nValor do desconto R$: {discount:5.2f} \nPreço a pagar: {new_price:5.2f}")