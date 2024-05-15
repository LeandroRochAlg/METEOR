from PIL import Image
import numpy as np
import sys

# Carregar a imagem do arquivo
imagem = Image.open("meteor_challenge_01.png")

# Converter a imagem para um array de pixels
pixels = np.array(imagem)

# Contar meteoros e estrelas
meteoros = 0
estrelas = 0
agua = 0

for i in range(len(pixels)):
    for j in range(len(pixels[i])):
        if pixels[i][j][0] == 255 and pixels[i][j][1] == 255 and pixels[i][j][2] == 255:
            estrelas += 1
        elif pixels[i][j][0] == 255:
            meteoros += 1

            # Verificar se o meteoro vai cair na água
            for k in range(len(pixels[i]) - 150, 0, -1):  # Percorrer a coluna de baixo para cima para otimizar
                if pixels[k][j][2] == 255 and pixels[k][j][0] == 0 and pixels[k][j][1] == 0:
                    agua += 1
                    break
                elif pixels[k][j][0] > 0:
                    break
        elif pixels[i][j][0] == 0 and pixels[i][j][1] == 0 and pixels[i][j][2] == 0:
            break

# Exibir o resultado
print(f"Meteoros: {meteoros}")
print(f"Estrelas: {estrelas}")
print(f"Metoro cai na água: {agua}")
sys.exit()