from PIL import Image
import numpy as np

# Carregar a imagem do arquivo
imagem = Image.open("meteor_challenge_01.png")

# Converter a imagem para um array de pixels
pixels = np.array(imagem)

# Obter dimensões da imagem
altura, largura, _ = pixels.shape

# Transformar a matriz 3D em uma matriz 2D
pixels_2d = pixels.reshape(altura, largura * 4)  # Multiplicamos a largura por 3 para manter os valores R, G, B juntos

# Salvar a matriz de pixels em um arquivo de texto
np.savetxt('matriz_de_pixels.txt', pixels_2d, fmt='%d')

print("Matriz de pixels salva em 'matriz_de_pixels.txt'.")
