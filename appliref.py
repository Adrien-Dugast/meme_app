import webbrowser
from tkinter import Button, Tk, Label
from tkinter import ttk
import time
import random


def charge_list_refs():
    filename = "liste_refs.txt"
    f = open(filename, "r")
    lines = f.read().split(sep = '\n')
    list_refs = [string.split(sep = ', ')[0] for string in lines]

    return(list_refs)

list_refs = charge_list_refs()

def display_random_video(list_refs):
    if len(list_refs)==0:
        list_refs = charge_list_refs()
        if len(list_refs)==0:
            ttk.label(root, text = "Aucune ref dans la liste, c'est un bug tkt pelo").place(x=0,y=0)
    url = random.choice(list_refs)
    list_refs.remove(url)
    webbrowser.open_new_tab(url)



root = Tk()
root.title("Dridrinator 3000 GX premium edition")
root.geometry("800x600")
# root.wm_state(newstate="zoomed")
root.bind('<Escape>',lambda e: root.destroy())
# ttk.Label(root, text="Hello World!").place(x=300,y=200)

# frm = ttk.Frame(root, padding = 10)
bouton = ttk.Button(root, text="Je veux devenir quelqu'un de cultivé et drôle !", command = lambda : display_random_video(list_refs)).place(x=250,y=300)
# frm.grid()



root.mainloop()
