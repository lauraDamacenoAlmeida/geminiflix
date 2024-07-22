import streamlit as st
import pandas as pd
import base64
import seaborn as sns
import numpy as np
import google.generativeai as genai
from deep_translator import GoogleTranslator

model = "models/embedding-001"
GOOGLE_API_KEY= "AIzaSyCzb82DnEM0S4pQyZAJAHFXBI8wmFTxmsQ"
genai.configure(api_key=GOOGLE_API_KEY)


def embed_fn(title, text):
  return genai.embed_content(model=model,
                                 content=text,
                                 title=title,
                                 task_type="RETRIEVAL_DOCUMENT")["embedding"]


# encontrar o filme semelhante com a entrada do usuário
def gerar_e_buscar_consulta(consulta, base):
  embedding_da_consulta = genai.embed_content(model=model,
                                 content=consulta,
                                 task_type="RETRIEVAL_QUERY")["embedding"]

  produtos_escalares = np.dot(np.stack(base["Embeddings"]), embedding_da_consulta)

  indice = np.argmax(produtos_escalares)
  return base.iloc[indice]["description"], base.iloc[indice]["title"]

def read_embeddings():
    df = pd.read_csv('netflix_titles.csv')
    movies200 = df.loc[:200]
    movies200["Embeddings"] = movies200.apply(lambda row: embed_fn(row["title"], row["description"]), axis=1)
    return movies200



def output_genai(trecho,titulo):
    generation_config = {
    "temperature": 0.2,
    "candidate_count": 1
    }

    #configurações de segurança
    safety_settings = {
        "HARASSMENT": "BLOCK_LOW_AND_ABOVE",
        "HATE":"BLOCK_LOW_AND_ABOVE",
        "SEXUAL": "BLOCK_NONE",
        "DANGEROUS": "BLOCK_LOW_AND_ABOVE"
    }

    model_2 = genai.GenerativeModel("gemini-1.0-pro",
                                generation_config=generation_config,safety_settings=safety_settings)
    prompt = f"You are friend of someone and you are recommended a movie to someone based on what they said. Rewrite this text leaving it in Portuguese and in a more informal way and friendly, without adding information that is not part of the text: {trecho} movie name {titulo}"
    resposta = model_2.generate_content(prompt) 
    return resposta.candidates[0].content.parts[0].text


def translate_english(prompt):
    translated = GoogleTranslator(source='pt', target='english').translate(prompt)
    return translated

def main():
    st.title('E aí, pessoal! Sejam muito bem-vindos ao GeminiFlix! 😄')
    st.markdown("Estou aqui para trazer um pouquinho de diversão e facilidade para os seus momentos de indecisão na hora de escolher um filme ou programa para assistir. Quem nunca ficou perdido no mar de opções da Netflix, né? Eu sei como é! É por isso que estou aqui para ajudar!")
    st.markdown("Eu sou o seu assistente de *Inteligência Artificil* perfeito para esses momentos de indecisão. Basta me dizer o que você está procurando, e eu vou correr atrás das melhores opções para você! *Adeus indecisão, olá entretenimento sem esforço comigo!* Estou aqui para fazer a sua experiência na Netflix muito mais fácil e divertida. Vamos nessa! 🎬✨")
    st.image('images/teste1.jpg', caption='Geminiflix - Imagem feita pela IA do Nightcafé')

    st.subheader("Como posso interagir com você?")
    st.markdown("Para isso basta colocar no chat ao lado as características e descrição do filme ou programa de TV que você tem interesse em assistir.")


    st.subheader("Mas com base no que você está tirando as recomendações?")
    st.markdown("Fui treinado com uma ampla base de conhecimento que inclui mais de 200 filmes e programas de TV disponíveis no catálogo da Netflix. Essa base foi compilada na comunidade Kaggle, uma das maiores comunidades de ciência de dados do mundo. ✨ No entanto, é importante notar que minha base de dados abrange filmes lançados até o ano de 2021. Portanto, não poderei oferecer recomendações de conteúdos lançados após esse ano.")

    st.subheader("E como você faz essas recomendações?")
    st.markdown("Eu sou um conjunto de dois modelos de Inteligência Artificial da Google, o Gemini. E baseado nas características do que você quer assistir, vou procurar dentro do meu acervo de conhecimento o mais parecido com o seu gosto. Espero que você goste da minha indicação")

    st.subheader("Criadora")
    st.markdown("Fui criado pela Laura Damaceno de Almeida (@laura_data_talks). Qualquer problema comigo ou pontos de melhoria, fale com ela.")

    movies = read_embeddings()
    #st.image('image.png',width= 900)


    with st.sidebar:
        messages = st.container(height=300)
        messages.chat_message("assistant").write(f"GeminiFlix: Olá humano 👋. Sou o Geminiflix seu assistente para momentos de indecisão ao escolher algo para assitir!")
        messages.chat_message("assistant").write(f"Descreva para mim o tipo de filme que você gostaria de assistir.")


        if prompt := st.chat_input("Digite algo.."):
            messages.chat_message("user").write(prompt)
            prompt_english = translate_english(prompt)
            trecho, titulo = gerar_e_buscar_consulta(prompt_english, movies)
            resposta = output_genai(trecho,titulo)

            #resposta = output_genai(model_2, trecho,titulo)
            messages.chat_message("assistant").write(f"GeminiFlix: {resposta}")
    #prompt = st.chat_input(placeholder="Your message")
    #if prompt:
    #    st.write(prompt)




if __name__ == '__main__':
    main()