import pyglet
from leaderboard import *
import sqlite3


def jouer_son():
    """
    !!! Ne fonctionne pas pour le moment !!!
    Arguments : Aucun.
    Retourne : Rien.
    Description : Joue un fichier sonore 'ambience.wav' en utilisant la bibliothèque pyglet. Crée un lecteur de média, charge la source sonore et la joue.
    """
    player = pyglet.media.Player()

    son = "sounds/ambience.wav"
    src = pyglet.media.StaticSource(pyglet.media.load(son))

    player.queue(src)

    player.play()


def end_game(winner: str):
    """
    Arguments :
        winner : Nom du joueur gagnant.
    Retourne : Rien.
    Description : Affiche une fenêtre Tkinter annonçant la fin du jeu et le nom du gagnant. Met à jour le score du joueur gagnant dans une base de données SQLite.
    Propose des boutons pour terminer le jeu ou afficher le leaderboard.
    """
    end_win = Tk()
    end_win.title("Fin du jeu")
    screen_height = end_win.winfo_screenheight()

    if screen_height < 854:
        end_win.geometry("1080x724")
    else:
        end_win.geometry("1280x854")

    end_win.configure(bg="#88cffb")

    label = Label(end_win, text="Fin du jeu", font=("Parisine", 40), bg="#88cffb", fg="black")
    label.pack(padx=20, pady=20)

    label = Label(end_win, text="Gagnant : " + str(winner), font=("Parisine", 20), bg="#88cffb", fg="black")
    label.pack(padx=20, pady=20)

    score_conn = sqlite3.connect('general.db')
    cursor = score_conn.cursor()
    query = f"UPDATE joueurs SET score = score + 10 WHERE nom = '{winner}'"
    cursor.execute(query)
    score_conn.commit()
    score_conn.close()

    label = Label(end_win, text="Votre score a augmenté de 10 points (10 points = 1 partie gagnée)",
                  font=("Parisine", 15), bg="#88cffb", fg="black")
    label.pack(padx=20, pady=20)

    button_frame = Frame(end_win, bg="#88cffa")
    button_frame.pack()

    stop_game = ttk.Button(
        button_frame,
        text="Terminer",
        command=lambda: [exit()],
    )

    stop_game.grid(row=0, column=0, padx=10, pady=10)

    leaderboard_button = ttk.Button(
        button_frame,
        text="Leaderboard",
        command=lambda: [leaderboard()],
    )

    leaderboard_button.grid(row=0, column=1, padx=10, pady=10)

    end_win.mainloop()