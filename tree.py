class Node:
    def __init__(self, ojciec, wartosc, lewySyn, prawySyn):
        self.ojciec = ojciec
        self.wartosc = wartosc
        self.lewySyn = lewySyn
        self.prawySyn = prawySyn
        self.center = None

class Drzewo:
    def __init__(self):
        self.korzen = None
        self.min = None
        self.max = None

    def przesun(self, n, wartosc):
        if wartosc < n.wartosc: self.przesunLewo(n.lewySyn, wartosc)
        else: self.przesunPrawo(n.prawySyn, wartosc)

    def przesunLewo(self, n, wartosc):
        if n:
            self.przesunLewo(n.lewySyn, wartosc)
            self.przesunLewo(n.prawySyn, wartosc)
            if wartosc > n.wartosc:
                n.center[0] -= 40

    def przesunPrawo(self, n, wartosc):
        if n:
            self.przesunPrawo(n.lewySyn, wartosc)
            self.przesunPrawo(n.prawySyn, wartosc)
            if wartosc < n.wartosc:
                n.center[0] += 40     

    def rysuj(self, n, canvas):
        if n:
            self.rysuj(n.lewySyn, canvas)
            self.rysuj(n.prawySyn, canvas)
            if n.ojciec:
                parentCenter = n.ojciec.center
                canvas.create_line(n.center[0],n.center[1],parentCenter[0],parentCenter[1], width=2)
            canvas.create_oval(n.center[0]-20,n.center[1]-20,n.center[0]+20,n.center[1]+20,fill='green', width=2)
            canvas.create_text(n.center[0],n.center[1],text=n.wartosc)

    def dodaj(self, n, wartosc, canvas):
        if n is None:
            n = Node(None, wartosc, None, None)
            self.korzen = n
            self.min = wartosc
            self.max = wartosc
            n.center = [300, 50]
            self.rysuj(self.korzen, canvas)
        else:
            if wartosc < n.wartosc and n.lewySyn is None:
                n.lewySyn = Node(n, wartosc, None, None)
                parentCenter = n.center
                n.lewySyn.center = [parentCenter[0]-40, parentCenter[1]+40]
                if wartosc < self.min: self.min = wartosc
                else: self.przesunLewo(self.korzen, wartosc)
                canvas.delete('all')
                self.rysuj(self.korzen, canvas)
            elif wartosc >= n.wartosc and n.prawySyn is None:
                n.prawySyn = Node(n, wartosc, None, None)
                parentCenter = n.center
                n.prawySyn.center = [parentCenter[0]+40, parentCenter[1]+40]
                if wartosc > self.max: self.max = wartosc
                else: self.przesunPrawo(self.korzen, wartosc)
                canvas.delete('all')
                self.rysuj(self.korzen, canvas)
            else:
                if wartosc < n.wartosc: self.dodaj(n.lewySyn, wartosc, canvas)
                else: self.dodaj(n.prawySyn, wartosc, canvas)