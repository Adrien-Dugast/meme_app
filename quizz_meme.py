import streamlit as st
import json
import time
import random as rd


if "is_doing_quizz" not in st.session_state:
    st.session_state['is_doing_quizz']=False

def is_doing_quizz_to_True():
    st.session_state['is_doing_quizz']= True
    st.session_state['score_of_current_quizz'] = 0
    st.session_state['current_question'] = 1

def check_answer(i):
    if st.session_state['correct_answer_id']==i:
        st.session_state['score_of_current_quizz']+=1
    st.session_state['current_question']+=1

with open("test_q.json", "r") as f:
    questions_json = json.load(f)



st.title("Quizz meme")

if st.session_state['is_doing_quizz']==False:

    
    st.text('''
            Félicitations, éminent membre de la société ! Si vous êtes arrivés jusqu'ici, c'est que vous faites parti des plus braves, parmi les connaisseurs et fin gourmets de références.
            Vous voulez de plus prouver votre valeur à vos amis ? Aucun problème, vous pouvez passer juste ici la certification meme-3000, certifiée et reconnue par l'êtat.
            Ce diplôme, équivalent à un niveau bac+5 et délivré par la commission des titres, pourra vous ouvrir de nombreuses portes.
            ''')
    st.header("Modalités d'obtention")
    st.text(
        '''
        Un score minimal de 9/10 est demandé pour obtenir ce diplôme, hautement sélectif.
        '''
    )

    st.text(
        '''
        Cliquez sur le bouton ci-dessous pour commencer. Taux de réussite actuel : 4,3%
        '''
    )
    
    a = st.button("Commencer mon test", on_click = is_doing_quizz_to_True)
    st.session_state['time_start_of_test'] = time.time()
    if a:
        st.session_state['is_doing_quizz'] = True

max_nb_of_q = min(10,len(questions_json))

if st.session_state['is_doing_quizz']:
    if 'current_question' not in st.session_state:
        st.session_state['current_question']=1
    if 'score_of_current_quizz' not in st.session_state:
        st.session_state['score_of_current_quizz']=0

    questions_to_ask = rd.sample(questions_json,max_nb_of_q)

    if st.session_state['current_question']< max_nb_of_q+1:
        idx = st.session_state['current_question']-1
        st.header(f'Question {idx+1} : ')
        st.text(questions_to_ask[idx]['q'])
        c1,c2,c3 = st.columns(3)

        st.session_state['correct_answer_id'] = int(questions_to_ask[idx]['ir'])

        c1.button(questions_to_ask[idx]['r1'], on_click = lambda : check_answer(1))
        c2.button(questions_to_ask[idx]['r2'], on_click = lambda : check_answer(2))
        c3.button(questions_to_ask[idx]['r3'], on_click = lambda : check_answer(3))


    else:
        if st.session_state['score_of_current_quizz']>=9:
            st.success('Félicitations !!')
            st.text('''
                    Vous avez réussi avec brio l'examen de culture générale, vous faites désormais parti des rares
                    élus à posséder ce diplôme. La légende raconte que seul un expert dans l'art de l'humour et de la
                    répartie peut réussir un tel quizz, félicitations à vous !
                    ''')

        ## Faire la page pour générer le diplome/ demander le nom ?
        

        else:
            st.text(
                f'''
                Dommage, votre score est de seulement {st.session_state['score_of_current_quizz']}/{max_nb_of_q}. Ce n'est pas suffisant pour être un maître dans l'art 
                du meme, de la répartie et de l'humour. Vous pouvez retenter votre chance ! \n Cliquez ci-dessous pour revenir à la page d'acceuil
                ''')
            
        st.session_state['current_question'] = 1
        st.session_state['is_doing_quizz'] = False
        st.session_state['score_of_current_quizz'] = 0
        st.session_state['quizz_finished'] = True

        st.button("Revenir à la page d'acceuil")

        
