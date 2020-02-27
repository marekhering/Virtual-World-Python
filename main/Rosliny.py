from Organizm import Organizm
import random

class Rosliny(Organizm):

    szansaNaRozpylenie = 4

    def __init__(self,x,y):
        Organizm.__init__(self,x,y)

        self.inicjatywa = 0
        self.sila = 0


    def akcja(self,swiat, ruchGracza):

        if(self.GetZyje() == True):
            self.ZwiekszWiek()
            self.Rozpyl(swiat)


    def Rozpyl(self,swiat):

        rozmnazanie = random.randint(1,100)

        if(rozmnazanie <= self.GetSzansaNaRozpylenie() and self.GetWiek() > 1):
            pozycja = self.WylosujPustePole(swiat, self.x, self.y, True, 1)
            if(pozycja != -1):
                swiat.Relacjonuj().Relacjonuj_Rozpylanie(self)
            self.StworzOrganizmNaPozycji(swiat,self,self.x,self.y,pozycja)


    def czyOdbilAtak(self,atk):
        return False

    def Ucieczka(self,swiat):
        return False

    def kolizja(self,swiat,org):
        return True

    def GetSzansaNaRozpylenie(self):
        return self.szansaNaRozpylenie