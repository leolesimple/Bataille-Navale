from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import *
from end_game import *

# Grille 1 : position bateau j1
# grille 2 : tir j1
# grille 3 : position bateaux j2
# grille 4 : tirs j2

j1 = ""
j2 = ""


def init_joueurs(j_p, j_d):
    """
    Arguments :
        j_p : Nom du joueur principal.
        j_d : Nom du joueur défenseur.
    Retourne : Rien.
    Description : Initialise les variables globales j1 et j2 avec les noms des joueurs.
    """
    global j1, j2
    j1 = j_p
    j2 = j_d


grille = [
    [
        [
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
        ],
        [
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
        ],
    ],
    [
        [
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
        ],
        [
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
        ],
    ],
]

grille_a_zero = grille
etape = 0


def wait_game(j_act: str, j_wait: str, mode: int):
    """
    Arguments :
        j_act : Nom du joueur actuel.
        j_wait : Nom du joueur en attente.
        mode : Mode de jeu (1 pour construction, 2 pour jeu).
    Retourne : Rien.
    Description : Affiche une fenêtre d'attente pour le joueur actuel et prépare le jeu selon le mode.
    """
    global etape
    if j1 == "" and j2 == "":
        init_joueurs(j_act, j_wait)
    elif etape != 0:
        etape = 0
    wait_win = Tk()
    wait_win.title("Ecran d'attente | NSI")
    wait_win.geometry("500x600")

    label1 = Label(wait_win, text=j_act, bg="#88cffa", width=455, height=600)
    label1.place(x=0, y=0)

    if mode == 1:
        mode_name = "Placer"
        content_label = "Commencer par poser vos bateaux sur la grille, \n les longueurs et orientations des bateaux \n sont désignées par le jeu.",
    elif mode == 2:
        mode_name = "Jouer"
        content_label = "C'est à vous de jouer, cliquer sur une case \n pour tirer les bateaux de votre adversaire, \n votre grille de bateau est affichée sur le côté.",

    else:
        print(
            "La fonction `wait_game()` n'a pas bien été appelé, merci de ralncer le jeu !"
        )
        exit()

    title = Label(
        wait_win,
        text=mode_name,
        fg="black",
        font=("Parisine", 45, "normal"),
        bg="#88cffa",
    )
    title.pack(pady=(10, 0))

    expl = Label(
        wait_win,
        text=content_label[0],
        fg="black",
        font=("Parisine", 20, "normal"),
        bg="#88cffa",
    )
    expl.pack(pady=(0, 50))

    j_name = Label(
        wait_win,
        text="Nom du joueur : " + j_act,
        fg="black",
        font=("Parisine", 16, "normal"),
        bg="#88cffa",
    )
    j_name.pack(pady=(0, 15))

    button_frame = Frame(wait_win, bg="#88cffa")
    button_frame.pack()

    new_game = ttk.Button(
        button_frame,
        text="Continuer",
        command=lambda: [wait_win.destroy(), grid_view(mode, j_act, j_wait)],
    )

    new_game.grid(row=0, column=0, padx=10, pady=10)

    wait_win.update_idletasks()
    # screen_width = wait_win.winfo_screenwidth()
    # screen_height = wait_win.winfo_screenheight()
    # x = screen_width // 5
    # y = screen_height // 5
    # wait_win.geometry("+{}+{}".format(x, y))

    wait_win.mainloop()


