from tkinter import *
from tkinter import ttk 
import sqlite3
from random import random


grille = [[
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None] ],
[
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None] ]]

grille_a_zero = grille


def longueur_bateau():
    """pour savoir la longueur des bateaux"""
    L_j0 = []
    for i in range(6):
        n = random(1,3)
        L_j0.append(n)
    L_j1 = L_j0
    return L_j0 , L_j1

def select_joueur():
    selectIn = sqlite3.connect('general.db')
    cursor = selectIn.cursor()
    cursor.execute("SELECT nom FROM joueurs")
    player_names = [row[0] for row in cursor.fetchall()]
    selectIn.close()

def changement_de_joueur(joueur_actuel,joueur_prochain):
    return joueur_prochain,joueur_actuel

def tirer(joueur_adverse,num_col, li):
    """Retourne si le tir a touche ou non
    Prend en parametre la grille du joueur adverse,
    le num de la colonne et de la ligne ou il tire
    il retourne True si le tir a touche et false sinon"""
    if grille[joueur_adverse][num_col][li] != False and grille[joueur_adverse][num_col][li] != None :
         grille[joueur_adverse][num_col][li] = False
         return True #en gros c'est touche
    return False #en gros t'es nul t'as rate

def bateau_touche():
    return 0

def vie_bateau(joueur_actuel,numero):
    """renvoie la vie d'un bateau specifie par son numero entre en parametre
    Prend en parametre le joueur actuel et renvoie les pv du bateau specifie"""
    vie_bateau = 0
    for i in grille[joueur_actuel]:
        if i == numero:
            vie_bateau += 1
    return vie_bateau


def reset():
    """reinitialise la grille a 0"""
    grille = grille_a_zero


def commencer_tour(joueur_actuel, joueur_prochain, grille):
    """Renvoie une fonction avec comme arguments :
    - le mode
    - la grille de l'adversaire
    - la grille du joueur actuel avec ses bateaux
    - le joueur qui joue
    - le joueur en attente"""
    j1 = joueur_actuel
    j2 = joueur_prochain
    
    return init_grille(2, """grille adversaire""", """grille joueur qui joue (ses bateaux)""",j1, j2)