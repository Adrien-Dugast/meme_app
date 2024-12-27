import streamlit as st
import webbrowser
import random

def charge_list_refs():
    filename = "liste_refs.txt"
    f = open(filename, "r")
    lines = f.read().split(sep = '\n')
    list_refs = [string.split(sep = ', ')[0] for string in lines]

    return(list_refs)

def display_random_video(list_refs):
    st.text('coucou 1')
    if len(list_refs)==0:
        list_refs = charge_list_refs()
        if len(list_refs)==0:
            st.text("oups aucune ref dans la liste, c'est un bug...")
    st.text('coucou 2')
    url = random.choice(list_refs)
    list_refs.remove(url)
    webbrowser.open_new_tab(url)
    st.text('coucou 3')
    return(list_refs)

list_refs = charge_list_refs()

st.title('Meme trainer 3000 GX premium edition')

st.text('''
        Si vous êtes sur cette page, c'est que vous avez conscience de votre manque de culture criant. Ne 
        vous en faites pas, ce n'est pas définitif. On peut progresser dans tous les domaines, et celui la ne fait pas
        exception. \n Grace au meme trainer 3000, vous allez avoir l'occasion de combler ce retard. \n
        Appuyez sur le bouton ci-dessous pour commencer votre entrainement.
        ''')

a = st.button("Je veux devenir quelqu'un de cultivé et intéressant en société")


if a:
    st.text('Bouton appuyé')
    st.text(f"{len(list_refs)} refs dans la liste")
    video_file = open("Jeux1.mp4", "rb")
    video_bytes = video_file.read()
    st.video(video_bytes)

    list_refs = display_random_video(list_refs)
    
