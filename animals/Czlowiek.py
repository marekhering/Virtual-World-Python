from Zwierze import Zwierze

import random

class Czlowiek(Zwierze):

    def __init__(self,x,y):
        Zwierze.__init__(self,x,y)
        self.gatunek = "Czlowiek"
        self.wyglad = "C"
        self.kolor = 'bisque2'

        self.inicjatywa = 4
        self.sila = 5
        self.delay = 0
        self.czasTrwania = 0


    def akcja(self,swiat,ruchGracza):


        if(self.GetZyje() == True):
            self.ZwiekszWiek()

            ruch = -1

            if(ruchGracza == "Up" and self.CzySciana(swiat,self.x,self.y - 1) == False):
                ruch = 1
            if(ruchGracza == "Right" and self.CzySciana(swiat,self.x + 1,self.y) == False):
                ruch = 3
            if(ruchGracza == "Down" and self.CzySciana(swiat,self.x,self.y + 1) == False):
                ruch = 5
            if(ruchGracza == "Left" and self.CzySciana(swiat,self.x - 1,self.y) == False):
                ruch = 7

            if(ruch != -1):
                if(self.SprawdzPole(swiat, ruch, 1) == True):
                    self.Rusz(swiat,ruch,1)

            if(ruchGracza == "Return"):
                self.UzyjUmiejetnosci()

            if(self.GetZyje() == True):
                self.Calopalenie(swiat)


    def UzyjUmiejetnosci(self):

        if(self.delay == 0):
            self.czasTrwania = 5
            self.delay = 5

    def Calopalenie(self,swiat):
        if(self.czasTrwania > 0):
            swiat.Relacjonuj().Relacjonuj_UmiejetnoscAktywna(self.czasTrwania)
            self.ZabijWszystkichDookola(swiat,False)
            self.czasTrwania -= 1
        else:
            if(self.delay > 0):
                swiat.Relacjonuj().Relacjonuj_Delay(self.delay)
                self.delay -= 1