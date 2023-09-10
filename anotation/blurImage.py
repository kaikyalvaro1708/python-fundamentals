from PIL import Image, ImageFilter

before = Image.open("bridge.bmp")
after = before.filter(ImageFilter.BoxBlur(10))
after.save("out.bmp")



# No Python, incluímos outras bibliotecas com import e aqui vamos importar os nomes de Image e ImageFilter da biblioteca PIL. 
# Image é uma estrutura que não apenas possui dados, mas funções que podemos acessar com o “.”, como com Image.open.
# Abrimos uma imagem chamada bridge.bmp, chamamos uma função de filtro de desfoque e salvamos em um arquivo chamado out.bmp.
# E nós podemos executar isso com python blur.py depois de salvar para um arquivo chamado blur.py.