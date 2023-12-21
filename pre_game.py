from tkinter import *
from tkinter import ttk

def debut_partie():
    return 1

def config_game():
    """
        Fenêtre de "configuration du jeu' --> choix des joueurs et initialisation des positions de bateaux.
    """
    pre_game = Tk()
    pre_game.title("Configuration du jeu | NSI")
    pre_game.geometry("1280x854")
    pre_game.resizable(False, False)

    bg = PhotoImage(file="img/background-sea-water.png")

    background_label = Label(pre_game, image=bg)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    title = Label(pre_game, text="Nouvelle partie", fg="black", font=("Parisine", 45), bg="#3676a8", padx=20, pady=20)
    title.pack(pady=50)

    button_frame = Frame(pre_game, bg="#3676a8")
    button_frame.pack()

    new_game = ttk.Button(
        button_frame,
        text='Continuer',
        command=lambda: debut_partie(),
    )

    new_game.grid(row=0, column=0, padx=10, pady=10)

    annul_button = ttk.Button(
        button_frame,
        text='Annuler',
        command=lambda: new_game.destroy(),
    )

    annul_button.grid(row=0, column=1, padx=10, pady=10)

    pre_game.update_idletasks()
    screen_width = pre_game.winfo_screenwidth()
    screen_height = pre_game.winfo_screenheight()
    x = (screen_width) // 7
    y = (screen_height) // 7
    pre_game.geometry("+{}+{}".format(x, y))
    pre_game.mainloop()