
def main(): #define a função principal do programa
    while True: 
        height = get_height() #chama a função 'get_height()'
        if height != -1: #se for igual a -1. siginifica que houve um erro na entrada de altura
            draw_pyramid(height) #chama a função com a altura fornecida pelo usuário
            break
        
def get_height(): #função de obter a altura
    try:
        height = int(input("Height: "))
        if height < 0 or height > 8: #se estiver fora do inntervalo, exibe uma mensagem de erro e retorna -1
            print("Height must be between 0 and 8. ")
            return -1
        return height
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return -1
    
def draw_pyramid(height): 
    for i in range(1, height + 1): #loop que percorre os números de 1 até a altura desejada
        spaces = ' ' * (height - i) #A quantidade de spaces é calculada subbtraindo a linha atual ('i') da altura total
        blocks = '#' * i
        print(spaces + blocks + " " + blocks + spaces)


if __name__ == "__main__":
    main()