from Rosliny import Rosliny

class BarszczSosnowskiego(Rosliny):

    def __init__(self,x,y):
        Rosliny.__init__(self,x,y)
        self.gatunek = "BarszczSosnowskiego"
        self.wyglad = "☠"
        self.kolor = 'lavender'

        self.sila = 10



    def akcja(self,swiat, ruchGracza):

        if(self.GetZyje() == True):
            self.ZwiekszWiek()
            self.Rozpyl(swiat)
            self.ZabijWszystkichDookola(swiat,True)