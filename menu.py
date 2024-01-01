from pre_game import *
import tkinter as tk
from tkinter import ttk
from leaderboard import *


def menu(type="color"):
    global menu_root
    """
    Fenêtre d'accueil du jeu de la Bataille Navale.
    """
    menu_root = Tk()
    menu_root.title("Bataille Navale | NSI")

    screen_height = menu_root.winfo_screenheight()

    if screen_height < 854:
        menu_root.geometry("1080x724")
    else:
        menu_root.geometry("1280x854")
    menu_root.resizable(False, False)

    if type == "image" :
        bg = PhotoImage(file="img/background-sea-water.png")
        background_label = Label(menu_root, image=bg)
    else : 
        background_label = Label(menu_root, bg = "#88cffa")
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    title = Label(
        menu_root,
        text="Bataille Navale",
        fg="black",
        font=("Parisine", 70),
        bg="#3676a8",
        padx=20,
        pady=20,
    )
    title.pack(pady=50)

    button_frame = Frame(menu_root, bg="#3676a8")
    button_frame.pack()

    new_game = ttk.Button(
        button_frame,
        text="Nouvelle partie",
        command=lambda:(menu_root.destroy(), config_game()),
    )

    new_game.grid(row=0, column=0, padx=10, pady=10)

    leaderboard_button = ttk.Button(
        button_frame,
        text="Leaderboard",
        command=lambda:[leaderboard()],
    )

    leaderboard_button.grid(row=0, column=1, padx=10, pady=10)

    menu_root.update_idletasks()
    screen_width = menu_root.winfo_screenwidth()
    screen_height = menu_root.winfo_screenheight()
    x = (screen_width) // 5
    y = (screen_height) // 5
    menu_root.geometry("+{}+{}".format(x, y))
    bar()
    menu_root.mainloop()

from bar import *