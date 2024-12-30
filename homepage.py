import streamlit as st
import datetime

st.title("Bienvenue sur la page d'Adrien")
st.header("A gauche la liste de mes apps rigolotes (en construction)")

st.text('''
        J'ai créé ce site pour mettre un peu toutes mes conneries, je sais pas à quel point ça va 
        marcher ni à quel point je vais en mettre mais bon ça m'amuse donc je le fais.
        ''')

f = open("log.txt", 'a')
f.write(datetime.datetime.now())
f.close()