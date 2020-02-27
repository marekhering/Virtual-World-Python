from Organizm import Organizm
from Rosliny import Rosliny
from Trawa import Trawa
import random

class Zwierze(Organizm):

    def __init__(self,x,y):
        Organizm.__init__(self,x,y)

    def akcja(self,swiat,ruchGracza):

        if(self.GetZyje() == True):
            self.ZwiekszWiek()
            ruch = self.WylosujPustePole(swiat,self.x,self.y,False,1)
            if(self.SprawdzPole(swiat,ruch,1) == True):
                self.Rusz(swiat,ruch,1)

    def Rusz(self,swiat,ruch,zasieg):

        if(ruch == 0):
            self.x -= zasieg;
            self.y -= zasieg;
        elif(ruch == 1):
            self.y -= zasieg;
        elif(ruch == 2):
            self.x += zasieg;
            self.y -= zasieg;
        elif(ruch == 3):
            self.x += zasieg;
        elif(ruch == 4):
            self.x += zasieg;
            self.y += zasieg;
        elif(ruch == 5):
            self.y += zasieg;
        elif(ruch == 6):
            self.x -= zasieg;
            self.y += zasieg;
        elif(ruch == 7):
            self.x -= zasieg;


    def SprawdzPole(self,swiat,ruch,zasieg):

        Obr = None

        if(ruch == 0):
            if(self.CzyPuste(swiat,self.x - zasieg, self.y - zasieg,True) == 1):
                return True
            else:
                Obr = self.ZnajdzOrganizm(swiat,self.x - zasieg, self.y - zasieg)

        elif(ruch == 1):
            if(self.CzyPuste(swiat,self.x, self.y - zasieg,True) == 1):
                return True
            else:
                Obr = self.ZnajdzOrganizm(swiat,self.x, self.y - zasieg)

        elif(ruch == 2):
            if(self.CzyPuste(swiat,self.x + zasieg, self.y - zasieg,True) == 1):
                return True
            else:
                Obr = self.ZnajdzOrganizm(swiat,self.x + zasieg, self.y - zasieg)

        elif(ruch == 3):
            if(self.CzyPuste(swiat,self.x + zasieg, self.y ,True) == 1):
                return True
            else:
                Obr = self.ZnajdzOrganizm(swiat,self.x + zasieg, self.y )

        elif(ruch == 4):
            if(self.CzyPuste(swiat,self.x + zasieg, self.y + zasieg,True) == 1):
                return True
            else:
                Obr = self.ZnajdzOrganizm(swiat,self.x + zasieg, self.y + zasieg)

        elif(ruch == 5):
            if(self.CzyPuste(swiat,self.x, self.y + zasieg,True) == 1):
                return True
            else:
                Obr = self.ZnajdzOrganizm(swiat,self.x, self.y + zasieg)

        elif(ruch == 6):
            if(self.CzyPuste(swiat,self.x - zasieg, self.y + zasieg,True) == 1):
                return True
            else:
                Obr = self.ZnajdzOrganizm(swiat,self.x - zasieg, self.y + zasieg)

        elif(ruch == 7):
            if(self.CzyPuste(swiat,self.x - zasieg, self.y ,True) == 1):
                return True
            else:
                Obr = self.ZnajdzOrganizm(swiat,self.x - zasieg, self.y )

        if(Obr != None):
            return self.kolizja(swiat,Obr)
        else:
            return True


    def Rozmnoz(self,swiat,DrugiRodzic):

        if(DrugiRodzic.GetWiek() > 2 and self.GetWiek() > 2):
            pozycja = self.WylosujPustePole(swiat,self.x,self.y,True,1)
            if(pozycja == -1):
                return False
            self.StworzOrganizmNaPozycji(swiat,self,self.x,self.y,pozycja)
        else:
            return False

        return True

    def kolizja(self,swiat,Obr):

        if(Obr.GetZyje() == True):
            if(Obr.GetGatunek() == self.GetGatunek()):
                if(self.Rozmnoz(swiat,Obr) == True):
                    swiat.Relacjonuj().Relacjonuj_Rozmnozenie(self,Obr)
                return False

            else:
                if (isinstance(Obr, Zwierze)):
                    if (Obr.czyOdbilAtak(self) == False):
                        if (Obr.Ucieczka(swiat) == False):
                            if(self.Ucieczka(swiat) == False):
                                if(Obr.GetSila() > self.GetSila()):
                                    swiat.Relacjonuj().Relacjonuj_Starcie(Obr,self)
                                    self.Zgin(swiat)
                                else:
                                    swiat.Relacjonuj().Relacjonuj_Starcie(self,Obr)
                                    Obr.Zgin(swiat)
                            else:
                                swiat.Relacjonuj().Relacjonuj_Unik(self,Obr)
                        else:
                            swiat.Relacjonuj().Relacjonuj_Unik(Obr,self)
                    else:
                        return False
                elif (isinstance(Obr, Rosliny)):

                    swiat.Relacjonuj().Relacjonuj_Jedzenie(Obr,self)
                    Obr.kolizja(swiat,self)
                    Obr.Zgin(swiat)

        return True






    def czyOdbilAtak(self,atk):
        return False

    def Ucieczka(self,swiat):
        return False
