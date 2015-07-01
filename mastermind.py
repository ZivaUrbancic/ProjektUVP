def predelaj(niz):
    niz=niz.strip('\n')
    sez=niz.split(', ')
    return sez

from tkinter import *
from random import randint

korak=0
cikel=0
barve=[]
zaporedje=[]
zap=[]
rezultati=[]
zmaga=False

class Semafor():
    def __init__(self, master):

        global korak
        global cikel, zaporedje
        global barve
        izbira=["green","yellow","orange","blue","violet","red","SkyBlue1","grey","purple4"]
        zaporedje=[]
        
        # Glavni menu
        menu = Menu(master)
        master.config(menu=menu)

        # Naredimo podmenu "File"
        file_menu = Menu(menu)
        menu.add_cascade(label="Menu", menu=file_menu)

        # Dodamo izbire v file_menu
        file_menu.add_command(label="Nova igra", command=self.restart)
        file_menu.add_command(label="Odpri", command=self.odpri)
        file_menu.add_command(label="Shrani", command=self.shrani)
        file_menu.add_separator() # To doda separator v menu
        file_menu.add_command(label="Izhod", command=master.destroy)

        #Računalnik izbere zaporedje
        for x in range(0,4):
            a=randint(0,len(izbira)-1)
            zaporedje.append(izbira[a])
            del izbira[a]
        #print(zaporedje)

        #Naredimo polje z navodili
        navodila=Label(text="Navodila za igro: \n Računalnik si je izmislil zaporedje štirih barv \n(barve se ne ponavljajo, so paroma različne), ki ga ugibate. \n Barve vnašate v polja s klikom na želeni gumb. \n Potez ne morete razveljaviti. Program vam v prvem kvadratku \n izpiše, koliko barv v zaporedju ste pravilno ugotovili, \n za koliko barv pa ste pravilno ugotovili tudi mesto, \n vam izpiše v drugem kvadratku. Zmagate, ko uganete prava \n mesta za vse štiri barve.")
        navodila.grid(row=0,column=0,columnspan=3)

        
        #Naredimo polje za prikaz
        self.canvas = Canvas(master, width=200, height=230)
        self.canvas.grid(row=1,column=1)
        for i in range(8):
            okno1=self.canvas.create_rectangle(10, 10+i*25, 120, 30+i*25)
            for j in range(4):
                krogec=self.canvas.create_oval(15+j*30,15+i*25,25+j*30,25+i*25)
            
            okno2=self.canvas.create_rectangle(140, 10+i*25, 160, 30+i*25)
            okno3=self.canvas.create_rectangle(170, 10+i*25, 190, 30+i*25)

        #Gumbi z barvami
        gumb_rumena=Button(master, text="     Rumena     ",command=self.nastavi_rumena, bg="yellow")
        gumb_rumena.grid(row=9, column=0)

        gumb_rdeca=Button(master, text="   Rdeca    ",command=self.nastavi_rdeca, bg="red")
        gumb_rdeca.grid(row=9, column=1)

        gumb_zelena=Button(master, text="  Zelena   ",command=self.nastavi_zelena, bg="green")
        gumb_zelena.grid(row=9, column=2)

        gumb_modra=Button(master, text="      Modra       ",command=self.nastavi_modra, bg="blue")
        gumb_modra.grid(row=10, column=0)

        gumb_viola=Button(master, text="  Vijolicna ",command=self.nastavi_vijolicna, bg="purple4")
        gumb_viola.grid(row=10, column=1)

        gumb_oranzna=Button(master, text=" Oranzna ",command=self.nastavi_oranzna, bg="orange")
        gumb_oranzna.grid(row=10, column=2)

        gumb_cian=Button(master, text=" Svetlo modra ",command=self.nastavi_cian, bg="SkyBlue1")
        gumb_cian.grid(row=11, column=0)

        gumb_roza=Button(master, text="     Roza     ",command=self.nastavi_roza, bg="violet")
        gumb_roza.grid(row=11, column=1)

        gumb_siva=Button(master, text="     Siva     ",command=self.nastavi_siva, bg="grey")
        gumb_siva.grid(row=11, column=2)


        
