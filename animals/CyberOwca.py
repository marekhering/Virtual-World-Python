from Zwierze import Zwierze

class CyberOwca(Zwierze):

    def __init__(self,x,y):
        Zwierze.__init__(self,x,y)
        self.gatunek = "CyberOwca"
        self.wyglad = "☣"
        self.kolor = 'gray86'

        self.inicjatywa = 4
        self.sila = 11

    def akcja(self, swiat, ruchGracza):

        from Point import Point

        if (self.GetZyje() == True):

            self.ZwiekszWiek()
            Punkt = self.ZnajdzBarszcz(swiat,self.x,self.y)


            if(Punkt.x == 0 and Punkt.y == 0):
                ruch = self.WylosujPustePole(swiat, self.x, self.y, False, 1)
                if (self.SprawdzPole(swiat, ruch, 1) == True):
                    self.Rusz(swiat, ruch, 1)
            else:
                ruch = -1

                if(Punkt.x - self.x < 0 and Punkt.y - self.y < 0):
                    ruch = 0
                elif(Punkt.x - self.x == 0 and Punkt.y - self.y < 0):
                    ruch = 1
                elif(Punkt.x - self.x > 0 and Punkt.y - self.y < 0):
                    ruch = 2
                elif(Punkt.x - self.x > 0 and Punkt.y - self.y == 0):
                    ruch = 3
                elif(Punkt.x - self.x > 0 and Punkt.y - self.y > 0):
                    ruch = 4
                elif(Punkt.x - self.x == 0 and Punkt.y - self.y > 0):
                    ruch = 5
                elif(Punkt.x - self.x < 0 and Punkt.y - self.y > 0):
                    ruch = 6
                elif(Punkt.x - self.x < 0 and Punkt.y - self.y == 0):
                    ruch = 7

                if (self.SprawdzPole(swiat, ruch, 1) == True):
                    self.Rusz(swiat, ruch, 1)


