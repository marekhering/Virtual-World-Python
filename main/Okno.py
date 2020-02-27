from tkinter import *

class Okno():
    def __init__(self,swiat):
        self.swiat = swiat
        self.rozmiar = 800
        self.poczatek = 25
        self.Okno = Tk()
        self.iloscPol = self.swiat.GetRozmiar()
        self.Przyciski = Frame(self.Okno)
        self.Tlo = 'white'
        self.Plansza = Canvas(self.Okno,width=850,height=850,background=self.Tlo)
        self.Newsy = Canvas(self.Okno, width=800, height=850, background=self.Tlo)

        self.Wybor = None
        self.OknoDanych = None
        self.Dane = None

        self.Okno.title("Wirtualny Swiat    Marek Hering 175729")


    def Rysuj(self):

        self.Przyciski.grid(row=0,column=0)
        NastepnaTura = Button(self.Przyciski,text = "Nowa Tura", command=self.NastepnaTuraFunkcja,width=15 ,font=('Purisa', 16),border=3)
        NastepnaTura.grid(column=0,row=0)
        UzyjUmiejetnosci = Button(self.Przyciski,text = "Uzyj Umiejetnosci", command=self.UzyjUmiejetnosciBtn,width=15 ,font=('Purisa', 16),border=3)
        UzyjUmiejetnosci.grid(column=1,row=0)
        Zapisz = Button(self.Przyciski,text = "Zapisz", command=self.ZapiszBtn,width=15 ,font=('Purisa', 16),border=3)
        Zapisz.grid(column=2,row=0)
        Wczytaj = Button(self.Przyciski,text = "Wczytaj", command=self.WczytajBtn,width=15 ,font=('Purisa', 16),border=3)
        Wczytaj.grid(column=3,row=0)

        self.Plansza.grid(row=1,column=0)
        self.Newsy.grid(row=1,column=1)

        self.RysujPlansze()
        self.NarysujOrganizmy()
        self.NarysujKomentarze()

        self.Okno.bind("<Key>",self.KlawiaturaEvent)

        self.Okno.mainloop()

    def RysujPlansze(self):
        self.Plansza.create_rectangle(self.poczatek,self.poczatek,self.rozmiar+self.poczatek,self.rozmiar+self.poczatek,width=2)
        for i in range(self.iloscPol):
            self.Plansza.create_line(self.poczatek + self.rozmiar / self.iloscPol * i, self.poczatek, self.poczatek + self.rozmiar / self.iloscPol * i,self.poczatek + self.rozmiar, fill='black', width=1)
            self.Plansza.create_line(self.poczatek , self.poczatek + self.rozmiar / self.iloscPol * i, self.poczatek + self.rozmiar ,self.poczatek + self.rozmiar / self.iloscPol * i, fill='black', width=1)

    def NarysujOrganizmy(self):

        self.NarysujKomentarze()

        for i in range(self.swiat.GetIloscOrganizmow()):
            x = self.swiat.GetOrganizm(i).x - 1
            y = self.swiat.GetOrganizm(i).y - 1
            kolor = self.swiat.GetOrganizm(i).GetKolor()
            znak = self.swiat.GetOrganizm(i).GetWyglad()

            self.Plansza.create_rectangle(self.poczatek + x * self.rozmiar/self.iloscPol + 3,self.poczatek + y * self.rozmiar/self.iloscPol + 3,self.poczatek + (x + 1 )* self.rozmiar/self.iloscPol - 3 , self.poczatek + (y + 1) * self.rozmiar/self.iloscPol - 3, fill=kolor, width=1)
            self.Plansza.create_text(self.poczatek + x * self.rozmiar/self.iloscPol + self.rozmiar/self.iloscPol/2 ,self.poczatek + y * self.rozmiar/self.iloscPol + self.rozmiar/self.iloscPol/2,text=znak,font=("Purisa", 20))

    def NarysujKomentarze(self):
        self.Newsy.delete("all")
        Komentarze = self.swiat.Relacjonuj().GetKomentarz()


        self.Newsy.create_text(self.poczatek + 350, 15, text="Komentator :", font=('Purisa', 20))

        for i in range (len(Komentarze)):
            self.Newsy.create_text(self.poczatek + 350, 45 + i*30, text=Komentarze[i],font=('Purisa', 16))

    def WyczyscOrganizmy(self):
        self.Plansza.delete("all")
        self.Newsy.delete("all")
        self.RysujPlansze()

    def NastepnaTuraFunkcja(self):
        self.WyczyscOrganizmy()
        self.swiat.WykonajTure("a")
        self.NarysujOrganizmy()

    def UzyjUmiejetnosciBtn(self):
        self.WyczyscOrganizmy()
        self.swiat.WykonajTure("Return")
        self.NarysujOrganizmy()

    def ZapiszBtn(self):
        self.PobierzDane("s")

    def WczytajBtn(self):
        self.PobierzDane("l")

    def KlawiaturaEvent(self,event):

        if(event.keysym == "s" or event.keysym == "l"):
            self.PobierzDane(event.keysym)

        if(event.keysym != "s" and event.keysym != "l"):
            self.WyczyscOrganizmy()
            self.swiat.WykonajTure(event.keysym)
            self.NarysujOrganizmy()



    def PobierzDane(self,znak):

        self.OknoDanych = Tk()
        self.OknoDanych.geometry("470x60")

        if(znak == "s"):
            self.OknoDanych.title("Zapis")
        if(znak == "l"):
            self.OknoDanych.title("Odczyt")

        self.Dane = Entry(self.OknoDanych,width=20,font=("Calibri",30))
        self.Dane.grid(row=0,column=0)

        ZatwierdzFrame = Frame(self.OknoDanych)
        ZatwierdzFrame.grid(row=0,column=1)

        self.Wybor = znak
        Zatwierdz = Button(ZatwierdzFrame, text="Ok", font=("Calibri",19),  height = 1, width = 4, command=self.ZatwierdzBtn)

        Zatwierdz.grid(column=0, row=0)

        self.OknoDanych.mainloop()

    def Zapisz(self, Sciezka):
        self.swiat.Zapisz(Sciezka)

    def Wczytaj(self,Sciezka):
        self.WyczyscOrganizmy()
        self.swiat.Wczytaj(Sciezka)
        self.NarysujOrganizmy()

    def ZatwierdzBtn(self):
        Sciezka=self.Dane.get()
        if(self.Wybor == "s"):
            self.Zapisz(Sciezka)
        if(self.Wybor == "l"):
            self.Wczytaj(Sciezka)
        self.OknoDanych.destroy()