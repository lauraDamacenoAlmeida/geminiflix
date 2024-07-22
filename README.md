# Geminiflix
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*WqK9zocvpZNIHPQmHtLNhg.png)

Gemini é uma família de modelos de linguagem grandes multimodais (LLM) desenvolvidos pelo Google DeepMind. Anunciado em 6 de dezembro de 2023, posicionado como concorrente do GPT-4 da OpenAI. Então decidi utilizar essa ferramenta potente para criar um recomendador com base na similaridade entre palavras, inclusive compartilhei mais detalhes no meu post no [Medium](https://medium.com/@lauradamaceno/geminiflix-utilizando-gemini-para-recomendar-filmes-e-séries-da-netflix-ccf079b014ca).

# Objetivo do projeto

O GeminiFlix foi criado para ser um assistente virtual que através de uma entrada textual trazida pelo usuário, ele irá buscar um filme ou série que tem combinação com o solicitado através do uso de IA generativa. 

# Estrutura do projeto:
1. Main.py : interface web feita com streamlit para interação com os usuários.
2. netflix_titles.csv: conjunto de dados da netflix com o catélogo dos filmes e séries
3. Geminiflix.ipynb: notebook com a criação do racional do sistema. Contém a exploração dos dados e primeiras interações com o assistente generativo

# Tecnologias Google utilizadas:

1. Gemini: para transformar texto em números para identificação de textos similares. E utilizar IA generativa para gerar um texto novo e amigável para o usuário.
2. Google translator: para traduzir a solitação do usuário do português para o inglês.

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

# Para excutar o notebook
Atualmente o notebook está com o seguinte trecho de código:

```
# Import the Python SDK
import google.generativeai as genai
from google.colab import userdata # para evitar de vazar a chave

api_key = userdata.get("SECRET_KEY") # está lá no campo "secrets", addnew secret
GOOGLE_API_KEY= api_key
genai.configure(api_key=GOOGLE_API_KEY)

```
Para você conseguir rodar localmente, é importante ajustar esse trecho para e colocar no lugar de "COLOQUE AQUI SUA API KEY" a sua API Key:

```
# Import the Python SDK
import google.generativeai as genai

GOOGLE_API_KEY= "COLOQUE AQUI SUA API KEY"
genai.configure(api_key=GOOGLE_API_KEY)

```

# Interface web desenvolvida
Logo após a construção lógica do funcionamento do GeminiFlix, explorei construir uma interface web utilizando Streamlit para deixar mais atrativo a interação com a IA

![](https://github.com/lauraDamacenoAlmeida/geminiflix/blob/main/images/Interface%20web.png)

