from Zwierze import Zwierze

class Owca(Zwierze):

    def __init__(self,x,y):
        Zwierze.__init__(self,x,y)
        self.gatunek = "Owca"
        self.wyglad = "O"
        self.kolor = 'gray86'

        self.inicjatywa = 4
        self.sila = 4