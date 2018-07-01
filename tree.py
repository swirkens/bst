from time import sleep
import threading

def worker(n, tree, root, canvas):
    n.color = 'green'
    tree.draw(root, canvas)
    print("Done")
    return

class Node:
    def __init__(self, parent, value, left, right):
        self.parent = parent
        self.value = value
        self.left = left
        self.right = right
        self.center = None
        self.color = 'green'

class BST:
    def __init__(self, canvas, function):
        self.root = None
        self.min = None
        self.max = None
        self.queue = []
        self.list = []
        self.msgFunction = function
        self.thread = threading.Timer(0.0, self.threadFunction, [canvas])
        self.thread.start()
        


    def threadFunction(self, canvas):
        while True:
            if self.queue:
                if self.queue[0][0] == 'paintNextRed':
                    self.queue[0][1].color = 'green'
                    self.queue[0][3].color = 'red'
                elif self.queue[0][0] == 'paintRed':
                    self.queue[0][1].color = 'red'
                elif self.queue[0][0] == 'paintGreen':
                    self.queue[0][1].color = 'green'
                elif self.queue[0][0] == 'paintBlue':
                    self.queue[0][1].color = 'blue'
                if self.queue[0][2] != '':
                        self.msgFunction(self.queue[0][2])
                self.draw(self.root, canvas)
                self.queue.pop(0)
            sleep(0.4)

    def move(self, n, value):
        if value < n.value: self.moveLeft(n.left, value)
        else: self.moveRight(n.right, value)

    def moveLeft(self, n, value):
        if n:
            self.moveLeft(n.left, value)
            self.moveLeft(n.right, value)
            if value > n.value:
                n.center[0] -= 40

    def moveRight(self, n, value):
        if n:
            self.moveRight(n.left, value)
            self.moveRight(n.right, value)
            if value < n.value:
                n.center[0] += 40     

    def draw(self, n, canvas):
        if n == self.root: canvas.delete('all')
        if n:
            self.draw(n.left, canvas)
            self.draw(n.right, canvas)
            if n.parent:
                parentCenter = n.parent.center
                canvas.create_line(n.center[0],n.center[1],parentCenter[0],parentCenter[1], width=2)
            canvas.create_oval(n.center[0]-20,n.center[1]-20,n.center[0]+20,n.center[1]+20,fill=n.color, width=2)
            canvas.create_text(n.center[0],n.center[1],text=n.value)

    def insert(self, n, value, canvas):
        if n is None:
            n = Node(None, value, None, None)
            self.root = n
            self.min = value
            self.max = value
            n.center = [300, 50]
            self.queue.append(('paintRed', n, 'Creating root node'))
            self.queue.append(('paintBlue', n, ''))
            self.queue.append(('paintGreen', n, ''))
        else:
            if value < n.value and n.left is None:
                self.queue.append(('paintRed', n, str(value) + ' < ' + str(n.value) + '? True. Going left'))
                n.left = Node(n, value, None, None)
                self.queue.append(('paintNextRed', n, '', n.left))
                self.queue.append(('paintBlue', n.left, 'Found empty node. Inserting ' + str(value)))
                self.queue.append(('paintGreen', n.left, ''))
                parentCenter = n.center
                n.left.center = [parentCenter[0]-40, parentCenter[1]+40]
                if value < self.min: self.min = value
                else: self.moveLeft(self.root, value)
            elif value >= n.value and n.right is None:
                self.queue.append(('paintRed', n, str(value) + ' < ' + str(n.value) + '? False. Going right'))
                n.right = Node(n, value, None, None)
                self.queue.append(('paintNextRed', n, '', n.right)) 
                self.queue.append(('paintBlue', n.right, 'Found empty node. Inserting ' + str(value)))
                self.queue.append(('paintGreen', n.right, ''))
                parentCenter = n.center
                n.right.center = [parentCenter[0]+40, parentCenter[1]+40]
                if value > self.max: self.max = value
                else: self.moveRight(self.root, value)
            else:
                if value < n.value:
                    self.queue.append(('paintRed', n, str(value) + ' < ' + str(n.value) + '? True. Going right'))
                    self.queue.append(('paintNextRed', n, '', n.left))
                    self.insert(n.left, value, canvas)
                else:
                    self.queue.append(('paintRed', n, str(value) + ' < ' + str(n.value) + '? False. Going right'))
                    self.queue.append(('paintNextRed', n, '', n.right)) 
                    self.insert(n.right, value, canvas)