def grid_view(mode: int, j_act: str, j_wait: str):
    """
    Arguments :
        mode : Mode de jeu (1 ou 2).
        j_act : Nom du joueur actuel.
        j_wait : Nom du joueur en attente.
    Retourne : Rien.
    Description : Crée et affiche la vue du jeu en fonction du mode et des joueurs.
    """
    global j1, j2, etape, button_frame_ag, game_player, title, grille_wait, grille_act, gamer_act
    j_id, j_a_id = "", ""
    game_player = Tk()
    game_player.title("Bataille Navale | NSI")

    screen_height = game_player.winfo_screenheight()

    game_player.geometry("970x710")
    game_player.resizable(False, False)

    background_label = Label(game_player, bg="#88cffa")
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    text_label = Label(game_player, bg="#88cffa")
    text_label.place(x=0, y=0)

    if j_act == j1:
        j_id = 0
        j_a_id = 0
    elif j_act == j2:
        j_id = 1
        j_a_id = 1

    if mode == 1:
        title = Label(
            text_label,
            text="Placez vos bateaux",
            fg="black",
            font=("Parisine", 45, "normal"),
            bg="#88cffa",
        )

        gamer_act = Label(
            text_label,
            text=j_act + " | Bateau n°" + str(long),
            fg="black",
            font=("Parisine", 15, "normal"),
            bg="#88cffa",
        )
    elif mode == 2:
        nb_bateaux_differents = nombre_bateaux(j_id, j_id)
        if nb_bateaux_differents == 0:
            game_player.destroy()
            end_game(j_wait)
            return

        title = Label(
            text_label,
            text="Jouez",
            fg="black",
            font=("Parisine", 45, "normal"),
            bg="#88cffa",
        )

        gamer_act = Label(
            text_label,
            text="Qui joue ? : " + j_act,
            fg="black",
            font=("Parisine", 15, "normal"),
            bg="#88cffa",
        )

        nb_bateaux_label = Label(
            text_label,
            text="Bateaux restants : " + str(nb_bateaux_differents),
            fg="black",
            font=("Parisine", 15, "normal"),
            bg="#88cffa",
        )

        nb_bateaux_label.grid(column=0, row=2, pady=(0, 20))

    title.grid(column=0, row=0, pady=(10, 0))
    gamer_act.grid(column=0, row=1, pady=(0, 20))

    button_frame_ag = Frame(text_label, bg="#88cffb")
    button_frame_ag.grid(column=0, row=2)

    grille_boat_j1 = grille[0][0]
    grille_boat_j2 = grille[1][0]
    grille_tir_j1 = grille[0][1]
    grille_tir_j2 = grille[1][1]

    if mode == 1:
        if j_act == j1:
            grille_act = grille_boat_j1
            grille_wait = grille_boat_j2
        elif j_act == j2:
            grille_act = grille_boat_j2
            grille_wait = grille_boat_j1
    elif mode == 2:
        if j_act == j1:
            grille_act = grille_tir_j2
            grille_wait = grille_boat_j1
        elif j_act == j2:
            grille_act = grille_tir_j1
            grille_wait = grille_boat_j2

    grid_frame = Label(game_player, bg="#88cffb")
    grid_frame.place(x=10, y=150)

    big_grid = Label(grid_frame, bg="#88cffb")
    big_grid.grid(column=0, row=0, pady=10, padx=10)

    small_grid = Label(grid_frame, bg="#88cffb")
    small_grid.grid(column=1, row=0, pady=10, padx=10)

    init_grille([game_player, big_grid, small_grid], mode, grille_act, grille_wait, j_act, j_wait)

    game_player.update_idletasks()
    # screen_width = game_player.winfo_screenwidth()
    # screen_height = game_player.winfo_screenheight()
    # x = screen_width // 5
    # y = screen_height // 5
    # game_player.geometry("+{}+{}".format(x, y))

    game_player.mainloop()


