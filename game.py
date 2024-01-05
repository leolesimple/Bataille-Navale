from stock_var import *
from tkinter import *
from tkinter import ttk
from random import *

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
        content_label = (
            "Commencer par poser vos bateaux sur la grille, \n les longueurs et orientations des bateaux \n sont désignées pas le jeu.",
        )
    elif mode == 2:
        mode_name = "Jouer"
        content_label = (
            "C'est à vous de jouer, cliquer sur une case \n pour tirer les bateaux de votre adversaire, \n votre grille de bateau est affichée sur le côté.",
        )
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
        text=content_label,
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
    x = (screen_width) // 5
    y = (screen_height) // 5
    wait_win.geometry("+{}+{}".format(x, y))

    wait_win.mainloop()


etape = 0


def grid_view(mode, j_act, j_wait):
    global j1, j2, etape, button_frame_ag, game_player
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

    if mode == 1 :
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
    elif mode == 2 : 
        title = Label(
            text_label,
            text="Jouez ",
            fg="black",
            font=("Parisine", 45),
            bg="#88cffa",
        )

        gamer_act = Label(
            text_label,
            text="Qui joue ? : "+j_act,
            fg="black",
            font=("Parisine", 15),
            bg="#88cffa",
        )
        
    title.grid(column=0, row=0,pady=(10, 0))
    gamer_act.grid(column=0, row=1,pady=(0, 20))

    button_frame_ag = Frame(text_label, bg="#88cffb" )
    button_frame_ag.grid(column=0, row=2)

    # Grille 1 : position bateau j1
    # grille 2 : tir j1
    # grille 3 : position bateaux j2
    # grille 4 : tirs j2

    grille_boat_j1 = grille[0][0]
    grille_boat_j2 = grille[1][0]
    grille_tir_j1 = grille[0][1]
    grille_tir_j2 = grille[1][1]

    if j_act == j1:
        grille_act = grille_boat_j1
        grille_wait = grille_boat_j2
    elif j_act == j2:
        grille_act = grille_boat_j2
        grille_wait = grille_boat_j1

    print(j1 + " j_wait: " + j2)
    grid_frame = Label(game_player)
    grid_frame.place(x=50, y=150)

    init_grille([game_player, grid_frame], mode, grille_act, grille_wait, j_act, j_wait)

    game_player.update_idletasks()
    screen_width = game_player.winfo_screenwidth()
    screen_height = game_player.winfo_screenheight()
    x = (screen_width) // 5
    y = (screen_height) // 5
    game_player.geometry("+{}+{}".format(x, y))

    game_player.mainloop()



# Mode : 1 = Création Bateau (grille unique)
#        2 = Jeu bateau (grille double)

def init_grille(frame, mode, grille_joueur, grille_ad, j_act, j_wait):
    global etape, long, button_frame_ag, game_player
    print(grille_joueur)
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
        init_grille(frame, mode, grille_joueur,grille_ad, j_act, j_wait)
        etape += 1
        print("Etape : " + str(etape))

    if j_act == j1:
        j_id = 0
    elif j_act == j2:
        j_id = 1

    if mode == 1:
        
        for i in range(8):
            for j in range(8):
                if grille_joueur[j][i] == None:
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
        return
    elif mode == 3:
        print("Mode : 3")
        for i in range(8):
            for j in range(8):
                case_value = grille_joueur[i][j] 
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
                    text=f"{i}-{j}",
                    fill="black",
                    font=("Parisine", 20),
                    tags="text",
                )
                grille_init_boat.bind(
                    "<Button-1>",
                    lambda event, row=i, col=j: (print("Clic inactif")),
                )
        if j_act != j2 :
            continue_btn = ttk.Button(
                button_frame_ag,
                text="Passer au joueur suivant",
                command=lambda: [game_player.destroy(), wait_game(j_wait, j_act, 1)],
            )
        else : 
            continue_btn = ttk.Button(
                button_frame_ag,
                text="Jouer",
                command=lambda: [game_player.destroy(), wait_game(j_wait, j_act, 2)],
            )
        continue_btn.grid(row=0, column=1, padx=0, pady=0)


# Léa


def longueur_bateau():
    """pour savoir la longueur des bateaux"""
    L_j0 = []
    for i in range(6):
        n = randint(1, 3)
        L_j0.append(n)
    return L_j0

long = longueur_bateau()

def changement_de_joueur(joueur_actuel, joueur_prochain):
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
    if (
        grille[joueur_adverse][0][num_col][li] != False
        and grille[joueur_adverse][0][num_col][li] != None
    ):
        grille[joueur_adverse][0][num_col][li] = False
        grille[joueur_actuel][1][num_col][
            li
        ] = True  # la grille de tir du joueur montre qu'il a touche
        return True  # en gros c'est touche
    grille[joueur_actuel][1][num_col][
        li
    ] = False  # la grille de tir du joueur montre qu'il a rate
    return False  # en gros t'es nul t'as rate


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
    """Renvoie une fonction avec comme arguments :
    - le mode
    - la grille de l'adversaire
    - la grille du joueur actuel avec ses bateaux
    - le joueur qui joue
    - le joueur en attente"""
    reset()
    j1 = joueur_actuel
    j2 = joueur_prochain
    return init_grille(2, grille[joueur_prochain], grille[joueur_actuel][0], j1, j2)


def deroulement_tour(joueur_actuel, joueur_prochain):
    """deroulement d'un tour"""
    if nombre_bateaux(joueur_actuel) == 0:
        return 0  # fin jeu
    # ecran noir avec bouton pourconfirmer qu'il change de joueur
    # apparition de la grille du joueur et celle dans lequel il tire
    # clique sur une case de la grille dans lequel il tire (celle ci sera dans une variable qui sera utilise pour la fonction tirer)
    tirer(joueur_actuel, joueur_prochain, """case cliquee""")
    if nombre_bateaux(joueur_prochain) == 0:
        return 0  # fin jeu
    # afficher pendant un certain temps l'ecran
    # mettre ecran noir
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


def nombre_bateaux(joueur_actuel):
    """Renvoie le nombre de bateaux differents restants
    Prend en parametre le joueur actuel et renvoie le nombre de bateau dans
    la liste (sa grille) qui lui est attribuee"""
    bateaux_differents = []
    for i in range(grille[joueur_actuel][0]):
        for num in i:
            if num not in bateaux_differents:
                bateaux_differents.append(num)
    return len(bateaux_differents)


def bateau_touche(joueur_adverse):
    """Retourne un dico avec les coo des cases touchees et cases coulees
    PDV du joueur actuel, la grille sera la grille de tir du joueur actuel"""
    coo_touchees = []
    coo_coulees = []
    for i in grille[joueur_adverse][0]:
        for k in i:
            if k == False:
                coo_touchees.append(tuple(k, i))
            elif k == True:
                coo_coulees.append(tuple(k, i))
    dico = {"touche": coo_touchees, "coule": coo_coulees}
    return dico


def vie_bateau(joueur_actuel, numero):
    """renvoie la vie d'un bateau specifie par son numero entre en parametre
    Prend en parametre le joueur actuel et renvoie les pv du bateau specifie"""
    vie_bateau = 0
    for i in grille[joueur_actuel][0]:
        if i == numero:
            vie_bateau += 1
    return vie_bateau


def reset():
    """reinitialise la grille a 0"""
    grille = grille_a_zero
