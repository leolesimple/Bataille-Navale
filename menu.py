import tkinter as tk
from tkinter import ttk
from PIL import *
from leaderboard import *
from pre_game import *

def menu():
    """
        Fenêtre d'accueil du jeu de la Bataille Navale.
    """
    root = Tk()
    root.title("Bataille Navale | NSI")
    root.geometry("1280x854")
    root.resizable(False, False)

    bg = PhotoImage(file="img/background-sea-water.png")

    background_label = Label(root, image=bg)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    title = Label(root, text="Bataille Navale", fg="black", font=("Parisine", 70), bg="#3676a8", padx=20, pady=20)
    title.pack(pady=50)

    button_frame = Frame(root, bg="#3676a8")
    button_frame.pack()

    new_game = ttk.Button(
        button_frame,
        text='Nouvelle partie',
        command=lambda: config_game(), #choix des joueurs plutôt que le choix de la position des bateaux.
    )

    new_game.grid(row=0, column=0, padx=10, pady=10)

    leaderboard_button = ttk.Button(
        button_frame,
        text='Leaderboard',
        command=lambda: leaderboard(),
    )

    leaderboard_button.grid(row=0, column=1, padx=10, pady=10)

    root.update_idletasks()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width) // 7
    y = (screen_height) // 7
    root.geometry("+{}+{}".format(x, y))
    root.mainloop()