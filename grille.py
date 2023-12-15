from tkinter import*
from random import*
ecriture=("comic sans ms",13)
nbcase=9
case=50
c=0
nb=6
x0,y0=9,9
chifre=[0,1,2,3,4,5,6,7,8,9]
  
def fin ():
    fenetre.quit()
    fenetre.destroy()
  
def grille():
    for i in range(nbcase+1):
        Can.create_line(x0+case*i, y0,x0+case*i,y0 + nbcase*case)
        Can.create_line(x0, y0+case*i,x0+nbcase*case ,y0+case*i)
  
def donne_position(event):
    TexteC.delete("0.0",END)# on efface l'écriture précédente
    TexteC.insert(END,"clic detecte en x="+str(event.x) + " et y = " + str(event.y))
  
  
  
def jouer(event):
    global trouve
    [i,j]=correspond(event.x,event.y)
    if i in range(nb) and j in range (nb):   # on ne fait rien si le click est hors grille
        Can.create_rectangle(x0 +c*j,y0+c*i,x0 +c*(j+1),y0+c*(i+1),fill="white")
  
  
def correspond(x,y):
    return [(y-y0)/c,(x-x0)/c]
  
  
fenetre=Tk()
Cadre=Frame(fenetre)
Texte1=Label(fenetre,text="Jeu du Sudoku",fg="red",font=ecriture)
BouttonQuit=Button(fenetre,text="quitter", command=fin)
BouttonJouer=Button(fenetre,text="jouer", command=grille)
TexteC=Text(fenetre,height=25,width=25)
Can=Canvas(Cadre,height=500,width=500,bg="white")
  
  
Texte1.grid(row=0,column=0)
BouttonQuit.grid(row=50, column=100)
Cadre.grid(row=1,column=0)
Can.grid(row=2, column=0)
BouttonJouer.grid(row=0, column=50)
TexteC.grid(row=1, column=3)
  
Can.bind("<Button-1>",donne_position)
  
fenetre.mainloop()