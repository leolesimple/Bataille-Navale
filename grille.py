import tkinter as tk
from tkinter import PhotoImage
from index import *
from random import randint

def button_click(row, col):
    print(f"Button clicked at row {row}, column {col}")

root = tk.Tk()
root.title("Grille de Boutons")
root.resizable(False, False)

bg = PhotoImage(file="img/background-sea-water.png")

label2 = Label(root, text="Bataille Navale", bg="#88cffa", font=("Achemine", 70))
label2.pack(pady=50)


# Utiliser une étiquette pour afficher l'image en arrière-plan
background_label = tk.Label(root, image=bg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

for i in range(8):
    for j in range(8):
        button = tk.Button(root, text=f"{i+1}-{j+1}", width=5, height=4, command=lambda row=i, col=j: (creation_bateau(col, row, randint(1,3), 1, 1), button_click(row, col)))
        button.grid(row=i, column=j)

root.mainloop()
