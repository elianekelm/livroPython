#Converter temperatura de °C para °F
temp_celsius = float(input("Digite a temperatura em °Celsius: "))
temp_fah = (temp_celsius * 9 / 5) + 32

print(f"{temp_celsius}° Celsius equivalem a {temp_fah:5.2f}° Fahrenheit.")