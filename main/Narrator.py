

class Narrator:

    def __init__(self):
        self.komentarz = []

    def GetKomentarz(self):
        return self.komentarz

    def Wyczysc(self):
        self.komentarz = []

    def Relacjonuj_Rozpylanie(self,Rozpylacz):
        self.komentarz.append(Rozpylacz.ToString() + " rozpylil sie")

    def Relacjonuj_Unik(self,Obr,Atk):
        self.komentarz.append(Obr.ToString() + " uniknal starcia z " + Atk.ToString())

    def Relacjonuj_Rozmnozenie(self,Rodzic1,Rodzic2):
        self.komentarz.append(Rodzic1.ToString() + " i " + Rodzic2.ToString() + " rozmnozyly sie" )

    def Relacjonuj_Jedzenie(self, Zjadany,  Jedzacy):
        self.komentarz.append(Zjadany.ToString()+ " zostal zjedzony przez "+Jedzacy.ToString())

    def Relacjonuj_Smierc(self,Ofiara):
        self.komentarz.append(Ofiara.ToString()+ " zginal!")

    def Relacjonuj_Starcie(self,Wygrany,Przegrany):
        self.komentarz.append(Przegrany.ToString() + " zostal zabity przez " + Wygrany.ToString())

    def Relacjonuj_UmiejetnoscAktywna(self,Czastrwania):
        if(Czastrwania > 1):
            self.komentarz.append("Umiejetnosc czlowieka aktywna jeszcze przez "+ str(Czastrwania)+" tur")
        else:
            self.komentarz.append("Umiejetnosc czlowieka jest aktywna jeszcze w tej turze")

    def Relacjonuj_Delay(self,delay):
        self.komentarz.append( "Umiejetnosc czlowieka odnowi sie za "+ str(delay)+" tur")

