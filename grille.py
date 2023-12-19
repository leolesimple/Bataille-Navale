import tkinter as tk
from tkinter import PhotoImage
from index import *
from random import randint

def button_click(row, col):
    print(f"Button clicked at row {row}, column {col}")

root = tk.Tk()
root.title("Grille de Boutons")
root.resizable(False, False)

    #bg = PhotoImage(file="img/background-sea-water.png")

for i in range(8):
    for j in range(8):
        button = tk.Button(root, text=f"{i+1}-{j+1}", relief=RIDGE, width=5, height=4, command=lambda row=i, col=j: (creation_bateau(col, row, randint(1,3), 1, 1), button_click(row, col)))
        button.grid(row=i+1, column=j)

root.update_idletasks()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width) // 6
y = (screen_height) // 6
root.geometry("+{}+{}".format(x, y))

root.mainloop()
