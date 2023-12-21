from tkinter import *
from tkinter import ttk 
import sqlite3
from random import random

def bateau_utilise():
    L = []
    for i in range(6):
        n = random(1,3)
        L.append(n)
    return L
