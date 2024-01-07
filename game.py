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


# mode = 1 -> construction
# mode = 2 -> jeu

def wait_game(j_act, j_wait, mode):
    global etape
    if j1 == "" and j2 == "":
        init_joueurs(j_act, j_wait)
    elif etape != 0:
        etape = 0
    print(j1, j2)
    wait_win = Tk()
    wait_win.title("Ecran d'attente | NSI")
    wait_win.geometry("450x600")
    wait_win.resizable(False, False)

    label1 = Label(wait_win, text=j_act, bg="#88cffa", width=455, height=600)
    label1.place(x=0, y=0)

    if mode == 1:
        mode_name = "Placer"
        content_label = "Commencer par poser vos bateaux sur la grille, \n les longueurs et orientations des bateaux \n sont désignées pas le jeu.",
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
        font=("Parisine", 45),
        bg="#88cffa",
    )
    title.pack(pady=(10, 0))

    expl = Label(
        wait_win,
        text=content_label[0],
        fg="black",
        font=("Parisine", 20),
        bg="#88cffa",
    )
    expl.pack(pady=(0, 50))

    j_name = Label(
        wait_win,
        text="Nom du joueur : " + j_act,
        fg="black",
        font=("Parisine", 16),
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
    screen_width = wait_win.winfo_screenwidth()
    screen_height = wait_win.winfo_screenheight()
    x = screen_width // 5
    y = screen_height // 5
    wait_win.geometry("+{}+{}".format(x, y))

    wait_win.mainloop()


etape = 0


def grid_view(mode, j_act, j_wait):
    global j1, j2, etape, button_frame_ag, game_player, title, grille_wait, grille_act, gamer_act
    j_id, j_a_id = "", ""
    game_player = Tk()
    game_player.title("Bataille Navale | NSI")

    screen_height = game_player.winfo_screenheight()

    if screen_height < 854:
        game_player.geometry("1080x724")
    else:
        game_player.geometry("1280x854")
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
            font=("Parisine", 45),
            bg="#88cffa",
        )

        gamer_act = Label(
            text_label,
            text=j_act + " | Bateau n°" + str(long),
            fg="black",
            font=("Parisine", 15),
            bg="#88cffa",
        )
    elif mode == 2:
        print(str(j_id) + " " + str(j_a_id))
        nb_bateaux_differents = nombre_bateaux(j_id, j_id)
        if nb_bateaux_differents == 0:
            game_player.destroy()
            end_game(j_wait)
            return

        title = Label(
            text_label,
            text="Jouez",
            fg="black",
            font=("Parisine", 45),
            bg="#88cffa",
        )

        gamer_act = Label(
            text_label,
            text="Qui joue ? : " + j_act,
            fg="black",
            font=("Parisine", 15),
            bg="#88cffa",
        )

        nb_bateaux_label = Label(
            text_label,
            text="Bateaux restants : " + str(nb_bateaux_differents),
            fg="black",
            font=("Parisine", 15),
            bg="#88cffa",
        )

        nb_bateaux_label.grid(column=0, row=2, pady=(0, 20))

    title.grid(column=0, row=0, pady=(10, 0))
    gamer_act.grid(column=0, row=1, pady=(0, 20))

    button_frame_ag = Frame(text_label, bg="#88cffb")
    button_frame_ag.grid(column=0, row=2)

    # Grille 1 : position bateau j1
    # grille 2 : tir j1
    # grille 3 : position bateaux j2
    # grille 4 : tirs j2

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
    screen_width = game_player.winfo_screenwidth()
    screen_height = game_player.winfo_screenheight()
    x = (screen_width) // 5
    y = (screen_height) // 5
    game_player.geometry("+{}+{}".format(x, y))

    game_player.mainloop()


# Mode : 1 = Création Bateau (grille unique)
#        2 = Jeu bateau (grille double)
#        3 = Affichage de la grille du joueur.

