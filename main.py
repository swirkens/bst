from tkinter import *
from tree import Node
from tree import BST

b = BST()

def scroll_start(event):
    canvas.scan_mark(event.x, event.y)

def scroll_move(event):
    canvas.scan_dragto(event.x, event.y, gain=1)
    moveUIback()

def moveUIback():
    insertButton.place(x=130, y=30)
    entryField.place(x=50, y=30)

def clicked() :
    value = entryField.get()
    if value != '':
        b.insert(b.root, int(value), canvas)


canvas = Canvas(width=600, height=600, bg='white')   
canvas.pack(expand=YES, fill=BOTH)                   
canvas.bind("<ButtonPress-1>", scroll_start)
canvas.bind("<B1-Motion>", scroll_move)

insertButton = Button(canvas, text ="Dodaj", command = clicked)
insertButton.pack()

entryField = Entry(canvas, width = 10, bd = 5)
entryField.pack()

canvas.create_window(60, 30, window = entryField)
canvas.create_window(130,30, window = insertButton)
moveUIback()

mainloop()