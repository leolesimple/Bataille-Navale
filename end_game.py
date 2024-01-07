from tkinter import *
import pyglet


def jouer_son():
    player = pyglet.media.Player()

    sound_file = "sounds/ambience.wav"
    source = pyglet.media.StaticSource(pyglet.media.load(sound_file))

    # Queue the source to the player
    player.queue(source)

    # Play the sound
    player.play()


def end_game(winner):
    end_win = Tk()
    end_win.title("Fin du jeu")

    # Configuration de la couleur de fond
    end_win.configure(bg="#0077BE")

    # Création d'un label pour afficher "Fin du jeu" en grand
    label = Label(end_win, text="Fin du jeu", font=("Parisine", 40), bg="#0077BE", fg="white")
    label.pack(padx=20, pady=20)

    end_win.mainloop()