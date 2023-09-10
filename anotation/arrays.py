scores = [72, 73, 74]

print(f"Average: " + str(sum(scores)) / len(scores))

# Podemos usar sum, uma função incorporada ao Python, para somar os valores em nossa lista e dividi-la pelo número 
# de pontuações, usando a função len para obter o comprimento da lista. Em seguida, convertemos o float em uma 
# string antes de podermos concatená-lo e imprimi-lo.

scores02 =[]
for i in range(3):
    scores.append(input("Score: "))

a = input("Antes: ")
print("Depois: ", end="")
for c in a:
    print(c.upper(), end="")
    print()

# Python irá iterar sobre cada caractere na string para nós com apenas for c in s.
# Para tornar uma string maiúscula, também podemos simplesmente chamar s.upper() , 
# sem ter que iterar nós mesmos sobre cada caractere.

 