def init_grille(frame: list, mode: int, grille_joueur: list, grille_ad: list, j_act, j_wait):
    """
    Arguments :
        frame : Liste contenant des éléments de l'interface graphique.
        mode : Mode de jeu (1 : construction, 2 : jeu ou 3 : affichage).
        grille_joueur : Grille du joueur actuel.
        grille_ad : Grille de l'adversaire.
        j_act : Nom du joueur actuel.
        j_wait : Nom du joueur en attente.
    Retourne : Rien.
    Description : Initialise la grille de jeu en fonction du mode et des joueurs.
    """
    global etape, long, button_frame_ag, game_player, indice_j_adv
    """
    Initialisation de la grille des bateaux. Grille de 8x8.
    """

    if etape >= 5 and mode != 3:
        init_grille(frame, 3, grille_ad, grille_joueur, j_act, j_wait)
    else:
        print(etape)

    def button_click(row, col):
        global etape
        print(f"Bouton N° R{row}C{col}")
        init_grille(frame, mode, grille_joueur, grille_ad, j_act, j_wait)
        etape += 1

    indice_j_adv = ""
    indice_j_act = ""

    if j_act == j1:
        j_id = 0
    elif j_act == j2:
        j_id = 1

    if j_act == j1:
        indice_j_adv = 1
        indice_j_act = 0
    elif j_act == j2:
        indice_j_adv = 0
        indice_j_act = 1

    if mode == 1:
        for i in range(8):
            for j in range(8):
                if grille_joueur[j][i] is None:
                    bg_color = "#0077BE"
                    text_case = f"{i}-{j}"
                else:
                    bg_color = "#808080"
                    text_case = "B " + str(grille_joueur[j][i])
                grille_init_boat = Canvas(
                    frame[1],
                    width=60,
                    height=60,
                    background=bg_color,
                    highlightthickness=0,
                )
                grille_init_boat.grid(row=i + 1, column=j, padx=2, pady=2)
                grille_init_boat.create_text(
                    25,
                    20,
                    text=text_case,
                    fill="black",
                    font=("Parisine", 15, "normal"),
                    tags="text",
                )
                grille_init_boat.bind(
                    "<Button-1>",
                    lambda event, row=i, col=j: (
                        creation_bateau(j_id, col, long[etape], row, etape),
                        button_click(row, col),
                    ),
                )
    elif mode == 2:
        infos_bateaux = bateau_touche(indice_j_adv)
        cases_touchees = infos_bateaux["touche"]
        cases_coulees = infos_bateaux["coule"]

        for k in range(8):
            for g in range(8):
                if (k, g) in cases_touchees:
                    bg_color = "#00FF00"
                elif (k, g) in cases_coulees:
                    bg_color = "#FF0000"
                else:
                    bg_color = "#AAAAAA"
                game_grid = Canvas(
                    frame[1],
                    width=60,
                    height=60,
                    background=bg_color,
                    highlightthickness=0,
                )
                game_grid.grid(row=k, column=g, padx=2, pady=2)

                coord_text = f"{k}-{g}"
                game_grid.create_text(
                    40,
                    40,
                    text=coord_text,
                    fill="black",
                    font=("Parisine", 12, "normal"),
                    tags="text",
                )

                game_grid.bind(
                    "<Button-1>",
                    lambda event, row=k, col=g: [
                        check_tour(indice_j_adv, indice_j_act, col, row, j_act, j_wait, frame, grille_joueur,
                                   grille_ad)]
                )

        infos_bateaux_j = bateau_touche(indice_j_act)
        cases_perdues = infos_bateaux_j["touche"]
        for s in range(8):
            for w in range(8):
                if grille_ad[w][s] is None:
                    bg_color = "#0077BE"
                elif (s, w) in cases_perdues:
                    bg_color = "#FF0000"
                else:
                    bg_color = "#808080"
                sample_grid = Canvas(
                    frame[2],
                    width=30,
                    height=30,
                    background=bg_color,
                    highlightthickness=0,
                )
                sample_grid.grid(row=s, column=w, padx=2, pady=2)

    elif mode == 3:
        for i in range(8):
            for j in range(8):
                case_value = grille_joueur[j][i]
                if case_value is None:
                    bg_color = "#0077BE"
                    text_case = f"{i}-{j}"
                else:
                    bg_color = "#808080"
                    text_case = "B " + str(case_value)

                grille_init_boat = Canvas(
                    frame[1],
                    width=60,
                    height=60,
                    background=bg_color,
                    highlightthickness=0,
                )
                grille_init_boat.grid(row=i + 1, column=j, padx=2, pady=2)
                grille_init_boat.create_text(
                    25,
                    20,
                    text=text_case,
                    fill="black",
                    font=("Parisine", 20, "normal"),
                    tags="text",
                )
        if j_act != j2:
            continue_btn = ttk.Button(
                button_frame_ag,
                text="Passer au joueur suivant",
                command=lambda: [game_player.destroy(), wait_game(j_wait, j_act, 1)],
            )
        else:
            continue_btn = ttk.Button(
                button_frame_ag,
                text="Jouer",
                command=lambda: [game_player.destroy(), wait_game(j_wait, j_act, 2)],
            )
        continue_btn.grid(row=0, column=1, padx=0, pady=0)