#.....................................................................................................#        
    def odpri(self):
        global zaporedje,barve,rezultati,cikel,zmaga
        rez = filedialog.askopenfile()
        ime = rez.name
        barve=[]
        rezultati=[]
        n=0
        self.canvas.delete("all")
        zmaga=False
        with open(ime) as f:
            for vrstica in f:
                niz=[]
                if n==0:
                    zaporedje=predelaj(vrstica)
                else:
                    sez=predelaj(vrstica)
                    #print(sez)
                    for i in range(4):
                        niz.append(sez[i])
                    rezultati.append([int(sez[4]),int(sez[5])])
                    barve.append(niz)
                n=n+1
        cikel=n-1
        for i in range(8):
            okno1=self.canvas.create_rectangle(10, 10+i*25, 120, 30+i*25)
            for j in range(4):
                if i<len(barve):
                    krogec=self.canvas.create_oval(15+j*30,15+i*25,25+j*30,25+i*25,fill=barve[i][j])
                else:
                    krogec=self.canvas.create_oval(15+j*30,15+i*25,25+j*30,25+i*25)
            okno2=self.canvas.create_rectangle(140, 10+i*25, 160, 30+i*25)
            okno3=self.canvas.create_rectangle(170, 10+i*25, 190, 30+i*25)
            if i<len(rezultati):
                izpis1=self.canvas.create_text(150,20+i*25,text=rezultati[i][0])
                izpis2=self.canvas.create_text(180,20+i*25,text=rezultati[i][1])
            if rezultati[-1][1]==4:zmaga=True
       
    def shrani(self):
        global barve,rezultati,korak
        if korak!=0:
            top = Toplevel()
            msg = Message(top, text='Shranite lahko, ko vnsete celotno vrstico.')
            msg.pack()
            button = Button(top, text="Nazaj", command=top.destroy)
            button.pack()
        else:    
            f=open('izhodna_datoteka.txt', 'w')
            for i in range(0,3):
                f.write(zaporedje[i]+', ')
            f.write(zaporedje[3]+'\n')
            for i in range(0,len(barve)):
                for j in range(len(barve[i])):
                    f.write(str(barve[i][j])+', ')
                f.write(str(rezultati[i][0])+', '+str(rezultati[i][1])+'\n')
            f.close()

    def restart(self):
        global korak
        global cikel, zaporedje
        global barve, zmaga
        zmaga=False
        izbira=["green","yellow","orange","blue","violet","red","SkyBlue1","grey","purple4"]
        zaporedje=[]
        #Računalnik izbere zaporedje
        for x in range(0,4):
            a=randint(0,len(izbira)-1)
            zaporedje.append(izbira[a])
            del izbira[a]
        korak=0
        cikel=0
        barve=[]
        self.canvas.delete("all")
        for i in range(8):
            okno1=self.canvas.create_rectangle(10, 10+i*25, 120, 30+i*25)
            for j in range(4):
                krogec=self.canvas.create_oval(15+j*30,15+i*25,25+j*30,25+i*25)
            okno2=self.canvas.create_rectangle(140, 10+i*25, 160, 30+i*25)
            okno3=self.canvas.create_rectangle(170, 10+i*25, 190, 30+i*25)

        
#Gumbi z barvami........................................................................................................................#

    def nastavi(self, barva):
        #self.canvas.delete(ALL)
        global korak,cikel,barve,zap,zmaga
        if (cikel!=8)and(zmaga==False):
            if barva in zap:
                top = Toplevel()
                msg = Message(top, text='Barve se v zaporedju ne ponavljajo')
                msg.pack()
                button = Button(top, text="OK", command=top.destroy)
                button.pack()
            elif korak==3:
                krogec=self.canvas.create_oval(15+korak*30,15+cikel*25,25+korak*30,25+cikel*25,fill=barva)
                zap.append(barva)
                barve.append(zap)
                self.poracunaj()
                #print(barve,korak)
                korak=0
                zap=[]
                cikel+=1
                #print(barve,korak,cikel)
            else:
                if korak==0:
                    zap=[]
                krogec=self.canvas.create_oval(15+korak*30,15+cikel*25,25+korak*30,25+cikel*25,fill=barva)
                zap.append(barva)
                #print(barve)
                korak+=1

    def nastavi_zelena(self): self.nastavi("green")

    def nastavi_rumena(self): self.nastavi("yellow")

    def nastavi_rdeca(self): self.nastavi("red")

    def nastavi_oranzna(self): self.nastavi("orange")

    def nastavi_vijolicna(self): self.nastavi("purple4")

    def nastavi_modra(self): self.nastavi("blue")

    def nastavi_cian(self): self.nastavi("SkyBlue1")

    def nastavi_roza(self): self.nastavi("violet")

    def nastavi_siva(self): self.nastavi("grey")

#..........................................................................................#

    def poracunaj(self):
        global barve,zaporedje,cikel,zap,rezultati,zmaga
        vzap=0
        okmesto=0
        for i in range(4):
            if barve[cikel][i] in zaporedje:
                vzap=vzap+1
                if barve[cikel][i]==zaporedje[i]:
                    okmesto=okmesto+1
        rezultati.append([vzap,okmesto])
        izpis1=self.canvas.create_text(150,20+cikel*25,text=vzap)
        izpis2=self.canvas.create_text(180,20+cikel*25,text=okmesto)
        if okmesto==4:
            top = Toplevel()
            #top.title("Čestitam!")

            msg = Message(top, text='Zmagali ste!')
            msg.pack()

            button = Button(top, text="Nazaj", command=top.destroy)
            button.pack()
            button1 = Button(top, text="Nova igra",command=self.restart)
            button1.pack()
            zmaga=True
        elif cikel==7:
            top = Toplevel()
            msg = Message(top, text='Zgubili ste!')
            msg.pack()
            button = Button(top, text="Nazaj", command=top.destroy)
            button.pack()
            button1 = Button(top, text="Nova igra",command=self.restart)
            button1.pack()
        #print(vzap,okmesto)

       
#____________________________________________________________________________________________________________________________#
#____________________________________________________________________________________________________________________________#
        
root = Tk()
aplikacija = Semafor(root)
root.mainloop()
