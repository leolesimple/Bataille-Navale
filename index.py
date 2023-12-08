from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import sqlite3

#La base de données et les données de celle-ci ne sont que temporaires !
def create_database():
    conn = sqlite3.connect('ma_base_de_donnees.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS utilisateurs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT,
            age INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def get_utilisateurs():
    conn = sqlite3.connect('ma_base_de_donnees.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM utilisateurs")
    utilisateurs = cursor.fetchall()
    conn.close()
    return utilisateurs

def afficher_utilisateurs():
    utilisateurs = get_utilisateurs()
    for utilisateur in utilisateurs:
        tree.insert("", "end", values=(utilisateur[0], utilisateur[1], utilisateur[2]))

root = Tk()
root.title("Bataille Navale | NSI")
root.geometry("1280x854")
root.resizable(False, False)

bg = PhotoImage(file="img/background-sea-water.png")

label1 = Label(root, image=bg)
label1.place(x=0, y=0)

# Modification de la taille et de la police du label "Welcome"
label2 = Label(root, text="Welcome", bg="#88cffa", font=("Parisine", 70))
label2.pack(pady=50)

frame1 = Frame(root, bg="#88cffa")
frame1.pack(pady=20)

columns = ("ID", "Nom", "Age")
tree = ttk.Treeview(frame1, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
tree.pack()

afficher_utilisateurs()

root.update_idletasks()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width) // 4
y = (screen_height) // 4
root.geometry("+{}+{}".format(x, y))

root.mainloop()
