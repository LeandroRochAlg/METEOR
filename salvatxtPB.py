from PIL import Image
import numpy as np

# Carregar a imagem do arquivo
imagem = Image.open("meteor_challenge_01.png")

# Converter a imagem para tons de cinza
imagemPB = imagem.convert('L')

# Converter a imagem para um array de pixels
pixels = np.array(imagemPB)

# Salvar a matriz de pixels em um arquivo de texto
np.savetxt('matriz_de_pixelsPB.txt', pixels, fmt='%d')

print("Matriz de pixels salva em 'matriz_de_pixelsPB.txt'.")