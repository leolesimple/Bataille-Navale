import sqlite3
from tkinter import *
from tkinter import ttk
from game import *


def error_gamer(case: int):
    """
    Arguments :
        case: Numéro indiquant le type d'erreur à afficher.
    Retourne : Rien.
    Description : Affiche un message d'erreur spécifique en fonction du cas indiqué et termine le programme. Utilisé pour gérer les erreurs dans le choix des joueurs pour une partie de jeu.
    """
    from tkinter import messagebox

    if case == 1:
        messagebox.showerror(
            "Les joueurs doivent être rempli pour commencer la partie !"
        )
    elif case == 2:
        messagebox.showerror(
            "Les joueurs doivent être différents pour commencer la partie !"
        )
    exit()


def config_game():
    """
    Arguments : Aucun.
    Retourne : Rien.
    Description : Crée une fenêtre de configuration pour une nouvelle partie de jeu, permettant de sélectionner les joueurs parmi une liste obtenue de la base de données. Affiche les options pour commencer la partie ou l'annuler. Utilise Tkinter pour l'interface graphique.
    """

    def select_gamers():
        """
        Arguments :
            Aucun, utilisations des variables de config_game().
        Retourne : Rien.
        Description : Fonction interne de `config_game` permettant de sélectionner les joueurs pour une nouvelle partie. Vérifie que les noms des joueurs sont différents et non vides, affiche des messages d'erreur si nécessaire, et configure le bouton de démarrage du jeu. Utilise des variables non locales pour accéder aux informations de l'interface graphique Tkinter.
        """
        nonlocal name_j1_list, name_j2_list, player_names, button_frame, player_ids, pre_game, new_game, annul_button
        value_combo_j1 = name_j1_list.get()
        j1 = value_combo_j1
        value_combo_j2 = name_j2_list.get()
        j2 = value_combo_j2
        assert j1 != "" and j2 != "", error_gamer(1)
        if j1 == j2:
            error_gamer(2)
        else:
            new_game.destroy()
            annul_button.destroy()
            start = ttk.Button(
                button_frame,
                text="Commencer",
                command=lambda: [pre_game.destroy(), wait_game(j1, j2, 1)],
            )
            start.grid(row=0, column=0, padx=10, pady=10)

    pre_game = Tk()
    pre_game.title("Configuration du jeu | NSI")
    screen_height = pre_game.winfo_screenheight()

    if screen_height < 854:
        pre_game.geometry("1080x724")
    else:
        pre_game.geometry("1280x854")

    pre_game.resizable(False, False)

    background_label = Label(pre_game, bg="#88cffa")
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    title = Label(
        pre_game,
        text="Nouvelle partie",
        fg="black",
        font=("Parisine", 45, "normal"),
        bg="#88cffa",
    )
    title.pack(pady=(50, 0))
    disclaimer = Label(
        pre_game,
        text="Si votre nom/pseudo n'apparaît pas dans les listes, \n accédez au leaderboard pour créer votre joueur.",
        fg="black",
        font=("Parisine", 20, "normal"),
        bg="#88cffa",
        padx=0,
        pady=0,
    )
    disclaimer.pack(pady=(0, 50))

    selectIn = sqlite3.connect("general.db")
    cursor = selectIn.cursor()
    cursor.execute("SELECT nom,id FROM joueurs")
    player_names = [row[0] for row in cursor.fetchall()]
    player_ids = [row[1] for row in cursor.fetchall()]
    selectIn.close()

    name_j1 = Label(pre_game, text="Premier joueur :", bg="#88cffa", padx=10, pady=10)
    name_j1.pack()

    name_j1_list = ttk.Combobox(pre_game, values=player_names)
    name_j1_list.pack()

    name_j2 = Label(pre_game, text="Deuxième joueur :", bg="#88cffa", padx=10, pady=10)
    name_j2.pack()

    name_j2_list = ttk.Combobox(pre_game, values=player_names, background="#88cffa")
    name_j2_list.pack()

    button_frame = Frame(pre_game, bg="#88cffa")
    button_frame.pack()

    new_game = ttk.Button(
        button_frame,
        text="Continuer",
        command=lambda: select_gamers(),
    )

    new_game.grid(row=0, column=0, padx=10, pady=10)

    annul_button = ttk.Button(
        button_frame,
        text="Annuler",
        command=lambda: [exit()],
    )

    annul_button.grid(row=0, column=1, padx=10, pady=10)

    pre_game.update_idletasks()
    # screen_width = pre_game.winfo_screenwidth()
    # screen_height = pre_game.winfo_screenheight()
    # x = screen_width // 5
    # y = screen_height // 5
    # pre_game.geometry("+{}+{}".format(x, y))
    pre_game.mainloop()