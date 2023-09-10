def main():
    # Solicita ao usuário que insira o texto
    text = input("Text: ")

    # Calcula o número de letras, palavras e frases no texto
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)

    # Calcula o índice Coleman-Liau
    L = (letters / words) * 100
    S = (sentences / words) * 100
    index = round(0.0588 * L - 0.296 * S - 15.8)

    # Imprime o nível escolar necessário
    if index < 1:
        print("Before Grade 1")
    elif index >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {index}")

def count_letters(text):
    count = 0
    for char in text:
        if char.isalpha():
            count += 1
    return count

def count_words(text):
    count = 1  # Começa com 1 palavra para contar a última palavra
    for char in text:
        if char.isspace():
            count += 1
    return count

def count_sentences(text):
    count = 0
    for char in text:
        if char in [".", "!", "?"]:
            count += 1
    return count

if __name__ == "__main__":
    main()
