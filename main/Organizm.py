import random

class Organizm():

    sila = None
    inicjatywa = None
    x = None
    y = None
    zyje = None
    delay = None
    czasTrwania = None

    wyglad = None
    kolor = None
    gatunek = None

    def __init__(self,x,y):
        self.x = x
        self.y = y


        self.zyje = True
        self.wiek = 0

    def WylosujPustePole(self, swiat, x, y, bezKolizji, zasieg):
        tab = []
        pozycja = -1
        ilePustych = 0

        self.ZnajdzPuste(swiat,tab,x,y,bezKolizji,zasieg)

        for i in range(len(tab)):
            ilePustych+=tab[i]

        if(ilePustych > 0):
            los = random.randint(1,ilePustych)
            n = 1
            for i in range(len(tab)):
                if(tab[i] == 1):
                    if(n == los):
                        pozycja = i
                        break
                    n += 1

        return pozycja


    def ZnajdzPuste(self,swiat, tab, x, y, bezKolizji, zasieg):

        tab.append(self.CzyPuste(swiat, x - zasieg, y - zasieg, bezKolizji))
        tab.append(self.CzyPuste(swiat, x, y - zasieg, bezKolizji))
        tab.append(self.CzyPuste(swiat, x + zasieg, y - zasieg, bezKolizji))
        tab.append(self.CzyPuste(swiat, x + zasieg, y, bezKolizji))
        tab.append(self.CzyPuste(swiat, x + zasieg, y + zasieg, bezKolizji))
        tab.append(self.CzyPuste(swiat, x, y + zasieg, bezKolizji))
        tab.append(self.CzyPuste(swiat, x - zasieg, y + zasieg, bezKolizji))
        tab.append(self.CzyPuste(swiat, x - zasieg, y, bezKolizji))

    def CzyPuste(self, swiat, x, y, bezKolizji):
        if(self.CzySciana(swiat,x,y) == True):
            return 0
        if(bezKolizji == True):
            for i in range(swiat.GetIloscOrganizmow()):
               if(swiat.GetOrganizm(i).x == x and swiat.GetOrganizm(i).y == y):
                    return 0
        return 1


    def CzySciana(self, swiat, x, y):
        if(x >= swiat.GetRozmiar() + 1 or y >= swiat.GetRozmiar() + 1 or y <=0 or x <= 0):
            return True
        else:
            return False


    def StworzOrganizmNaPozycji(self,swiat,org,x,y,pozycja):
        if (pozycja != -1):
            if (pozycja == 0):
                swiat.StworzOrganizm(org, x - 1, y - 1)
            elif (pozycja == 1):
                swiat.StworzOrganizm(org, x, y - 1)
            elif (pozycja == 2):
                swiat.StworzOrganizm(org, x + 1, y - 1)
            elif (pozycja == 3):
                swiat.StworzOrganizm(org, x + 1, y)
            elif (pozycja == 4):
                swiat.StworzOrganizm(org, x + 1, y + 1)
            elif (pozycja == 5):
                swiat.StworzOrganizm(org, x, y + 1)
            elif (pozycja == 6):
                swiat.StworzOrganizm(org, x - 1, y + 1)
            elif (pozycja == 7):
                swiat.StworzOrganizm(org, x - 1, y)


    def ZnajdzOrganizm(self,swiat,x,y):

        for i in range(swiat.GetIloscOrganizmow()):
            if (swiat.GetOrganizm(i).x == x and swiat.GetOrganizm(i).y == y):
                org = swiat.GetOrganizm(i)
                return org

        return None

    def ZnajdzBarszcz(self,swiat,x,y):
        from Point import Point
        from BarszczSosnowskiego import BarszczSosnowskiego
        import math

        Punkt = Point(0,0)
        min = 0

        for i in range(swiat.GetIloscOrganizmow()):
            if(isinstance(swiat.GetOrganizm(i),BarszczSosnowskiego)):
                dystans = math.sqrt( pow(swiat.GetOrganizm(i).x - x,2) + pow(swiat.GetOrganizm(i).y - y,2))
                if(min == 0):
                    min = dystans
                    Punkt.x = swiat.GetOrganizm(i).x
                    Punkt.y = swiat.GetOrganizm(i).y
                if(min > dystans):
                    min = dystans
                    Punkt.x = swiat.GetOrganizm(i).x
                    Punkt.y = swiat.GetOrganizm(i).y

        return Punkt



    def ZabijWszystkichDookola(self,swiat,OproczRosliny):

        from Zwierze import Zwierze
        from CyberOwca import CyberOwca

        for i in range(swiat.GetIloscOrganizmow()):
            if(abs(swiat.GetOrganizm(i).x - self.x) <= 1 and abs(swiat.GetOrganizm(i).y - self.y) <= 1 and self != swiat.GetOrganizm(i)):
                if(OproczRosliny == True):
                    if(isinstance(swiat.GetOrganizm(i),Zwierze) and not(isinstance(swiat.GetOrganizm(i),CyberOwca))):
                        swiat.GetOrganizm(i).Zgin(swiat)

                else:
                    swiat.GetOrganizm(i).Zgin(swiat)

    def ToString(self):
        string = self.gatunek + "(" + str(self.x) + "," + str(self.y) + ")"
        return string

    def Zgin(self,swiat):
        from Zwierze import Zwierze
        self.zyje = False
        if(isinstance(self,Zwierze)):
            swiat.Relacjonuj().Relacjonuj_Smierc(self)

    def ZwiekszSile(self,x):
        self.sila += x

    def ZwiekszWiek(self):
        self.wiek += 1

    def GetKolor(self):
        return self.kolor

    def GetSila(self):
        return self.sila

    def GetInicjatywa(self):
        return self.inicjatywa

    def GetWyglad(self):
        return self.wyglad

    def GetGatunek(self):
        return self.gatunek

    def GetZyje(self):
        return self.zyje

    def GetWiek(self):
        return self.wiek