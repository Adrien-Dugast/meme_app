import streamlit as st
import webbrowser
import random
import os
import json
import pickle as pkl
import datetime

# if 'list_used.pkl' in os.listdir():
#     with open('list_used.pkl','r') as f:
#         dict_IP = pkl.load(f) 
# else:
#     dict_IP = []

# # if st.session_state()
# dict_IP.append("rajouter l'IP, checker que c'est pas la même session ?")

def display_random_video():
    list_vids = os.listdir('videos')
    vid_to_display = random.choice(list_vids)
    path_to_video = os.path.join('videos',vid_to_display)
    video_file = open(path_to_video, "rb")
    video_bytes = video_file.read()

    st.header(vid_to_display[:-4])
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
    
