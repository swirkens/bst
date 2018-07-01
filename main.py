from tkinter import *
from tree import Node
from tree import Drzewo

drzewo = Drzewo()

def scroll_start(event):
    canvas.scan_mark(event.x, event.y)

def scroll_move(event):
    canvas.scan_dragto(event.x, event.y, gain=1)
    moveGUIback()

def moveGUIback():
    przyciskDodaj.place(x=130, y=30)
    pole.place(x=50, y=30)

def clicked() :
    wartosc = pole.get()
    if wartosc != '':
        drzewo.dodaj(drzewo.korzen, int(wartosc), canvas)


canvas = Canvas(width=600, height=600, bg='white')   
canvas.pack(expand=YES, fill=BOTH)                   
canvas.bind("<ButtonPress-1>", scroll_start)
canvas.bind("<B1-Motion>", scroll_move)

przyciskDodaj = Button(canvas, text ="Dodaj", command = clicked)
przyciskDodaj.pack()

pole = Entry(canvas, width = 10, bd = 5)
pole.pack()

canvas.create_window(60, 30, window = pole)
canvas.create_window(130,30, window = przyciskDodaj)
moveGUIback()

mainloop()