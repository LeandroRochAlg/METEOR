### README

# Meteor Challenge

Este repositório contém soluções para o Meteor Challenge, incluindo a contagem de estrelas e meteoros em uma imagem, a verificação de quais meteoros caem na água e uma tentativa de decodificar uma frase oculta. A tarefa opcional de encontrar a frase oculta não foi completada, mas o código para as outras partes está funcional.

## Estrutura do Repositório

- **meteor.py**: Código principal que conta o número de estrelas e meteoros, e verifica quais meteoros caem na água.
- **utils/salvatxt.py**: Código para salvar a matriz de pixels da imagem em um arquivo de texto.
- **utils/salvatxtPB.py**: Código para converter a imagem para preto e branco e salvar a matriz de pixels em um arquivo de texto.

## Tarefas

### 1. Contar o número de Estrelas
### 2. Contar o número de Meteoros
### 3. Verificar quantos Meteoros caem na água
### 4. (Opcional) Encontrar a frase oculta nos pontos no céu

## Resultados

- **Meteoros**: 328
- **Estrelas**: 315
- **Meteoros que caem na água**: 105
- **Frase**: A tarefa opcional de decodificação da frase oculta não foi completada.

## Códigos

- O script `meteor.py` carrega a imagem `meteor_challenge_01.png` e converte-a para uma matriz de pixels. Em seguida, percorre cada pixel para contar estrelas e meteoros, e verifica se os meteoros caem na água.
- O script `utils/salvatxt.py` carrega a imagem e converte-a para uma matriz de pixels. Em seguida, salva essa matriz em um arquivo de texto.
- O script `utils/salvatxtPB.py` carrega a imagem, converte-a para tons de cinza, e salva a matriz de pixels resultante em um arquivo de texto.

## Como Executar

1. **Instalar Dependências**:
   - Certifique-se de ter o `Pillow` e `numpy` instalados. Você pode instalar usando:
     ```sh
     pip install pillow numpy
     ```

2. **Executar o Código Principal**:
   - Execute `meteor.py` para contar estrelas, meteoros e verificar quais caem na água:
     ```sh
     python meteor.py
     ```

3. **Salvar Matriz de Pixels**:
   - Execute `utils/salvatxt.py` para salvar a matriz de pixels da imagem original:
     ```sh
     python utils/salvatxt.py
     ```
   - Execute `utils/salvatxtPB.py` para salvar a matriz de pixels da imagem em preto e branco:
     ```sh
     python utils/salvatxtPB.py
     ```

## Contribuições

Sinta-se à vontade para abrir issues e pull requests se encontrar algum problema ou quiser adicionar melhorias ao código.

## Licença

Este projeto é licenciado sob os termos da licença MIT.

---

Espero que este README forneça uma orientação clara sobre como utilizar o código e quais resultados esperar. Se houver alguma dúvida ou sugestão, por favor, entre em contato!