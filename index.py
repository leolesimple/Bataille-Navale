from tkinter import *
from tkinter import ttk 
import sqlite3
from random import random


grille = [
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None] ]


def longueur_bateau():
    """pour savoir la longueur des bateaux"""
    L = []
    for i in range(6):
        n = random(1,3)
        L.append(n)
    l = L
    return L , l

def select_joueur():
    selectIn = sqlite3.connect('general.db')
    cursor = selectIn.cursor()
    cursor.execute("SELECT nom FROM joueurs")
    player_names = [row[0] for row in cursor.fetchall()]
    selectIn.close()

def changement_de_joueur(joueur):
    return 

def tirer(num_col, li):
    if grille[num_col[li]] != False and grille[num_col[li]] != None :
         grille[num_col[li]] = False
         return True #en gros c'est touche
    return False #en gros t'es nul t'as rate


"""
def commencer_tour():
return mode=2 , list des grilles , joueur actuel , joueur en attente 
"""