# Podemos abrir um terminal após instalar o Python e usar outra biblioteca para converter texto em fala:

Em nosso próprio Mac ou PC, podemos abrir um terminal após instalar o Python e usar outra biblioteca para converter texto em fala:

importar pyttsx3

engine = pyttsx3.init ()
engine.say("olá, mundo")
engine.runAndWait()
Lendo a documentação, podemos descobrir como inicializar a biblioteca e dizer uma string.
Podemos até passar uma string de formato com engine.say (f "olá, {nome}") para dizer alguma entrada.
Podemos usar outra biblioteca, face_recognition, para encontrar rostos nas imagens:

# Encontre rostos na imagem
# https://github.com/ageitgey/face_recognition/blob/master/examples/find_faces_in_picture.py
from PIL import Image
import face_recognition

# Carregue o arquivo jpg em uma matriz numpy
image = face_recognition.load_image_file("office.jpg")

# Encontre todos os rostos na imagem usando o modelo baseado em HOG padrão.
# Este método é bastante preciso, mas não tão preciso quanto o modelo CNN e não é acelerado por GPU.
# Veja também: find_faces_in_picture_cnn.py
face_locations = face_recognition.face_locations(image)

for face_location in face_locations:
   # Imprima a localização de cada rosto nesta imagem: cima, direita, baixo, esquerda
   top, right, bottom, left = face_location

   # Você pode acessar o próprio rosto desta forma:
   face_image = image [top: bottom, left: right]
   pil_image = Image.fromarray(face_image)
   pil_image.show()
Com recognize.py podemos escrever um programa que encontra uma correspondência para um rosto específico.

Podemos criar um código QR, ou código de barras bidimensional, com outra biblioteca:

import os
import qrcode

img = qrcode.make("https://youtu.be/oHg5SJYRHA0")
img.save("qr.png","PNG")
os.system("open qr.png")
Podemos reconhecer a entrada de áudio de um microfone:

import speech_recognition

# Obtenha áudio do microfone
recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() como fonte:
   print("Say something:")
   audio = reconhecizer.listen(fonte)

# Reconhecer fala usando o Google Speech Recognition
print("Você disse:")
print(recognizer.recognize_google(audio))
Estamos seguindo a documentação da biblioteca para ouvir nosso microfone e convertê-lo em texto.

Podemos até adicionar lógica adicional para respostas básicas:

...
words = recognizer.recognize_google(audio)

# Responda ao discurso
if "hello" in words:
   print("Olá para você também :)")
elif "how are you" em palavras:
   print("Estou bem, obrigado!")
elif "goodbye" em palavras:
   print("Tchau pra você também")
else:
   print("Hm?")
Finalmente, usamos outro programa mais sofisticado para gerar deepfakes, ou vídeos que parecem realistas, mas gerados por computador, de várias personalidades.
Tirando proveito de todas essas bibliotecas disponíveis gratuitamente online, podemos facilmente adicionar funcionalidades avançadas aos nossos próprios aplicativos.
Bora colocar o que foi aprendido na prática?