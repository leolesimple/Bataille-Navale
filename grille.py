import tkinter as tk
from tkinter import ttk
from random import randint

def init_boat():
    """
        Initialisation de la grille des bateaux. Grille de 8x8. 
    """
    etape = 0

    def button_click(row, col):
        nonlocal etape
        print(f"Button clicked at row {row}, column {col}")
        etape += 1
        if etape > 6:
            root.destroy()

    root = tk.Tk()
    root.title("Grille du Joueur | NSI")
    root.resizable(False, False)

    for i in range(8):
        for j in range(8):
            grille_init_boat = tk.Canvas(root, width=100, height=80, background="#AAE0FE", highlightthickness=0)
            grille_init_boat.grid(row=i+1, column=j, padx=2, pady=2)
            grille_init_boat.create_text(25, 20, text=f"{i}-{j}", fill="black", font=("Parisine", 20), tags="text")
            grille_init_boat.bind("<Button-1>", lambda event, row=i, col=j: (creation_bateau(col, row, randint(1, 3), etape), button_click(row, col))) #add joueur

    root.update_idletasks()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width) // 6
    y = (screen_height) // 6
    root.geometry("+{}+{}".format(x, y))

    root.mainloop()

def creation_bateau(col, li, longueur, num): #add_joueur
    print(col, li, longueur, num)