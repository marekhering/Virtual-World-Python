from Rosliny import Rosliny

class Guarana(Rosliny):

    def __init__(self,x,y):
        Rosliny.__init__(self,x,y)
        self.gatunek = "Guarana"
        self.wyglad = "G"
        self.kolor = 'orange red'

    def kolizja(self,swiat,org):
        org.ZwiekszSile(3)

        return True

