# Geminiflix
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*WqK9zocvpZNIHPQmHtLNhg.png)

Gemini é uma família de modelos de linguagem grandes multimodais (LLM) desenvolvidos pelo Google DeepMind. Anunciado em 6 de dezembro de 2023, posicionado como concorrente do GPT-4 da OpenAI. Então decidi utilizar essa ferramenta potente para criar um recomendador com base na similaridade entre palavras, inclusive compartilhei mais detalhes no meu post no [Medium](https://medium.com/@lauradamaceno/geminiflix-utilizando-gemini-para-recomendar-filmes-e-séries-da-netflix-ccf079b014ca).

# Objetivo do projeto

Eu certamente já passei por isso inúmeras vezes, como uma geminiana apaixonada por séries e filmes eu precisava ajudar pessoas que assim como eu sofrem com esse problema 🤓.
Por isso, eu criei meu próprio assistente virtual chamado Geminiflix para nos ajudar! Ele é o assistente perfeito para esses momentos de indecisão. Com Geminiflix ao seu lado, você nunca mais perderá tempo procurando o filme ideal.

Basta descrever o que você está procurando, e Geminiflix irá encontrar as opções perfeitas para você. Adeus indecisão, olá entretenimento sem esforço com Geminiflix!


# Requisitos
1. [Python 3.6 ou maior](https://www.python.org/downloads/)

2. [Pandas](https://pandas.pydata.org/docs/): Para explorar e fazer a leitura dos dados

3. [Matplotlib](https://matplotlib.org/): Para a visulização dos dados

4. [Seaborn](http://seaborn.pydata.org): Para a visulização dos dados

5. [google.generativeai](https://scikit-learn.org/stable/): Biblioteca para interagir com a API do Gemini


Para instalar as bibliotecas você pode digitar no terminal:
```
pip install nome_pacote
```
Por exemplo:

```
pip install pandas
```

# Conjunto de dados
Para treinar a nossa IA precisamos ter uma base de conhecimento com as informações dos filmes e séries disponíveis. Então estou considerando a base de dados do [Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows) com as informações do catálogo da Netflix.

# Interface web desenvolvida
Logo após a construção lógica do funcionamento do GeminiFlix, explorei construir uma interface web utilizando Streamlit para deixar mais atrativo a interação com a IA

![](https://github.com/lauraDamacenoAlmeida/geminiflix/blob/main/images/Interface%20web.png)

