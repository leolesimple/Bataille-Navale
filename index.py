from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import sqlite3



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
[None,None,None,None,None,None,None,None] ] ]


def creation_bateau(num_joueur,num_col, li, longueur, num):
    """renvoie la grille avec les numeros des bateaux, et si ya rien bah cest none
    Prend en parametre :
    - num du joueur (0 ou 1) qui definit quelle liste de liste prendre
    - num colonne pour la 1ere sousliste definissant les colonnes
    - li pour la 2e sous liste definissant les lignes
    - longueur qui sera la longueur du bateau
    - num qui correspont a l'etape et au numero du bateau"""
    liste_bateau = []
    if num % 2 == 0 :
        if 7 - num_col >= longueur :
            for i in range(longueur - 1):
                grille[num_joueur][num_col][li] = num
                num_col += 1
        else :
            for i in range(longueur - 1):
                grille[num_joueur][num_col][li] = num
                num_col -= 1
    else :
        if 7 - li >= longueur :
            for i in range(longueur - 1):
                grille[num_joueur][num_col][li] = num
                li += 1
        else :
            for i in range(longueur - 1):
                grille[num_joueur][num_col][li] = num
                li -= 1


def nombre_bateaux(joueur_actuel):
     """Renvoie le nombre de bateaux differents restants
      Prend en parametre le joueur actuel et renvoie le nombre de bateau dans
      la liste (sa grille) qui lui est attribuee"""
     bateaux_differents = []
     for i in range(grille[joueur_actuel]):
         for num in i:
             if num not in bateaux_differents:
                 bateaux_differents.append(num)
     return len(bateaux_differents)


def tirer(joueur_adverse,num_col, li):
    """Retourne si le tir a touche ou non
    Prend en parametre la grille du joueur adverse,
    le num de la colonne et de la ligne ou il tire
    il retourne True si le tir a touche et false sinon"""
    if grille[joueur_adverse][num_col][li] != False and grille[joueur_adverse][num_col][li] != None :
         grille[joueur_adverse][num_col][li] = False
         return True #en gros c'est touche
    return False #en gros t'es nul t'as rate

def bateau_touche(joueur_adverse):
    """Retourne un dico avec les coo des cases touchees et cases coulees
    PDV du joueur actuel, la grille sera la grille de tir du joueur actuel"""
    coo_touchees = []
    coo_coulees = []
    for i in grille[joueur_adverse]:
        for k in i:
            if k == False:
                coo_touchees.append(tuple(k, i))
            elif k == True :
                coo_coulees.append(tuple(k, i))

    dico = { "touche" : coo_touchees, "coule" : coo_coulees}
    return dico

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


