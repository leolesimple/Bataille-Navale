import tkinter as tk
from index import *
from random import randint

def button_click(row, col):
    print(f"Button clicked at row {row}, column {col}")

root = tk.Tk()
root.title("Grille de Boutons")

for i in range(8):
    for j in range(8):
        button = tk.Button(root, text=f"{i+1}-{j+1}", width=5, height=4, command=lambda row=i, col=j: (creation_bateau(col,row, randint(1,3), 1, 1), button_click(row, col)))
        button.grid(row=i, column=j)

root.mainloop()