def init_grille(frame: list, mode: int, grille_joueur: list, grille_ad: list, j_act, j_wait):
    global etape, long, button_frame_ag, game_player, indice_j_adv
    """
    Initialisation de la grille des bateaux. Grille de 8x8.
    """

    if etape >= 5 and mode != 3:
        # frame_1 = frame[1]
        # frame_1.destroy()

        init_grille(frame, 3, grille_ad, grille_joueur, j_act, j_wait)
        print(grille_joueur)
    else:
        print(etape)

    def button_click(row, col):
        global etape
        print(f"Bouton N° R{row}C{col}")
        init_grille(frame, mode, grille_joueur, grille_ad, j_act, j_wait)
        etape += 1
        print("Etape : " + str(etape))

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
        print('Mode 1')
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
                    width=100,
                    height=80,
                    background=bg_color,
                    highlightthickness=0,
                )
                grille_init_boat.grid(row=i + 1, column=j, padx=2, pady=2)
                grille_init_boat.create_text(
                    25,
                    20,
                    text=text_case,
                    fill="black",
                    font=("Parisine", 20),
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
        print("Mode 2" + " Joueur Actuel : " + str(j_act) + "Joueur Attente : " + str(j_wait))
        # Appel à bateau_touche pour obtenir les informations sur les cases touchées et coulées
        infos_bateaux = bateau_touche(indice_j_adv)
        cases_touchees = infos_bateaux["touche"]
        cases_coulees = infos_bateaux["coule"]

        # Grande Grille
        for k in range(8):
            for g in range(8):
                if (k, g) in cases_touchees:
                    bg_color = "#00FF00"  # Case touchée
                elif (k, g) in cases_coulees:
                    bg_color = "#FF0000"  # Case coulée
                else:
                    bg_color = "#AAAAAA"  # Case non cliquée
                game_grid = Canvas(
                    frame[1],
                    width=80,
                    height=80,
                    background=bg_color,
                    highlightthickness=0,
                )
                game_grid.grid(row=k, column=g, padx=2, pady=2)

                # Ajouter les coordonnées de la case
                coord_text = f"{k}-{g}"
                game_grid.create_text(
                    40,
                    40,
                    text=coord_text,
                    fill="black",
                    font=("Arial", 12),
                    tags="text",
                )

                game_grid.bind(
                    "<Button-1>",
                    lambda event, row=k, col=g: [
                        check_tour(indice_j_adv, indice_j_act, col, row, j_act, j_wait, frame, grille_joueur,
                                   grille_ad)]
                )

        # Petite grille
        for s in range(8):
            for w in range(8):
                if grille_ad[w][s] is None:
                    bg_color = "#0077BE"
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
        print("Mode : 3")
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
                    width=100,
                    height=80,
                    background=bg_color,
                    highlightthickness=0,
                )
                grille_init_boat.grid(row=i + 1, column=j, padx=2, pady=2)
                grille_init_boat.create_text(
                    25,
                    20,
                    text=text_case,
                    fill="black",
                    font=("Parisine", 20),
                    tags="text",
                )
                grille_init_boat.bind(
                    "<Button-1>",
                    lambda event, row=i, col=j: (print("Clic inactif")),
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


def check_tour(nb_adv, nb_act, col, row, next_j, nv_wait, frames, grille_joueur, grille_ad):
    joueur_actuel = nb_act
    joueur_adverse = nb_adv

    # Vérifier que le joueur actuel est autorisé à tirer
    if joueur_actuel == joueur_actuel:
        tir = tirer(nb_adv, nb_act, col, row)
        print("tirer(" + str(nb_adv) + ", " + str(nb_act) + ", " + str(col) + ", " + str(row) + ")")
        n_boat = grille_ad[col][row]

        if not tir:
            messagebox.showinfo(title="Tir coulé",
                                message="Le tir a échoué, vous n'êtes pas tombé sur une bonne case !")
            game_player.destroy()
            wait_game(nv_wait, next_j, 2)
            case_touchee((col, row), 2, joueur_adverse)

        else:
            messagebox.showinfo(title="Tir touché",
                                message="Vous avez touché une partie de bateau ! Vous pouvez rejouer !")
            case_touchee((col, row), 1,
                         joueur_adverse)
            init_grille(frames, 2, grille_joueur, grille_ad, next_j, nv_wait)
            pv_bateau = vie_bateau(joueur_adverse, n_boat)

            if pv_bateau == 0:
                messagebox.showinfo(title="Coulé !", message=f"Le bateau {n_boat} a été coulé !")
    else:
        messagebox.showerror(title="Erreur !", message="Une erreur dans l'attribution des tirs !")


# Léa

def longueur_bateau():
    """pour savoir la longueur des bateaux"""
    L_j0 = []
    for i in range(6):
        n = randint(1, 3)
        L_j0.append(n)
    return L_j0


long = [1, 2, 1, 2, 1, 2]  # longueur_bateau()


def changement_de_joueur(joueur_actuel, joueur_prochain):
    # Intégrée dans le code définitif.
    joueur_pro, joueur_act = joueur_actuel, joueur_prochain
    return joueur_act, joueur_pro


# def tirer(joueur_actuel, joueur_adverse, num_col, li):
"""Retourne si le tir a touche ou non
    Prend en parametre la grille du joueur adverse,
    le num de la colonne et de la ligne ou il tire
    il retourne True si le tir a touche et false sinon"""
"""     if (
        grille[joueur_adverse][0][num_col][li] != False
        and grille[joueur_adverse][0][num_col][li] != None
    ):
        grille[joueur_actuel][1][num_col][li] = True
        return True  # en gros c'est touche
    return False  # en gros t'es nul t'as rate """


def tirer(joueur_actuel, joueur_adverse, num_col, li):
    """Retourne si le tir a touche ou non
    Prend en parametre la grille du joueur adverse,
    le num de la colonne et de la ligne ou il tire
    il retourne True si le tir a touche et false sinon"""
    if grille[joueur_actuel][1][num_col][li] != False and grille[joueur_actuel][0][num_col][li] is not None:
        grille[joueur_actuel][0][num_col][li] = False
        # grille[joueur_actuel][1][num_col][li] = True
        return True
    # grille[joueur_actuel][1][num_col][li] = False
    return False


def vie_bateau(joueur_actuel, numero):
    """renvoie la vie d'un bateau specifie par son numero entre en parametre
    Prend en parametre le joueur actuel et renvoie les pv du bateau specifie"""
    vie_bateau = 0
    for i in grille[joueur_actuel]:
        if i == numero:
            vie_bateau += 1
    return vie_bateau


def reset():
    global grille
    """reinitialise la grille a 0"""
    grille = grille_a_zero


def commencer_tour(joueur_actuel, joueur_prochain, grille):
    # Intégré dans le wait_game
    """Renvoie une fonction avec comme arguments :
    - le mode
    - la grille de l'adversaire
    - la grille du joueur actuel avec ses bateaux
    - le joueur qui joue
    - le joueur en attente"""
    return


def deroulement_tour(joueur_actuel, joueur_prochain):
    # Déplacé dans les fonctions wait_game(), etc.

    """deroulement d'un tour"""
    if nombre_bateaux(joueur_actuel, joueur_prochain) == 0:
        return 0  # fin jeu
    # ecran noir avec bouton pourconfirmer qu'il change de joueur (Léo -> Interface)
    # apparition de la grille du joueur et celle dans lequel il tire (Léo -> Interface)
    # clique sur une case de la grille dans lequel il tire (celle ci sera dans une variable qui sera utilise pour la fonction tirer) (Léo -> Interface)
    tirer(joueur_actuel, joueur_prochain, """case cliquee""")
    if nombre_bateaux(joueur_prochain, joueur_actuel) == 0:
        return 0  # fin jeu
    # afficher pendant un certain temps l'ecran (Léo -> Interface)
    # mettre ecran noir (Léo -> Interface)
    deroulement_tour(changement_de_joueur(joueur_actuel, joueur_prochain))


# Timothée


def creation_bateau(num_joueur, num_col, longueur, li, num):
    """renvoie la grille avec les numeros des bateaux, et si ya rien bah cest none
    Prend en parametre :
    - num du joueur (0 ou 1) qui definit quelle liste de liste prendre
    - num colonne pour la 1ere sousliste definissant les colonnes
    - li pour la 2e sous liste definissant les lignes
    - longueur qui sera la longueur du bateau
    - num qui correspont a l'etape et au numero du bateau"""
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


def nombre_bateaux(joueur_actuel, joueur_adverse):
    """Compte le nombre de bateaux non coulés du joueur actuel en utilisant la grille de position
    et les informations sur les tirs du joueur adverse."""

    # Obtenez la grille de position des bateaux du joueur actuel
    grille_position = grille[joueur_actuel][0]

    # Initialisez une liste vide pour stocker les numéros de bateaux
    numeros_bateaux = []

    # Parcourez la grille de position et ajoutez les numéros de bateaux à la liste
    for ligne in grille_position:
        for case in ligne:
            if case is not None and isinstance(case, int) and case not in numeros_bateaux:
                numeros_bateaux.append(case)

    # Obtenez les informations sur les tirs du joueur adverse
    infos_tirs = bateau_touche(joueur_adverse)

    # Parcourez les numéros de bateaux et vérifiez s'ils ont toutes leurs cases touchées
    bateaux_non_coulés = 0
    for numero in numeros_bateaux:
        toutes_cases_touchees = all(
            coordonnees in infos_tirs["touche"] for coordonnees in cases_du_meme_bateau(numero, joueur_actuel))
        if not toutes_cases_touchees:
            bateaux_non_coulés += 1

    return bateaux_non_coulés - 1


def cases_du_meme_bateau(numero_bateau, joueur_actuel):
    """Retourne les coordonnées (ligne, colonne) de toutes les cases du même bateau."""
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


def case_touchee(coo: tuple, etat, joueur):
    global bateaux_touche
    if joueur not in bateaux_touche:
        bateaux_touche[joueur] = {"touche": [], "coule": []}

    m_coo = (coo[1], coo[0])
    if etat == 1:
        bateaux_touche[joueur]["touche"].append(m_coo)
    elif etat == 2:
        bateaux_touche[joueur]["coule"].append(m_coo)


def bateau_touche(nb_joueur):
    print(nb_joueur)
    print(bateaux_touche[nb_joueur])
    return bateaux_touche[nb_joueur]