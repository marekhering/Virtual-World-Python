from Zwierze import Zwierze

import random

class Antylopa(Zwierze):

    def __init__(self,x,y):
        Zwierze.__init__(self,x,y)
        self.gatunek = "Antylopa"
        self.wyglad = "A"
        self.kolor = 'DarkGoldenrod1'

        self.inicjatywa = 4
        self.sila = 4


    def akcja(self,swiat,ruchGracza):

        if(self.GetZyje() == True):

            self.ZwiekszWiek()
            ruch = self.WylosujPustePole(swiat,self.x,self.y,False,2)
            if(self.SprawdzPole(swiat,ruch,2) == True):
                self.Rusz(swiat,ruch,2)


    def Ucieczka(self,swiat):

        los = random.randint(1,2)

        if(los == 1):
            return False
        else:
            ruch = self.WylosujPustePole(swiat,self.x,self.y,False,1)
            if(self.SprawdzPole(swiat,ruch,1) == True):
                self.Rusz(swiat,ruch,1)

        return True