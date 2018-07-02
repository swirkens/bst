class Node:
    def __init__(self, parent, value, center, canvas):
        self.parent = parent
        self.value = value
        self.left = None
        self.right = None
        self.center = center

        self.oval = canvas.create_oval(center[0]-20,center[1]-20,center[0]+20,center[1]+20,fill='green', width=2)
        self.text = canvas.create_text(center[0],center[1],text=value)

        self.leftLine = None
        self.rightLine = None

class BST:
    def __init__(self, canvas, function):
        self.canvas = canvas
        self.msgFunction = function
        self.root = None
        self.min = None
        self.max = None
    
    def animationStep(self, node, color, msg):
        self.canvas.itemconfigure(node.oval, fill=color)
        if msg: self.msgFunction(msg)
        self.canvas.update()

    def createLine(self, node, direction, childCenter):
        if direction == 'left':
            node.leftLine = self.canvas.create_line(node.center[0], node.center[1], childCenter[0], childCenter[1], width=2)
            self.canvas.tag_lower(node.leftLine)
        else:
            node.rightLine = self.canvas.create_line(node.center[0], node.center[1], childCenter[0], childCenter[1], width=2)
            self.canvas.tag_lower(node.rightLine)

    def updateLines(self, n):
        if n:
            self.updateLines(n.left)
            self.updateLines(n.right)
            if n.leftLine:
                self.canvas.delete(n.leftLine)
                childCenter = n.left.center
                n.leftLine = self.canvas.create_line(n.center[0], n.center[1], childCenter[0], childCenter[1], width=2)
                self.canvas.tag_lower(n.leftLine)
            if n.rightLine:
                self.canvas.delete(n.rightLine)
                childCenter = n.right.center
                n.rightLine = self.canvas.create_line(n.center[0], n.center[1], childCenter[0], childCenter[1], width=2)
                self.canvas.tag_lower(n.rightLine)

    def moveLeft(self, n, value):
        if n:
            self.moveLeft(n.left, value)
            self.moveLeft(n.right, value)
            if value > n.value:
                n.center[0] -= 40
                self.canvas.move(n.oval, -40, 0)
                self.canvas.move(n.text, -40, 0)

    def moveRight(self, n, value):
        if n:
            self.moveRight(n.left, value)
            self.moveRight(n.right, value)
            if value < n.value:
                n.center[0] += 40
                self.canvas.move(n.oval, 40, 0)
                self.canvas.move(n.text, 40, 0)

    def insert(self, n, value, canvas):
        if n is None:
            center = [300, 50]
            n = Node(None, value, center, canvas)
            self.root = n
            self.min = value
            self.max = value

            canvas.after(500, self.animationStep(n, 'blue', 'Creating root node'))
            canvas.after(500, self.animationStep(n, 'green', ''))
        else:
            if value < n.value and n.left is None:
                canvas.after(500, self.animationStep(n, 'red', str(value) + ' < ' + str(n.value) + '? True. Going left'))
                center = [n.center[0]-40, n.center[1]+40]
                n.left = Node(n, value, center, canvas)
                self.createLine(n, 'left', center)
               
                if value < self.min: self.min = value
                else:
                    self.moveLeft(self.root, value)
                    self.updateLines(self.root)

                canvas.after(0, self.animationStep(n, 'green', ''))
                canvas.after(500, self.animationStep(n.left, 'blue', 'Found empty node. Inserting ' + str(value)))
                canvas.after(0, self.animationStep(n.left, 'green', ''))
                canvas.after(500, self.animationStep(n, 'green', '')) 
                
            elif value >= n.value and n.right is None:
                canvas.after(500, self.animationStep(n, 'red', str(value) + ' < ' + str(n.value) + '? False. Going right'))
                center = [n.center[0]+40, n.center[1]+40]
                n.right = Node(n, value, center, canvas)
                self.createLine(n, 'right', center)

                if value > self.max: self.max = value
                else:
                    self.moveRight(self.root, value)
                    self.updateLines(self.root)

                canvas.after(0, self.animationStep(n, 'green', ''))
                canvas.after(500, self.animationStep(n.right, 'blue', 'Found empty node. Inserting ' + str(value)))
                canvas.after(0, self.animationStep(n.right, 'green', ''))
                canvas.after(500, self.animationStep(n, 'green', ''))
            else:
                if value < n.value:
                    canvas.after(500, self.animationStep(n, 'red', str(value) + ' < ' + str(n.value) + '? True. Going left'))
                    canvas.after(500, self.animationStep(n, 'green', ''))
                    self.insert(n.left, value, canvas)
                else:
                    canvas.after(500, self.animationStep(n, 'red', str(value) + ' < ' + str(n.value) + '? False. Going right'))
                    canvas.after(500, self.animationStep(n, 'green', ''))
                    self.insert(n.right, value, canvas)