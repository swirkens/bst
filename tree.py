class Node:
    def __init__(self, parent, value, left, right):
        self.parent = parent
        self.value = value
        self.left = left
        self.right = right
        self.center = None

class BST:
    def __init__(self):
        self.root = None
        self.min = None
        self.max = None

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
        if n:
            self.draw(n.left, canvas)
            self.draw(n.right, canvas)
            if n.parent:
                parentCenter = n.parent.center
                canvas.create_line(n.center[0],n.center[1],parentCenter[0],parentCenter[1], width=2)
            canvas.create_oval(n.center[0]-20,n.center[1]-20,n.center[0]+20,n.center[1]+20,fill='green', width=2)
            canvas.create_text(n.center[0],n.center[1],text=n.value)

    def insert(self, n, value, canvas):
        if n is None:
            n = Node(None, value, None, None)
            self.root = n
            self.min = value
            self.max = value
            n.center = [300, 50]
            self.draw(self.root, canvas)
        else:
            if value < n.value and n.left is None:
                n.left = Node(n, value, None, None)
                parentCenter = n.center
                n.left.center = [parentCenter[0]-40, parentCenter[1]+40]
                if value < self.min: self.min = value
                else: self.moveLeft(self.root, value)
                canvas.delete('all')
                self.draw(self.root, canvas)
            elif value >= n.value and n.right is None:
                n.right = Node(n, value, None, None)
                parentCenter = n.center
                n.right.center = [parentCenter[0]+40, parentCenter[1]+40]
                if value > self.max: self.max = value
                else: self.moveRight(self.root, value)
                canvas.delete('all')
                self.draw(self.root, canvas)
            else:
                if value < n.value: self.insert(n.left, value, canvas)
                else: self.insert(n.right, value, canvas)