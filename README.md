#  Relatório Reflexivo - Processamento de Imagens com OpenCV

Este relatório descreve os efeitos das transformações aplicadas a uma imagem utilizando a biblioteca **OpenCV** em **Python**.
As operações foram realizadas com o objetivo de preparar e analisar a imagem por meio de diferentes técnicas de pré-processamento e transformação.

---

## 1.  Conversão para Escala de Cinza

A conversão da imagem original para **escala de cinza** elimina as informações de cor, mantendo apenas a intensidade luminosa de cada pixel.
Isso facilita operações subsequentes, como binarização e detecção de contornos.

---

## 2.  Equalização de Histograma

A **equalização de histograma** melhora o contraste da imagem em tons de cinza. Ela redistribui os níveis de intensidade, fazendo com que áreas
escuras e claras fiquem mais equilibradas e com mais detalhes visíveis.

---

## 3.  Conversão para HSV e Ajuste de Saturação

A imagem é convertida para o espaço de cor **HSV** (Matiz, Saturação, Valor), permitindo o ajuste seletivo da **saturação**. Isso torna as cores
mais vibrantes e realçadas, o que é útil para análises baseadas em cor.

---

## 4.  Ajuste de Brilho e Contraste

Utiliza a função `convertScaleAbs` do OpenCV para clarear a imagem e melhorar os contrastes visuais. Essa técnica é útil para compensar problemas
de **iluminação ruim** na imagem original.

---

## 5.  Redimensionamento

A imagem foi redimensionada para **metade** e para o **dobro** do seu tamanho original, utilizando diferentes métodos de **interpolação**. O
redimensionamento é importante para ajustes de desempenho e adaptação de imagens a diferentes contextos de visualização.

---

## 6.  Transformações Geométricas

Incluem:
- **Rotação** da imagem em 45 graus;
- **Espelhamento horizontal** (inversão da esquerda para a direita);
- **Recorte** de uma área central da imagem.

Essas transformações são úteis para simular variações e testar a **robustez** de algoritmos de reconhecimento.

---

## 7.  Binarização com Otsu

A binarização converte a imagem em **preto e branco**, utilizando o método de **Otsu** para determinar automaticamente o melhor limiar. Essa
técnica é essencial para tarefas de **OCR**, segmentação e reconhecimento de padrões.

---

##  Conclusão

As transformações aplicadas demonstram como técnicas de **processamento de imagem** podem modificar aspectos fundamentais de uma imagem digital.
Essas operações são **bases essenciais** para tarefas mais avançadas em **visão computacional**, como:
- Reconhecimento de padrões;
- OCR (Reconhecimento Óptico de Caracteres);
- Aplicações com aprendizado de máquina.

---

>  Este relatório é parte de uma atividade prática de estudo e implementação de técnicas de processamento de imagens com Python e OpenCV.
