words = set()

def load(dictionary):
   file = open(dictionary, "r")
   for line in file:
      words.add(line.rstrip())
   file.close()
   return True

def check(word):
   if word.lower() in words:
      return True
   else:
      return False

def size():
   return len(words)

def unload():
   return True

# Primeiro, criamos um novo conjunto chamado words.

# Observe que não precisamos de uma função main. Nosso programa Python será executado de cima para baixo. Aqui, 
# queremos definir uma função, então usamos def load(). load terá um parâmetro, dictionary, e seu valor de retorno 
# está implícito. Nós abrimos o arquivo com open, e iteramos sobre as linhas no arquivo com apenas for line in file:.
# Em seguida, removemos a nova linha no final da linha e a adicionamos à words. Observe que line é uma string, mas
# tem uma função .rstrip que podemos chamar.

# Então, para check, podemos apenas perguntar if word.lower() in words. Para o tamanho , podemos usar len para 
# contar o número de elementos em nosso conjunto e, finalmente, para unload, não precisamos fazer nada, já que 
# o Python gerencia a memória para nós.