def check_tour(nb_adv: int, nb_act: int, col: int, row: int, next_j: str, nv_wait: str, frames: list,
               grille_joueur: list, grille_ad: list):
    """
    Arguments :
        nb_adv : Identifiant numérique du joueur adverse.
        nb_act : Identifiant numérique du joueur actuel.
        col : Numéro de la colonne sélectionnée.
        row : Numéro de la ligne sélectionnée.
        next_j : Nom du joueur suivant.
        nv_wait : Nom du joueur en attente.
        frames : Eléments de l'interface graphique.
        grille_joueur : Grille du joueur actuel.
        grille_ad : Grille de l'adversaire.
    Retourne : Rien.
    Description : Vérifie le tour et gère les actions selon le tir effectué.
    """
    joueur_actuel = nb_act
    joueur_adverse = nb_adv

    nom_joueur = ""

    if joueur_actuel == 0:
        nom_joueur = j1
    else:
        nom_joueur = j2

    if joueur_actuel == joueur_actuel:
        tir = tirer(nb_adv, nb_act, col, row)

        if not tir:
            case_touchee((col, row), 2, joueur_adverse)
            messagebox.showinfo(title="Tir coulé",
                                message="Le tir a échoué, vous n'êtes pas tombé sur une bonne case !")
            game_player.destroy()
            wait_game(nv_wait, next_j, 2)

        else:
            messagebox.showinfo(title="Tir touché",
                                message="Vous avez touché une partie de bateau ! Vous pouvez rejouer !")
            case_touchee((col, row), 1,
                         joueur_adverse)
            init_grille(frames, 2, grille_joueur, grille_ad, next_j, nv_wait)
            nb_bateaux_differents = nombre_bateaux(joueur_adverse, joueur_adverse)
            if nb_bateaux_differents == 0:
                game_player.destroy()
                messagebox.showinfo(title="Fin du jeu",
                                    message="Tous les bateaux du joueur ont été touchés !")
                end_game(nom_joueur)
                reset()
                return
    else:
        messagebox.showerror(title="Erreur !", message="Une erreur dans l'attribution des tirs !")
        exit()


def longueur_bateau():
    """
    Arguments : Aucun.
    Retourne : Liste des longueurs des bateaux.
    Description : Génère aléatoirement les longueurs des bateaux pour un joueur.
    """
    L_j0 = []
    for i in range(6):
        n = randint(1, 3)
        L_j0.append(n)
    return L_j0


long = longueur_bateau()


def tirer(joueur_actuel: int, joueur_adverse: int, num_col: int, li: int):
    """
    Arguments :
        joueur_actuel : Identifiant du joueur actuel.
        joueur_adverse : Identifiant du joueur adverse.
        num_col : Numéro de la colonne ciblée.
        li : Numéro de la ligne ciblée.
    Retourne : Booléen indiquant si le tir a touché un bateau.
    Description : Effectue un tir et détermine s'il a touché un bateau.
    """
    if grille[joueur_actuel][1][num_col][li] != False and grille[joueur_actuel][0][num_col][li] is not None:
        grille[joueur_actuel][0][num_col][li] = False
        return True
    return False


def vie_bateau(joueur_actuel: int, numero: int):
    """
    Arguments :
        joueur_actuel : Identifiant du joueur actuel.
        numero : Numéro du bateau.
    Retourne : Nombre de points de vie restants du bateau spécifié.
    Description : Calcule la vie restante d'un bateau spécifié.
    """
    vie_bateau = 0
    for i in grille[joueur_actuel]:
        if i == numero:
            vie_bateau += 1
    return vie_bateau


