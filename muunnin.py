'''
Created on 2.3.2016

@author: Sini
'''

#-*-coding: utf-8 -*- 


class Muunnin():
    

    def __init__(self):
        self.aines = ""
        self.l�ht�yksikk� = ""
        self.yksikk� = ""
        self.muunnettava_arvo = 0
        self.tulos = ""
        
    def tee_muunnos(self,aines,l�ht�yksikk�,yksikk�,l�ht�arvo):
        
        if l�ht�yksikk� == "L":
            tulos = self.litra(aines,l�ht�yksikk�,yksikk�,l�ht�arvo)
            return tulos
        
        elif l�ht�yksikk� == "dl":
            l�ht�arvo /= 10
            tulos = self.litra(aines,l�ht�yksikk�,yksikk�,l�ht�arvo)
            return tulos
        
        elif l�ht�yksikk� == "cl":
            l�ht�arvo /= 100
            tulos = self.litra(aines,l�ht�yksikk�,yksikk�,l�ht�arvo)
            return tulos
        
        elif l�ht�yksikk� == "ml":
            l�ht�arvo /= 1000
            tulos = self.litra(aines,l�ht�yksikk�,yksikk�,l�ht�arvo)
            return tulos
        
        elif l�ht�yksikk� == "kkp":
            l�ht�arvo /= 6.67
            tulos = self.litra(aines,l�ht�yksikk�,yksikk�,l�ht�arvo)
            return tulos
        
        elif l�ht�yksikk� == "rkl":
            l�ht�arvo /= 66.67
            tulos = self.litra(aines,l�ht�yksikk�,yksikk�,l�ht�arvo)
            return tulos
        
        elif l�ht�yksikk� == "tl":
            l�ht�arvo /= 200
            tulos = self.litra(aines,l�ht�yksikk�,yksikk�,l�ht�arvo)
            return tulos
         
    
    def litra(self,aines,l�ht�yksikk�,yksikk�,l�ht�arvo):
        self.aines = aines
        self.l�ht�yksikk� = l�ht�yksikk�
        self.yksikk� = yksikk�
        self.muunnettava_arvo = l�ht�arvo
        
        if l�ht�yksikk� == "L":
            self.l�ht�yksikk� = "l"
        if yksikk� == "L":
            self.yksikk� = "l"
        
        if self.yksikk� == "l":
            tulos = self.muunnettava_arvo
            self.tulos = "{:.1f}".format(tulos)
            return tulos
        if self.yksikk� == "dl":
            tulos = self.muunnettava_arvo*10
            self.tulos = "{:.1f}".format(tulos)
            return tulos
                
        if self.yksikk� == "cl":
            tulos = self.muunnettava_arvo*100
            self.tulos = "{:.1f}".format(tulos)
            return tulos

        if self.yksikk� == "ml" or self.yksikk� == "mm":
            tulos = self.muunnettava_arvo*1000
            self.tulos = "{:.1f}".format(tulos)
            return tulos

        if self.yksikk� == "kkp":
            tulos = self.muunnettava_arvo*6.67
            self.tulos = "{:.1f}".format(tulos)
            return tulos
            
        if self.yksikk� == "rkl":
            tulos = self.muunnettava_arvo*66.67
            self.tulos = "{:.1f}".format(tulos)
            return tulos
        
        if self.yksikk� == "tl":
            tulos = self.muunnettava_arvo*200
            self.tulos = "{:.1f}".format(tulos)
            return tulos
        
    
    def __str__(self):
        teksti = str(self.muunnettava_arvo) + " " + self.l�ht�yksikk� + " " + self.aines + " on "  + self.tulos + " " + self.yksikk�
        return teksti