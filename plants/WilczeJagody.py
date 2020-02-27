from Rosliny import Rosliny

class WilczeJagody(Rosliny):

    def __init__(self,x,y):
        Rosliny.__init__(self,x,y)
        self.gatunek = "WilczeJagody"
        self.wyglad = "J"
        self.kolor = 'MediumPurple4'

        self.sila = 99



    def kolizja(self,swiat,org):
        org.Zgin(swiat)
        return True


