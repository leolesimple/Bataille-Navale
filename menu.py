from pre_game import *
import tkinter as tk
from tkinter import ttk
from leaderboard import *


def menu(mode="color"):
    """
    Arguments :
        type: (Optionnel) Détermine le type de fond d'écran pour la fenêtre, avec "color" comme valeur par défaut.
    Retourne : Rien.
    Description : Crée une fenêtre d'accueil pour le jeu de la Bataille Navale. Configure le titre, le fond d'écran (selon le type spécifié), les boutons pour démarrer une nouvelle partie, afficher le tableau des scores, et affiche les crédits. Utilise Tkinter pour l'interface graphique.
    """
    global menu_root
    menu_root = Tk()
    menu_root.title("Bataille Navale | NSI")

    menu_root.geometry("970x710")
    menu_root.resizable(False, False)

    if mode == "image":
        bg = PhotoImage(file="img/background-sea-water.png")
        background_label = Label(menu_root, image=bg)
    else:
        background_label = Label(menu_root, bg="#88cffa")
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    title = Label(
        menu_root,
        text="Bataille Navale",
        fg="black",
        font=("Parisine", 60, "normal"),
        bg="#88cffa",
        padx=20,
        pady=20,
    )
    title.pack(pady=50)

    button_frame = Frame(menu_root, bg="#88cffa")
    button_frame.pack()

    new_game = ttk.Button(
        button_frame,
        text="Nouvelle partie",
        command=lambda: [config_game()],
    )

    new_game.grid(row=0, column=0, padx=10, pady=10)

    leaderboard_button = ttk.Button(
        button_frame,
        text="Leaderboard",
        command=lambda: [leaderboard()],
    )

    leaderboard_button.grid(row=0, column=1, padx=10, pady=10)

    nam = Label(
        menu_root,
        text="NSI 2024\n — \n Léo Lesimple, \n Timothée  Gallier et \n Léa Kolmerschlag",
        fg="black",
        font=("Parisine", 15, "normal"),
        bg="#88cffa",
        padx=5,
        pady=10,
    )
    nam.pack(pady=(200, 0))

    menu_root.update_idletasks()
    # screen_width = menu_root.winfo_screenwidth()
    # screen_height = menu_root.winfo_screenheight()
    # x = (screen_width) // 5
    # y = (screen_height) // 5
    # menu_root.geometry("+{}+{}".format(x, y))
    menu_root.mainloop()