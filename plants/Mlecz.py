from Rosliny import Rosliny

class Mlecz(Rosliny):

    def __init__(self,x,y):
        Rosliny.__init__(self,x,y)
        self.gatunek = "Mlecz"
        self.wyglad = "M"
        self.kolor = 'yellow2'


    def akcja(self,swiat, ruchGracza):

        if(self.GetZyje() == True):
            self.ZwiekszWiek()
            for i in range(3):
                self.Rozpyl(swiat)