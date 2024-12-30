import streamlit as st



# selected_tab = st.tabs(['tab 1', 'tab 2'])

# if selected_tab == 'tab 1':
#     st.write("eehh")

pages = {
    " " : [
        st.Page('homepage.py', title = "Home page")
    ],
    "Applications" : [
        st.Page("meme_trainer_page.py", title = "Meme trainer"),
        st.Page("quizz_meme.py", title = "Quizz même")
    ]

}

pg = st.navigation(pages)
pg.run()