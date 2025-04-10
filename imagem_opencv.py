import cv2
import numpy as np
import os

# =============================
# Funções de Utilidade
# =============================

def carregar_imagem(caminho):
    """
    Carrega a imagem do caminho fornecido.
    Retorna a imagem em formato BGR.
    """
    imagem = cv2.imread(caminho)
    if imagem is None:
        raise FileNotFoundError("Erro ao carregar imagem - Verifique o caminho.")
    return imagem


def exibir_imagem(nome, imagem):
    """
    Exibe uma imagem em uma janela com o nome fornecido.
    A janela se fecha após pressionar qualquer tecla.
    """
    cv2.imshow(nome, imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def salvar_exibir_imagem(nome, imagem):
    """
    Salva a imagem com o nome especificado dentro da pasta 'resultados',
    criando a pasta caso não exista. Também exibe a imagem.
    """
    if not os.path.exists("resultados"):
        os.makedirs("resultados")
    caminho = f"resultados/{nome}.jpg"
    cv2.imwrite(caminho, imagem)
    exibir_imagem(nome, imagem)


# =============================
# Funções de Transformação
# =============================

def converter_cinza(imagem):
    """
    Converte a imagem de BGR para escala de cinza.
    Útil para análises estruturais, como binarização e segmentação.
    """
    return cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)


def equalizar_histograma(imagem):
    """
    Aplica equalização de histograma na imagem em tons de cinza.
    Realça os contrastes, especialmente em imagens escuras ou lavadas.
    """
    return cv2.equalizeHist(imagem)


def converter_hsv(imagem):
    """
    Converte a imagem do espaço de cor BGR para HSV.
    HSV separa as informações de cor (Hue) da iluminação (Value).
    """
    return cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)


def ajustar_saturacao(imagem_hsv, fator):
    """
    Ajusta a saturação da imagem no espaço HSV.
    Aumentar o fator torna as cores mais vibrantes; reduzir, mais suaves.
    """
    imagem_hsv = imagem_hsv.astype(np.float32)
    imagem_hsv[:, :, 1] = np.clip(imagem_hsv[:, :, 1] * fator, 0, 255)
    imagem_resultado = imagem_hsv.astype(np.uint8)
    return cv2.cvtColor(imagem_resultado, cv2.COLOR_HSV2BGR)


def ajustar_brilho_contraste(imagem, brilho=50, contraste=1.2):
    """
    Ajusta o brilho e contraste da imagem.
    Parâmetro 'beta' controla o brilho e 'alpha' o contraste.
    """
    return cv2.convertScaleAbs(imagem, alpha=contraste, beta=brilho)


def redimensionar(imagem, escala, metodo):
    """
    Redimensiona a imagem com base em uma escala (ex: 0.5 para reduzir pela metade).
    O método de interpolação define a qualidade da transformação:
    - INTER_CUBIC (melhor para reduzir)
    - INTER_LINEAR (melhor para ampliar)
    """
    largura = int(imagem.shape[1] * escala)
    altura = int(imagem.shape[0] * escala)
    return cv2.resize(imagem, (largura, altura), interpolation=metodo)


def rotacionar(imagem, angulo):
    """
    Rotaciona a imagem em torno de seu centro.
    O tamanho da imagem permanece fixo.
    """
    h, w = imagem.shape[:2]
    matriz = cv2.getRotationMatrix2D((w // 2, h // 2), angulo, 1)
    return cv2.warpAffine(imagem, matriz, (w, h))


def espelhar_horizontalmente(imagem):
    """
    Gera o espelhamento horizontal (imagem invertida da esquerda para direita).
    """
    return cv2.flip(imagem, 1)


def recortar_central(imagem, largura, altura):
    """
    Recorta uma área central da imagem com as dimensões desejadas.
    Útil para focar em uma região específica da imagem.
    """
    h, w = imagem.shape[:2]
    x_inicio = (w - largura) // 2
    y_inicio = (h - altura) // 2
    return imagem[y_inicio:y_inicio + altura, x_inicio:x_inicio + largura]


def binarizar_otsu(imagem):
    """
    Aplica binarização com o método de Otsu.
    Ideal para separar fundo e objeto em imagens de tons de cinza.
    """
    _, binarizada = cv2.threshold(imagem, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return binarizada


# =============================
# Pipeline de Processamento
# =============================

def processar_imagem(caminho):
    """
    Função principal que aplica todas as transformações na imagem original.
    Cada transformação é salva em disco e exibida ao usuário.
    """
    imagem = carregar_imagem(caminho)
    salvar_exibir_imagem("original", imagem)

    # Etapa 1: Escala de cinza e equalização
    cinza = converter_cinza(imagem)
    salvar_exibir_imagem("cinza", cinza)
    equalizada = equalizar_histograma(cinza)
    salvar_exibir_imagem("equalizada", equalizada)

    # Etapa 2: Saturação de cor (HSV)
    hsv = converter_hsv(imagem)
    saturado = ajustar_saturacao(hsv, fator=1.3)
    salvar_exibir_imagem("saturado", saturado)

    # Etapa 3: Ajustes de brilho e contraste
    ajustado = ajustar_brilho_contraste(imagem, brilho=50, contraste=1.2)
    salvar_exibir_imagem("brilho_contraste", ajustado)

    # Etapa 4: Redimensionamento
    reduzida = redimensionar(imagem, escala=0.5, metodo=cv2.INTER_CUBIC)
    salvar_exibir_imagem("reduzida", reduzida)
    ampliada = redimensionar(imagem, escala=2.0, metodo=cv2.INTER_LINEAR)
    salvar_exibir_imagem("ampliada", ampliada)

    # Etapa 5: Transformações geométricas
    rotacionada = rotacionar(imagem, angulo=45)
    salvar_exibir_imagem("rotacionada", rotacionada)
    espelhada = espelhar_horizontalmente(imagem)
    salvar_exibir_imagem("espelhada", espelhada)
    recorte = recortar_central(imagem, largura=300, altura=300)
    salvar_exibir_imagem("recortada", recorte)

    # Etapa 6: Binarização
    binarizada = binarizar_otsu(cinza)
    salvar_exibir_imagem("binarizada", binarizada)

    print("Processamento concluído. Imagens salvas na pasta 'resultados/'.")


# =============================
# Execução do Programa
# =============================

if __name__ == "__main__":
    processar_imagem("Trabalho1.jpg")
