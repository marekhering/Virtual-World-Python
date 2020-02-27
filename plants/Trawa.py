from Rosliny import Rosliny

class Trawa(Rosliny):

    def __init__(self,x,y):
        Rosliny.__init__(self,x,y)
        self.gatunek = "Trawa"
        self.wyglad = "T"
        self.kolor = 'green'



