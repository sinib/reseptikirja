'''
Created on 2.3.2016

@author: Sini
'''

#-*-coding: utf-8 -*- 


class Muunnin():
    

    def __init__(self):
        self.aines = ""
        self.lähtöyksikkö = ""
        self.yksikkö = ""
        self.muunnettava_arvo = 0
        self.tulos = ""
        
    def tee_muunnos(self,aines,lähtöyksikkö,yksikkö,lähtöarvo):
        
        if lähtöyksikkö == "L":
            tulos = self.litra(aines,lähtöyksikkö,yksikkö,lähtöarvo)
            return tulos
        
        elif lähtöyksikkö == "dl":
            lähtöarvo /= 10
            tulos = self.litra(aines,lähtöyksikkö,yksikkö,lähtöarvo)
            return tulos
        
        elif lähtöyksikkö == "cl":
            lähtöarvo /= 100
            tulos = self.litra(aines,lähtöyksikkö,yksikkö,lähtöarvo)
            return tulos
        
        elif lähtöyksikkö == "ml":
            lähtöarvo /= 1000
            tulos = self.litra(aines,lähtöyksikkö,yksikkö,lähtöarvo)
            return tulos
        
        elif lähtöyksikkö == "kkp":
            lähtöarvo /= 6.67
            tulos = self.litra(aines,lähtöyksikkö,yksikkö,lähtöarvo)
            return tulos
        
        elif lähtöyksikkö == "rkl":
            lähtöarvo /= 66.67
            tulos = self.litra(aines,lähtöyksikkö,yksikkö,lähtöarvo)
            return tulos
        
        elif lähtöyksikkö == "tl":
            lähtöarvo /= 200
            tulos = self.litra(aines,lähtöyksikkö,yksikkö,lähtöarvo)
            return tulos
         
    
    def litra(self,aines,lähtöyksikkö,yksikkö,lähtöarvo):
        self.aines = aines
        self.lähtöyksikkö = lähtöyksikkö
        self.yksikkö = yksikkö
        self.muunnettava_arvo = lähtöarvo
        
        if lähtöyksikkö == "L":
            self.lähtöyksikkö = "l"
        if yksikkö == "L":
            self.yksikkö = "l"
        
        if self.yksikkö == "l":
            tulos = self.muunnettava_arvo
            self.tulos = "{:.1f}".format(tulos)
            return tulos
        if self.yksikkö == "dl":
            tulos = self.muunnettava_arvo*10
            self.tulos = "{:.1f}".format(tulos)
            return tulos
                
        if self.yksikkö == "cl":
            tulos = self.muunnettava_arvo*100
            self.tulos = "{:.1f}".format(tulos)
            return tulos

        if self.yksikkö == "ml" or self.yksikkö == "mm":
            tulos = self.muunnettava_arvo*1000
            self.tulos = "{:.1f}".format(tulos)
            return tulos

        if self.yksikkö == "kkp":
            tulos = self.muunnettava_arvo*6.67
            self.tulos = "{:.1f}".format(tulos)
            return tulos
            
        if self.yksikkö == "rkl":
            tulos = self.muunnettava_arvo*66.67
            self.tulos = "{:.1f}".format(tulos)
            return tulos
        
        if self.yksikkö == "tl":
            tulos = self.muunnettava_arvo*200
            self.tulos = "{:.1f}".format(tulos)
            return tulos
        
    
    def __str__(self):
        teksti = str(self.muunnettava_arvo) + " " + self.lähtöyksikkö + " " + self.aines + " on "  + self.tulos + " " + self.yksikkö
        return teksti