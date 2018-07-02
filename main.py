from tkinter import *
from tree import Node
from tree import BST

def addMessage(newMsg) :
    for i in range(8, -1, -1) : 
        msg = stringList[i].get()
        stringList[i+1].set(msg)
    stringList[0].set(newMsg)

def scroll_start(event):
    canvas.scan_mark(event.x, event.y)

def scroll_move(event):
    canvas.scan_dragto(event.x, event.y, gain=1)
    moveUIback()

def insertButtonClicked() :
    value = entryField.get()
    if value != '':
        entryField.delete(0, END)
        b.insert(b.root, int(value))

def searchButtonClicked():
    value = entryField.get()
    if value != '':
        entryField.delete(0, END)
        b.search(b.root, int(value)) 

def moveUIback():
    insertButton.place(x=25, y=35)
    searchButton.place(x=25, y=65)
    entryField.place(x=5, y=5)
    for i in range(0,9):
        labelList[i].place(x=5, y=580 - i*20)



canvas = Canvas(width=600, height=600, bg='white')   
canvas.pack(expand=YES, fill=BOTH)                   
canvas.bind("<ButtonPress-1>", scroll_start)
canvas.bind("<B1-Motion>", scroll_move)

stringList = []
for i in range(10):
    stringList.append(StringVar())

labelList = []
for i in range(10):
    labelList.append(Label(canvas, textvariable=stringList[i]))


b = BST(canvas, addMessage)

insertButton = Button(canvas, text ="Insert", command = insertButtonClicked, width=10)
insertButton.pack()

searchButton = Button(canvas, text = "Search", command = searchButtonClicked, width = 10)
searchButton.pack()

entryField = Entry(canvas, width = 20, bd = 5)
entryField.pack()

canvas.create_window(0,0, window = entryField)
canvas.create_window(0,0, window = insertButton)
canvas.create_window(0,0, window = searchButton)
for i in range(0,9):
    canvas.create_window(0,0, window = labelList[i])
moveUIback()

mainloop()