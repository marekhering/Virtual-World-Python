from Narrator import Narrator
from Czlowiek import Czlowiek
from Trawa import Trawa
from Mlecz import Mlecz
from Guarana import Guarana
from WilczeJagody import WilczeJagody
from BarszczSosnowskiego import BarszczSosnowskiego

from Wilk import Wilk
from Owca import Owca
from Lis import Lis
from Zolw import Zolw
from Antylopa import Antylopa
from CyberOwca import CyberOwca

from Point import Point
from Okno import Okno

import random

class Swiat():


    def __init__(self):
        self.organizmy = []
        self.RozmiarXY = 20
        self.StworzCzlowieka()
        self.StartoweOrganizmy()
        self.narrator = Narrator()


    def StworzOrganizm(self,org,x,y):

        if(type(org) == Trawa):
            self.organizmy.append(Trawa(x,y))
        if (type(org) == Mlecz):
            self.organizmy.append(Mlecz(x, y))
        if (type(org) == Guarana):
            self.organizmy.append(Guarana(x, y))
        if (type(org) == WilczeJagody):
            self.organizmy.append(WilczeJagody(x, y))
        if (type(org) == BarszczSosnowskiego):
            self.organizmy.append(BarszczSosnowskiego(x, y))
        if (type(org) == Owca):
            self.organizmy.append(Owca(x, y))
        if(type(org) == Wilk):
            self.organizmy.append(Wilk(x,y))
        if (type(org) == Lis):
            self.organizmy.append(Lis(x, y))
        if (type(org) == Zolw):
            self.organizmy.append(Zolw(x, y))
        if (type(org) == Antylopa):
            self.organizmy.append(Antylopa(x, y))
        if (type(org) == CyberOwca):
            self.organizmy.append(CyberOwca(x, y))

    def StartoweOrganizmy(self):

        trawa = Trawa(0,0)
        mlecz = Mlecz(0,0)
        guarana = Guarana(0,0)
        wilczejagody = WilczeJagody(0,0)
        barszczsosnowskiego = BarszczSosnowskiego(0,0)

        wilk = Wilk(0, 0)
        owca = Owca(0,0)
        lis = Lis(0,0)
        zolw = Zolw(0,0)
        antylopa = Antylopa(0,0)
        cyberOwca = CyberOwca(0,0)

        punkt = Point(0,0)

        self.LosujPole(punkt);self.StworzOrganizm(trawa, punkt.x, punkt.y)
        self.LosujPole(punkt);self.StworzOrganizm(trawa, punkt.x, punkt.y)

        self.LosujPole(punkt);self.StworzOrganizm(wilk, punkt.x, punkt.y)
        self.LosujPole(punkt);self.StworzOrganizm(wilk, punkt.x, punkt.y)

        self.LosujPole(punkt);self.StworzOrganizm(mlecz, punkt.x, punkt.y)
        self.LosujPole(punkt);self.StworzOrganizm(mlecz, punkt.x, punkt.y)

        self.LosujPole(punkt);self.StworzOrganizm(guarana, punkt.x, punkt.y)
        self.LosujPole(punkt);self.StworzOrganizm(guarana, punkt.x, punkt.y)

        self.LosujPole(punkt);self.StworzOrganizm(wilczejagody, punkt.x, punkt.y)
        self.LosujPole(punkt);self.StworzOrganizm(wilczejagody, punkt.x, punkt.y)

        self.LosujPole(punkt);self.StworzOrganizm(barszczsosnowskiego, punkt.x, punkt.y)
        self.LosujPole(punkt);self.StworzOrganizm(barszczsosnowskiego, punkt.x, punkt.y)
        self.LosujPole(punkt);self.StworzOrganizm(barszczsosnowskiego, punkt.x, punkt.y)
        self.LosujPole(punkt);self.StworzOrganizm(barszczsosnowskiego, punkt.x, punkt.y)

        self.LosujPole(punkt);self.StworzOrganizm(owca, punkt.x, punkt.y)
        self.LosujPole(punkt);self.StworzOrganizm(owca, punkt.x, punkt.y)

        self.LosujPole(punkt);self.StworzOrganizm(lis, punkt.x, punkt.y)
        self.LosujPole(punkt);self.StworzOrganizm(lis, punkt.x, punkt.y)

        self.LosujPole(punkt);self.StworzOrganizm(zolw, punkt.x, punkt.y)
        self.LosujPole(punkt);self.StworzOrganizm(zolw, punkt.x, punkt.y)

        self.LosujPole(punkt);self.StworzOrganizm(antylopa, punkt.x, punkt.y)
        self.LosujPole(punkt);self.StworzOrganizm(antylopa, punkt.x, punkt.y)

        self.LosujPole(punkt);self.StworzOrganizm(cyberOwca, punkt.x, punkt.y)


    def StworzCzlowieka(self):

        if(self.GetRozmiar() % 2 == 1):
            czlowiek = Czlowiek(int(self.GetRozmiar()/2)+1,int(self.GetRozmiar()/2)+1)
        else:
            czlowiek = Czlowiek(int(self.GetRozmiar() / 2) , int(self.GetRozmiar() / 2))

        self.organizmy.append(czlowiek)

    def Graj(self):
        okno = Okno(self)
        okno.Rysuj()


    def WykonajTure(self,ruch):
        self.Relacjonuj().Wyczysc()
        max = self.Najwyzszainicjatywa()
        while( max >= 0):
            for i in range(self.GetIloscOrganizmow()):
                if(self.GetOrganizm(i).GetInicjatywa() == max):
                    self.GetOrganizm(i).akcja(self,ruch)
            max -= 1
        self.UsunMartweOrganizmy()


    def LosujPole(self,punkt):

        wynik = 0

        while(wynik == 0):
            punkt.x = random.randint(1, self.GetRozmiar())
            punkt.y = random.randint(1, self.GetRozmiar())
            wynik = self.CzyPuste(self,punkt.x,punkt.y,True)

    def CzyPuste(self, swiat, x, y, bezKolizji):
        if(bezKolizji == True):
            for i in range(self.GetIloscOrganizmow()):
                if(self.GetOrganizm(i).x == x and self.GetOrganizm(i).y == y):
                    return 0
        return 1

    def Zapisz(self,Sciezka):
        Plik = open(Sciezka,"w")


        for i in range(self.GetIloscOrganizmow()):
            Plik.write(self.GetOrganizm(i).GetGatunek()+"\n")
            Plik.write(str(self.GetOrganizm(i).x)+"\n")
            Plik.write(str(self.GetOrganizm(i).y)+"\n")
            Plik.write(str(self.GetOrganizm(i).GetWiek()) + "\n")
            Plik.write(str(self.GetOrganizm(i).GetSila()) + "\n")
            Plik.write(str(self.GetOrganizm(i).delay) + "\n")
            Plik.write(str(self.GetOrganizm(i).czasTrwania) + "\n")

    def Wczytaj(self,Sciezka):

        self.WyczyscPlansze()
        self.Relacjonuj().Wyczysc()
        Plik = open(Sciezka,"r")
        kontent = Plik.read().splitlines()
        i = 0
        for j in kontent:
            if (i % 7 == 0):
                Gatunek = j
            if (i % 7 == 1):
                x = j
            if (i % 7 == 2):
                y = j
            if (i % 7 == 3):
                Wiek = j
            if (i % 7 == 4):
                Sila = j
            if (i % 7 == 5):
                Delay = j
            if (i % 7 == 6):
                CzasTrwania = j

                self.WczytajOrganizm(Gatunek,x,y,Wiek,Sila,Delay,CzasTrwania)
            i += 1

    def WczytajOrganizm(self,Gatunek,x,y,Wiek,Sila,Delay,CzasTrwania):

        Org = None

        if(Gatunek == "Trawa"):
            Org = Trawa(int(x), int(y))
        if (Gatunek == "Mlecz"):
            Org = Mlecz(int(x), int(y))
        if (Gatunek == "Guarana"):
            Org = Guarana(int(x), int(y))
        if (Gatunek == "WilczeJagody"):
            Org = WilczeJagody(int(x), int(y))
        if (Gatunek == "BarszczSosnowskiego"):
            Org = BarszczSosnowskiego(int(x), int(y))
        if (Gatunek == "Owca"):
            Org = Owca(int(x), int(y))
        if(Gatunek == "Wilk"):
            Org = Wilk(int(x), int(y))
        if (Gatunek == "Lis"):
            Org = Lis(int(x), int(y))
        if (Gatunek == "Zolw"):
            Org = Zolw(int(x), int(y))
        if (Gatunek == "Antylopa"):
            Org = Antylopa(int(x), int(y))
        if (Gatunek == "CyberOwca"):
            Org = CyberOwca(int(x), int(y))
        if (Gatunek == "Czlowiek"):
            Org = Czlowiek(int(x), int(y))

        if(Org != None):
            Org.wiek = int(Wiek)
            Org.sila = int(Sila)
            if(Delay != "None" and CzasTrwania != "None"):
                Org.delay = int(Delay)
                Org.czasTrwania = int(CzasTrwania)
            self.organizmy.append(Org)



    def WyczyscPlansze(self):
        for i in range(self.GetIloscOrganizmow()):
            self.organizmy.pop(0)

    def Najwyzszainicjatywa(self):
        max = 0
        for i in range(self.GetIloscOrganizmow()):
            if(self.GetOrganizm(i).GetInicjatywa() > max):
                max = self.GetOrganizm(i).GetInicjatywa()
        return max

    def UsunMartweOrganizmy(self):
        ilosc = self.GetIloscOrganizmow()
        for i in reversed(range(0,ilosc)):
            if(self.GetOrganizm(i).GetZyje() == False):
                self.organizmy.pop(i)

    def Relacjonuj(self):
        return self.narrator

    def GetRozmiar(self):
        return self.RozmiarXY

    def GetIloscOrganizmow(self):
        return len(self.organizmy)

    def GetOrganizm(self,i):
        return self.organizmy[i]


    def Wyswietl(self):

        for i in range(self.GetIloscOrganizmow()):
            print(self.GetOrganizm(i).x,self.GetOrganizm(i).y)
