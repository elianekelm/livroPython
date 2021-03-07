print("**** CÁLCULO VALOR DA PASSAGEM ****")
km = float(input("Distância a percorrer (km): "))


if km <= 200:
    price = 0.5
else:
    price = 0.45

vl_passagem = km * price
print(f"Valor da passagem R$: {vl_passagem:5.2f}")