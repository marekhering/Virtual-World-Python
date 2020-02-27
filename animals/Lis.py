from Zwierze import Zwierze

class Lis(Zwierze):

    def __init__(self,x,y):
        Zwierze.__init__(self,x,y)
        self.gatunek = "Lis"
        self.wyglad = "L"
        self.kolor = 'DarkOrange2'

        self.inicjatywa = 7
        self.sila = 3



    def akcja(self,swiat,ruchGracza):

        if(self.GetZyje() == True):
            self.ZwiekszWiek()

            ruch = self.WylosujPustePole(swiat,self.x,self.y,False,1)
            if(self.DobryWech(swiat,ruch) == True):
                if(self.SprawdzPole(swiat,ruch,1) == True):
                    self.Rusz(swiat,ruch,1)


    def DobryWech(self,swiat,ruch):

        org = None

        for i in range(swiat.GetIloscOrganizmow()):

            if (ruch == 0):
                if (swiat.GetOrganizm(i).x == self.x - 1 and swiat.GetOrganizm(i).y == self.y - 1):
                    org = swiat.GetOrganizm(i)
            if (ruch == 1):
                if (swiat.GetOrganizm(i).x == self.x and swiat.GetOrganizm(i).y == self.y - 1):
                    org = swiat.GetOrganizm(i)
            if (ruch == 2):
                if (swiat.GetOrganizm(i).x == self.x + 1 and swiat.GetOrganizm(i).y == self.y - 1):
                    org = swiat.GetOrganizm(i)
            if (ruch == 3):
                if (swiat.GetOrganizm(i).x == self.x + 1 and swiat.GetOrganizm(i).y == self.y):
                    org = swiat.GetOrganizm(i)
            if (ruch == 4):
                if (swiat.GetOrganizm(i).x == self.x + 1 and swiat.GetOrganizm(i).y == self.y + 1):
                    org = swiat.GetOrganizm(i)
            if (ruch == 5):
                if (swiat.GetOrganizm(i).x == self.x and swiat.GetOrganizm(i).y == self.y + 1):
                    org = swiat.GetOrganizm(i)
            if (ruch == 6):
                if (swiat.GetOrganizm(i).x == self.x - 1 and swiat.GetOrganizm(i).y == self.y + 1):
                    org = swiat.GetOrganizm(i)
            if (ruch == 7):
                if (swiat.GetOrganizm(i).x == self.x - 1 and swiat.GetOrganizm(i).y == self.y):
                    org = swiat.GetOrganizm(i)


        if(org != None):
            if(org.GetSila() > self.sila and org.GetGatunek() != self.GetGatunek()):
                return False
            else:
                return True

        return True