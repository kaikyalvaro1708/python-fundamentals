import sys 

names = ["Bill", "Charlie", "Fred", "George", "Ginny", "Percy", "Ron"]

if "Ron" in names: 
    print("Encontrado")
else: 
    print("Não encontrado")

# Se tivermos um dicionário, um conjunto de pares de chaves-valores, também 
# podemos verificar se há uma chave específica e examinar o valor armazenado para ela:

people = {
    "Brian": "+1-617-495-1000",
    "David": "+1-949-468-2750"
}

name = input("Nome: ")
if name in people:
    print(f"Número: {people[name]}")
else:
    print("Não encontrado")