def reset():
    """
    Arguments : Aucun.
    Retourne : Rien.
    Description : Réinitialise la grille de jeu à son état initial.
    """
    global grille
    grille = grille_a_zero


def creation_bateau(num_joueur: int, num_col: int, longueur: int, li: int, num: int):
    """
    Arguments :
        num_joueur : Identifiant du joueur.
        num_col : Numéro de la colonne de départ.
        longueur : Longueur du bateau.
        li : Numéro de la ligne de départ.
        num : Numéro d'étape / identifiant du bateau.
    Retourne : Rien.
    Description : Place un bateau sur la grille du joueur.
    """
    if num % 2 == 0:
        if 7 - num_col >= longueur:
            for i in range(longueur):
                grille[num_joueur][0][num_col][li] = num
                num_col += 1
        else:
            for i in range(longueur):
                grille[num_joueur][0][num_col][li] = num
                num_col -= 1
    else:
        if 7 - li >= longueur:
            for i in range(longueur):
                grille[num_joueur][0][num_col][li] = num
                li += 1
        else:
            for i in range(longueur):
                grille[num_joueur][0][num_col][li] = num
                li -= 1


def nombre_bateaux(joueur_actuel: int, joueur_adverse: int):
    """
    Arguments :
        joueur_actuel : Identifiant du joueur actuel.
        joueur_adverse : Identifiant du joueur adverse.
    Retourne : Nombre de bateaux non coulés du joueur actuel.
    Description : Compte les bateaux non coulés du joueur actuel en fonction des tirs de l'adversaire.
    """

    grille_position = grille[joueur_actuel][0]

    numeros_bateaux = []

    for ligne in grille_position:
        for case in ligne:
            if case is not None and isinstance(case, int) and case not in numeros_bateaux:
                numeros_bateaux.append(case)

    infos_tirs = bateau_touche(joueur_adverse)

    bateaux_non_coules = 0
    for numero in numeros_bateaux:
        toutes_cases_touchees = all(
            coordonnees in infos_tirs["touche"] for coordonnees in cases_du_meme_bateau(numero, joueur_actuel))
        if not toutes_cases_touchees:
            bateaux_non_coules += 1

    return bateaux_non_coules - 1


def cases_du_meme_bateau(numero_bateau: int, joueur_actuel: int):
    """
    Arguments :
        numero_bateau : Numéro du bateau.
        joueur_actuel : Identifiant du joueur actuel.
    Retourne : Liste de coordonnées des cases occupées par le bateau.
    Description : Retourne les coordonnées de toutes les cases occupées par un bateau spécifié.
    """
    coordonnees = []
    for i in range(8):
        for j in range(8):
            if grille[joueur_actuel][0][i][j] == numero_bateau:
                coordonnees.append((i, j))
    return coordonnees


bateaux_touche = {
    0: {"touche": [], "coule": []},
    1: {"touche": [], "coule": []},
}


def case_touchee(coo: tuple, etat: int, joueur: int):
    """
    Arguments :
        coo : Coordonnées de la case.
        etat : État de la case (touche ou coule).
        joueur : Identifiant du joueur.
    Retourne : Rien.
    Description : Met à jour l'état d'une case spécifiée comme touchée ou coulée.
    """
    global bateaux_touche
    if joueur not in bateaux_touche:
        bateaux_touche[joueur] = {"touche": [], "coule": []}

    m_coo = (coo[1], coo[0])
    if etat == 1:
        bateaux_touche[joueur]["touche"].append(m_coo)
    else:
        bateaux_touche[joueur]["coule"].append(m_coo)


def bateau_touche(nb_joueur: int):
    """
    Arguments :
        nb_joueur : Identifiant du joueur.
    Retourne : Dictionnaire des états des bateaux (touchés ou coulés).
    Description : Renvoie l'état actuel des bateaux d'un joueur spécifié.
    """
    return bateaux_touche[nb_joueur]