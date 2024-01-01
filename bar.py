from tkinter import *
from tkinter import ttk
from menu import *
from leaderboard import *
from pre_game import *
from grille import *
from game import *


def open_menu():
    menu()


def win_reset():
    global j1, j2
    pre_game.destroy()
    wait_win.destroy()
    root.destroy()
    del_win.destroy()
    add_win.destroy()
    init_grid.destroy()
    menu_root.destroy()
    j1 = ""
    j2 = ""
    menu()


def bar():
    bar = Tk()
    bar.title("Shortcuts | NSI")
    button_frame = Frame(bar, bg="#3676a8")
    button_frame.pack()

    menu = ttk.Button(
        button_frame,
        text="Home",
        command=lambda: [open_menu()],
    )

    menu.grid(row=0, column=0, padx=10, pady=10)

    leaderboard_button = ttk.Button(
        button_frame,
        text="Leaderboard",
        command=lambda: [leaderboard()],
    )

    leaderboard_button.grid(row=0, column=1, padx=10, pady=10)

    grille = ttk.Button(
        button_frame,
        text="Grille",
        command=lambda: init_grille(),
    )

    grille.grid(row=0, column=2, padx=10, pady=10)

    pre_game = ttk.Button(
        button_frame,
        text="Pre Game",
        command=lambda: config_game(),
    )

    pre_game.grid(row=0, column=3, padx=10, pady=10)

    game = ttk.Button(
        button_frame,
        text="Game",
        command=lambda: wait_game(),
    )

    game.grid(row=0, column=4, padx=10, pady=10)

    moins = ttk.Button(
        button_frame,
        text="❌ joueur",
        command=lambda: delete_player(),
    )

    moins.grid(row=0, column=5, padx=10, pady=10)

    plus = ttk.Button(
        button_frame,
        text="✅ Joueur",
        command=lambda: add_player(),
    )

    plus.grid(row=0, column=6, padx=10, pady=10)

    c_all = ttk.Button(
        button_frame,
        text="Close Win",
        command=lambda: win_reset(),
    )

    c_all.grid(row=0, column=7, padx=10, pady=10)
    bar.mainloop()
