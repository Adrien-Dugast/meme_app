import streamlit as st
import webbrowser
import random
import os

def display_random_video(list_refs):
    list_vids = os.listdir('videos')
    vid_to_display = random.choice(list_vids)
    video_file = open("Jeux1.mp4", "rb")
    video_bytes = video_file.read()
    st.video(video_bytes, autoplay = True)


st.title('Meme trainer 3000 GX premium edition')

st.text('''
        Si vous êtes sur cette page, c'est que vous avez conscience de votre manque de culture criant. Ne 
        vous en faites pas, ce n'est pas définitif. On peut progresser dans tous les domaines, et celui la ne fait pas
        exception. \n Grace au meme trainer 3000, vous allez avoir l'occasion de combler ce retard. \n
        Appuyez sur le bouton ci-dessous pour commencer votre entrainement.
        ''')

a = st.button("Je veux devenir quelqu'un de cultivé et intéressant en société")


if a:
    display_random_video()
    
