sair = "sair"

Nome = input("Digite seu nome ")
Sobrenome = input("digite seu sobrenome ")
idade = int(input("digite sua idade "))
altura = float(input("digite sua altura "))
peso = float(input("digite seu peso "))

maior_idade = idade >= 18

print("resultado")
print("nome", Nome)
print("sobrenome", Sobrenome)
print("idade", idade)
print("altura", altura)
print("peso", peso, "kg")
print("maior de idade", "sim" if maior_idade else "não")