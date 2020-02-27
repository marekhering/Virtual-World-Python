from Zwierze import Zwierze

import random

class Zolw(Zwierze):

    def __init__(self,x,y):
        Zwierze.__init__(self,x,y)
        self.gatunek = "Zolw"
        self.wyglad = "Z"
        self.kolor = 'LemonChiffon3'

        self.inicjatywa = 1
        self.sila = 2



    def akcja(self,swiat,ruchGracza):

        if(self.GetZyje() == True):
            self.ZwiekszWiek()

            los = random.randint(1, 4)

            if(los == 1):
                ruch = self.WylosujPustePole(swiat,self.x,self.y,False,1)
                if(self.SprawdzPole(swiat,ruch,1) == True):
                    self.Rusz(swiat,ruch,1)


    def czyOdbilAtak(self,atk):

        if(atk.GetSila() < 5):
            return True
        else :
            return False


