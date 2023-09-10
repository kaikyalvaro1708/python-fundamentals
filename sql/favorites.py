#Começando com SQL - database
import csv

#dictionary
#usado para armazenar os títulos
titles = {}


#Modo para ler o arquivo em csv
with open("Favorite TV Shows -  Form Responses 1.csv", "r") as file:
    reader = csv.DictReader(file) #ler e trata a primeira linha do arquivo, geralmentos os nomes
    for row in reader: #loop que itera sobre cada linha do arquivo
        #acessa o valor da coluna "title", o strip remove espaços em branco
        title = row["title"].strip().upper()
        if title in titles:
            titles[title] += 1
        else:
            titles[title] = 1

#formando os titles
#loop que itera sobre os titulos armazenados no dic 'titles'
#O sorted oderna os titulos em ordem decrescente
#O key lambda é uma função anônima
#"reverse=True" garante que a ordenação seja em ordem decrescente
for title in sorted(titles, key=lambda title: titles[title], reverse=True):
    print(title, titles[title])