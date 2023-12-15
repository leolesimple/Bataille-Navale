from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import sqlite3



col = [
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None] ]


def creation_bateau(num_col, li, longueur, num, etape):
    b = num
    liste_bateau = []
    if etape % 2 == 0 :
        if 8 - col >= longueur :
            for i in range(longueur - 1):
                col[num_col[li]] = num
                col += 1
        else :
            for i in range(longueur - 1):
                col[num_col[li]] = num
                col -= 1
    else :
        if 7 - li >= longueur :
            for i in range(longueur - 1):
                col[num_col[li]] = num
                li += 1
        else :
            for i in range(longueur - 1):
                col[num_col[li]] = num
                li -= 1
    return col


def nombre_bateaux():
     """Renvoie le nombre de bateaux restants """
     bateaux_differents = []
     for i in range(col):
         if num in i:
             if num not in bateaux_differents:
                 bateaux_differents.append(num)
     return "Nombre de bateaux restants :" + len(bateaux_differents)


#def enregistrer_bateaux():
#   return "Vive Léo !"
#à laisser pour Léo

def afficher_carte():
    return 0

def tirer():
    return 0

def bateau_touche():
    return 0

def vie_bateau():
    return 0

def bateaux_restants():
    return 0