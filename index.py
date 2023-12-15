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
                col[num_col[li]] = True
                col += 1
        else :
            for i in range(longueur - 1):
                col[num_col[li]] = True
                col -= 1
    return col

def nombre_bateaux():
     return 0

def localisation_bateaux():
     return 0

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