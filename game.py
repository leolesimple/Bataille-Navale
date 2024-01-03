from stock_var import *
from tkinter import *
from tkinter import ttk
from grille import *

# mode = 1 -> construction
# mode = 2 -> jeu


def wait_game(j_act, mode):
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
    title.pack(pady=(50, 0))

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
        command=lambda: [wait_win.destroy(), grid_view("image", mode, j_act)],
    )

    new_game.grid(row=0, column=0, padx=10, pady=10)

    wait_win.update_idletasks()
    screen_width = wait_win.winfo_screenwidth()
    screen_height = wait_win.winfo_screenheight()
    x = (screen_width) // 5
    y = (screen_height) // 5
    wait_win.geometry("+{}+{}".format(x, y))

    wait_win.mainloop()


def grid_view(type, mode, j_act):
    global j1,j2
    game_player = Tk()
    game_player.title("Bataille Navale | NSI")

    screen_height = game_player.winfo_screenheight()

    if screen_height < 854:
        game_player.geometry("1080x724")
    else:
        game_player.geometry("1280x854")
    game_player.resizable(False, False)

    if type == "image":
        bg = PhotoImage(file="img/background-sea-water.png")
        background_label = Label(game_player, image=bg)
    else:
        background_label = Label(game_player, bg="#88cffa")
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    while j1 == "" or j2 == "":
        from stock_var import j1,j2
    if j_act == j1 :
        j_wait = j2
        grille_act = grille[0]
        grille_wait = grille[1]
    else :
        j_wait = j1
        grille_act = grille[1]
        grille_wait = grille[0]

    print(j1 + " j_wait: " + j2)
    grid_frame = Label(game_player)
    grid_frame.place(x=0, y=0, relwidth=1, relheight=1)

    init_grille([game_player,grid_frame], mode, grille_act, grille_wait, j_act, j_wait)

    game_player.update_idletasks()
    screen_width = game_player.winfo_screenwidth()
    screen_height = game_player.winfo_screenheight()
    x = (screen_width) // 5
    y = (screen_height) // 5
    game_player.geometry("+{}+{}".format(x, y))

    game_player.mainloop()



# Mode : 1 = Création Bateau (grille unique)
#        2 = Jeu bateau (grille double)
def init_grille(frame, mode, grille_ad, grille_joueur, j_act, j_wait):
    """
    Initialisation de la grille des bateaux. Grille de 8x8.
    """
    etape = 0

    def button_click(row, col):
        nonlocal etape
        print(f"Button clicked at row {row}, column {col}")
        etape += 1
        if etape > 6:
            frame[1].destroy()

            button_frame = Frame(frame[0], bg="#88cffa")
            button_frame.pack()

            new_game = ttk.Button(
                button_frame,
                text="Partie terminée",
                command=lambda: [frame[0].destroy(), wait_game(j_wait,1)],
            )

            new_game.grid(row=0, column=0, padx=10, pady=10)

    for i in range(8):
        for j in range(8):
            grille_init_boat = Canvas(
                frame[1],
                width=100,
                height=80,
                background="#AAE0FE",
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
                lambda event, row=i, col=j: (
                    creation_bateau(j_act, col, row, longueur_bateau(), etape),
                    button_click(row, col),
                ),
            )


def creation_bateau(joueur_act, col, li, longueur, num):
    print(joueur_act, col, li, longueur, num)
