from Zwierze import Zwierze

class Wilk(Zwierze):

    def __init__(self,x,y):
        Zwierze.__init__(self,x,y)
        self.gatunek = "Wilk"
        self.wyglad = "W"
        self.kolor = 'gray'

        self.inicjatywa = 5
        self.sila = 9