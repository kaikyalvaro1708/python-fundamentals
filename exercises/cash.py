# Função para calcular o número mínimo de moedas
def calculate_coins(change):
    coins = 0
    
    # Converter centavos para dólares
    cents = round(change * 100) #em um dólar tem 100 centavos
    
    # Definir os valores das moedas disponíveis
    coin_values = [25, 10, 5, 1]
    
    # Iterar pelas moedas e contar quantas são necessárias
    for value in coin_values:
        while cents >= value:
            cents -= value #em cada iteração, subtrai o valor da maior moeda possível
            coins += 1 #a cada iteração, incrementaa variável 'coins' para contar a quantidade de moedas usadas 
    
    return coins #retorna o número mínimo de moedas necessárias para representar o troco

def main():
    # Solicitar ao usuário o valor do troco devido
    while True:
        change = float(input(f"Change owed: "))
        if change >= 0:
            break

    # Calcular o número mínimo de moedas
    coins = calculate_coins(change)
    
    # Imprimir o resultado
    print("Your change contains: " + str(coins) + " coins")

if __name__ == "__main__":
    main()
