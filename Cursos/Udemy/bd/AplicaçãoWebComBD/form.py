import streamlit as st
import dados

st.title("Filmes")

titulo = st.text_input("Título do filme")
ano = st.number_input("Ano do filme", min_value=2000, max_value=2024, step=1)
nota = st.slider("Nota do filme", min_value=0.0, max_value=10.0, step=0.5) 

if st.button ("Adicionar filme"):
    if titulo and ano and nota:
        dados.inserir_dados(titulo, ano, nota)
        st.success("Filme adicionado com sucesso!")
    else:
        st.error("Por favor, preencha todos os campos.")

filmes = dados.obtendo_dados()
st.subheader("Lista de filmes")
st.table(filmes)