'''
Created on 2.3.2016

@author: Sini Bäckman
'''

#-*-coding: utf-8 -*-
import os


class Ruokakaappi():
    
    def __init__(self):
        self.sisalto = []
        self.alusta_kaappi()
        
    def lisaa_aines(self,aines):
        self.sisalto.append(aines)
        return True
    
    def poista_aines(self,aines):
        self.sisalto.remove(aines)
        return True
    
    def anna_ainekset(self):
        return self.sisalto
    
    def alusta_kaappi(self):
        path = os.path.expanduser("~/Documents/reseptikirja/ruokakaappi.txt")
        if os.path.exists(path):
            tiedosto = open(path,"r")
            lista = tiedosto.readlines()
            for i in lista:
                i = i.split(",")
                aines = Aines(i[0],i[1],i[2])
                self.sisalto.append(aines)
            tiedosto.close()
        else:
            paikka = os.path.expanduser("~/Documents/")
            os.makedirs(paikka + "reseptikirja/")
            tiedosto = open(path,"w")
            tiedosto.close()
    
class Aines():
    
    def __init__(self,nimi,maara,yksikko):
        self.nimi = nimi
        self.maara = maara
        self.yksikko = yksikko
        self.meta_ainekset = []
        self.valmistettavissa = False
        
    def lisaa(self,maara):
        self.maara += maara
        return True
    
    def poista(self,maara):
        self.maara -= maara
        return True
    
    def aineksen_maara(self,maara):
        self.aara = maara
        return True
    
    def valmistettavissa(self,ainekset):
        if self.meta_ainekset != []:
            self.valmistettavissa = True
        return True

    def __str__(self):
        teksti = self.nimi + "\t" + self.maara + " " + self.yksikko
        return teksti
