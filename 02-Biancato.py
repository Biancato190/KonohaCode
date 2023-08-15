peso = float(input("insira seu peso em quilos: "))
altura = float(input("insita sua altura: "))

imc = peso / (altura ** 2)

print(f"Seu imc é: {imc:.2f}")

if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc < 24.9:
    print("Seu peso está dentro da faixa saudável")
elif imc < 29.9:
    print("Você está com sobrepeso." )
else:
    print("Você está Obeso." )