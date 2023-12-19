from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import sqlite3



grille = [
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None] ]


def creation_bateau(num_col, li, longueur, num, etape):
    liste_bateau = []
    if etape % 2 == 0 :
        if 7 - num_col >= longueur :
            for i in range(longueur - 1):
                grille[num_col[li]] = num
                num_col += 1
        else :
            for i in range(longueur - 1):
                grille[num_col[li]] = num
                num_col -= 1
    else :
        if 7 - li >= longueur :
            for i in range(longueur - 1):
                grille[num_col[li]] = num
                li += 1
        else :
            for i in range(longueur - 1):
                grille[num_col[li]] = num
                li -= 1
    return col


def nombre_bateaux():
     """Renvoie le nombre de bateaux restants """
     bateaux_differents = []
     for i in range(grille):
         for num in i:
             if num not in bateaux_differents:
                 bateaux_differents.append(num)
     return "Nombre de bateaux restants :" + len(bateaux_differents)


def enregistrer_bateaux():
    return "Vive Léo !"


def tirer(num_col, li):
    if grille[num_col[li]] != False and grille[num_col[li]] != None :
         grille[num_col[li]] = False
         return True #en gros c'est touche
    return False #en gros t'es nul t'as rate

def bateau_touche():
    return 0

def vie_bateau():
    return 0

def bateaux_restants():
    return 0