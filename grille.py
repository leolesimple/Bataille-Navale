from graphics_nsi import *
import sqlite3

def ex1():
    init_graphic(900,600,"Exemple introductif")

    P=Point(100,90)
    draw_fill_rectangle(P,50,25,blue)
    P1=Point(10,10)
    P2=Point(400,500)
    draw_line(P1,P2,red)
    draw_circle(Point(300,350),100,magenta)
    return 0
