'''
Created on 2.3.2016

@author: Sini Bäckman
'''

import sys
from PyQt4 import QtGui,QtCore
from ruokakaappi import Ruokakaappi
from muunnin import Muunnin
#-*-coding: utf-8 -*- 


class Kayttoliittyma(QtGui.QWidget):
    
    def __init__(self):
        super(Kayttoliittyma, self).__init__()
        
        self.liittyma()
        self.header()
        self.etusivu()
        self.kaapin_muokkaus()
        self.reseptihaku()
        self.reseptihallinta()
        self.muunnin()
        self.valilehdet()
        self.kaappi()
        self.toggle_theme()
        self.setGeometry(250, 150, 810, 610)
        self.setWindowTitle("Reseptikirja") 
        self.show()
        
        
    def liittyma(self):
        '''
        -----------------------------------
        Käyttöliittymän eri osien 
        tarvitsemat asiat: Monikot,
        paletit, layoutit, stylesheetit.
        -----------------------------------
        '''
        
        self.yksikot = ("L","dl","cl","ml","kkp","rkl","tl")
        
        # foreground    background    light    dark    mid    text    base
        self.varit = QtGui.QPalette(QtGui.QColor(255,255,255), QtGui.QColor(38,38,38), QtGui.QColor(54,111,145), QtGui.QColor(200,227,244), QtGui.QColor(114,168,200), QtGui.QColor(255,255,255), QtGui.QColor(200,227,244))
        self.varitt = QtGui.QPalette(QtGui.QColor(0,0,0), QtGui.QColor(255,255,255), QtGui.QColor(200,227,244), QtGui.QColor(54,111,145), QtGui.QColor(114,168,200), QtGui.QColor(0,0,0), QtGui.QColor(200,227,244))
        self.setPalette(self.varit)
        
        self.layout = QtGui.QGridLayout() 
        self.setLayout(self.layout)
        
        self.laatikkolayout = QtGui.QVBoxLayout()
        self.laatikko1layout = QtGui.QVBoxLayout()
        self.laatikko2layout = QtGui.QVBoxLayout()
        self.laatikko3layout = QtGui.QVBoxLayout()
        self.laatikko4Vlayout = QtGui.QVBoxLayout()
        self.laatikko4Hlayout = QtGui.QHBoxLayout()
        self.ruokakaappilayout = QtGui.QVBoxLayout()

        
        self.button_stylesheet = (".QPushButton { \
                                            max-width: 80px; \
                                            background:rgb(38,38,38); \
                                            color:rgb(255,255,255); \
                                            border-bottom: 2px solid rgb(54,111,145); \
                                            border-right: 2px solid rgb(54,111,145); \
                                            border-top: 2px solid rgb(102,162,198); \
                                            border-left: 2px solid rgb(102,162,198); \
                                            padding: 3px;} \
                                    .QPushButton:hover{\
                                            background:rgb(18,18,18);\
                                                }\
                                     .QPushButton:pressed {\
                                            background:rgb(18,18,18); \
                                            border-bottom: 2px solid rgb(102,162,198); \
                                            border-right: 2px solid rgb(102,162,198); \
                                            border-top: 2px solid rgb(54,111,145); \
                                            border-left: 2px solid rgb(54,111,145);}  \
                                ")
        
        self.button_stylesheett = (".QPushButton { \
                                            max-width: 80px; \
                                            background:rgb(255,255,255); \
                                            color:rgb(0,0,0); \
                                            border-bottom: 2px solid rgb(54,111,145); \
                                            border-right: 2px solid rgb(54,111,145); \
                                            border-top: 2px solid rgb(102,162,198); \
                                            border-left: 2px solid rgb(102,162,198); \
                                            padding: 3px;} \
                                    .QPushButton:hover{\
                                            background:rgb(235,235,235);\
                                    }\
                                    .QPushButton:pressed {\
                                            background:rgb(235,235,235); \
                                            border-bottom: 2px solid rgb(102,162,198); \
                                            border-right: 2px solid rgb(102,162,198); \
                                            border-top: 2px solid rgb(54,111,145); \
                                            border-left: 2px solid rgb(54,111,145);}  \
                                    ")
        
        self.box_stylesheet = (".QGroupBox{ \
                                        border: 1px solid rgb(102,162,198);\
                                        background: rgb(0,0,0,0) \
                                      } \
                                ")
        
        self.label_stylesheet = (".QLabel{ \
                                        color: rgb(255,255,255);\
                                      } \
                                ")
        
        self.label_stylesheett = (".QLabel{ \
                                        color: rgb(0,0,0);\
                                      } \
                                ")
        self.laatikkolabel = (".QLabel{ \
                                        color: rgb(109,109,109);\
                                      } \
                            ")
        
        self.tab_stylesheet = (".QTabWidget::pane{\
                                    background:rgb(38,38,38); \
                                    border: 1px solid rgb(102,162,198);} \
                                \
                                .QTabWidget::tab-bar{\
                                    left: 5px;\
                                    } \
                                \
                                .QTabBar::tab{ \
                                    background:rgb(38,38,38); \
                                    border-top-right-radius: 5px;\
                                    border-top-left-radius: 5px; \
                                    color: rgb(255,255,255); \
                                    padding: 5px; \
                                    min-width: 120px;\
                                    }\
                                .QTabBar::tab:first{\
                                    min-width: 65px; \
                                    margin-left:0px; \
                                    } \
                                \
                                .QTabBar::tab:last{\
                                    min-width: 65px; \
                                    margin-right:0px; \
                                    } \
                                \
                                .QTabBar::tab:first:selected{\
                                    margin-left:0px; \
                                    } \
                                \
                                .QTabBar::tab:last:selected{\
                                    margin-right:0px;} \
                                \
                                .QTabBar::tab:first:!selected{\
                                    margin-left:0px;} \
                                \
                                .QTabBar::tab:last:!selected{\
                                    margin-right:0px;} \
                                \
                                .QTabBar::tab:selected{\
                                    background:rgb(58,58,58); \
                                    margin-left:-3px; \
                                    margin-right:-3px; \
                                    border-top: 2px solid rgb(102,162,198); \
                                    border-right: 2px solid rgb(102,162,198); \
                                    border-left: 2px solid rgb(102,162,198); \
                                    }\
                                \
                                .QTabBar::tab:!selected{\
                                    margin-top:2px;\
                                    border-top: 1px solid rgb(102,162,198); \
                                    border-right: 1px solid rgb(102,162,198); \
                                    border-left: 1px solid rgb(102,162,198);\
                                    } \
                                \
                                .QTabBar::tab:hover{\
                                    background:rgb(18,18,18);} \
                                \
                                .QTabBar::tab:selected:hover{\
                                    background:rgb(58,58,58);} \
                                ")
        
        self.tab_stylesheett = (".QTabWidget::pane{\
                                    background:rgb(255,255,255); \
                                    border: 1px solid rgb(102,162,198);} \
                                \
                                .QTabWidget::tab-bar{\
                                    left: 5px;\
                                    } \
                                \
                                .QTabBar::tab{ \
                                    background:rgb(255,255,255); \
                                    min-width:120px; \
                                    border-top-right-radius: 5px;\
                                    border-top-left-radius: 5px; \
                                    color: rgb(0,0,0); \
                                    padding: 5px;} \
                                    \
                                .QTabBar::tab:first{\
                                    min-width:65px; \
                                    } \
                                \
                                .QTabBar::tab:last{\
                                    min-width: 65px; \
                                    } \
                                \
                                .QTabBar::tab:first:selected{\
                                    margin-left:0px;} \
                                \
                                .QTabBar::tab:last:selected{\
                                    margin-right:0px;} \
                                \
                                .QTabBar::tab:first:!selected{\
                                    margin-left:0px;} \
                                \
                                .QTabBar::tab:last:!selected{\
                                    margin-right:0px;} \
                                \
                                .QTabBar::tab:selected{\
                                    background:rgb(237,237,237); \
                                    margin-left:-3px; \
                                    margin-right:-3px; \
                                    border-top: 2px solid rgb(102,162,198); \
                                    border-right: 2px solid rgb(102,162,198); \
                                    border-left: 2px solid rgb(102,162,198); \
                                    }\
                                .QTabBar::tab:!selected{\
                                    margin-top:2px; \
                                    border-top: 1px solid rgb(102,162,198); \
                                    border-right: 1px solid rgb(102,162,198); \
                                    border-left: 1px solid rgb(102,162,198);\
                                    } \
                                \
                                .QTabBar::tab:hover{\
                                    background:rgb(197,197,197);} \
                                \
                                .QTabBar::tab:selected:hover{\
                                    background:rgb(237,237,237);} \
                                ")
                                      
        
    def header(self):
        '''
        -----------------------------------
        Otsikkoalue
        -----------------------------------
        '''
        
        self.teksti = QtGui.QLabel("Reseptikirja",self)
        self.teksti.setFont(QtGui.QFont('Cambria', 20))
        self.layout.addWidget(self.teksti,1,0,1,1)
        
        
    def valilehdet(self): 
        '''
        -----------------------------------
        Välilehdet sisältävä laatikko
        -----------------------------------
        '''
        
        self.valilehti = QtGui.QTabWidget()
        self.valilehti.setStyleSheet(self.tab_stylesheet)
        self.valilehti.addTab(self.laatikko,"Etusivu")
        self.valilehti.addTab(self.laatikko1,"Muokkaa ruokakaappia")
        self.valilehti.addTab(self.laatikko2,"Hae reseptejä")
        self.valilehti.addTab(self.laatikko3,"Muokkaa reseptejä")
        self.valilehti.addTab(self.laatikko4,"Muunnin")
        self.layout.addWidget(self.valilehti,2,0,3,4)
        
        
    def etusivu(self):
        '''
        -----------------------------------
        Ensimmäinen ja oletusvälilehti
        -----------------------------------
        '''
        
        self.laatikko = QtGui.QGroupBox()
        self.laatikko.setStyleSheet(".QGroupBox{border:none}")
        self.laatikko.setLayout(self.laatikkolayout)

        
        self.nappi1 = QtGui.QPushButton("paina",self.laatikko)
        self.nappi1.setStyleSheet(self.button_stylesheet)
        
        self.nappi2 = QtGui.QPushButton("paina",self.laatikko)
        self.nappi2.setStyleSheet(self.button_stylesheet)
        

        self.laatikkolayout.addWidget(self.nappi1,0)
        self.laatikkolayout.addWidget(self.nappi2,1)
        self.laatikkolayout.addStretch(0)
        
        
    def kaappi(self):
        '''
        -----------------------------------
        Ruokakaappiosio, näyttää käyttäjän
        ruokakaapin senhetkisen sisällön
        -----------------------------------
        '''
        
        self.kaappi = QtGui.QGroupBox(self)
        self.kaappi.setStyleSheet(self.box_stylesheet)
        self.kaappi.setLayout(self.ruokakaappilayout)
        
        
        #otsikko
        
        self.otsikko_ruokakaappi = QtGui.QLabel("Ruokakaappi")
        self.otsikko_ruokakaappi.setFont(QtGui.QFont('Cambria', 15))
        self.otsikko_ruokakaappi.setStyleSheet(self.label_stylesheet)
        self.ruokakaappilayout.addWidget(self.otsikko_ruokakaappi,0)
        
        
        #sisältö
        try:
            self.oma_kaappi = Ruokakaappi()
            self.aineslista = Ruokakaappi.anna_ainekset(self.oma_kaappi)
            if len(self.aineslista) > 0:
                for aines in self.aineslista:
                    self.rivi = QtGui.QLabel(aines.__str__())
                    self.rivi.setFont(QtGui.QFont('Arial', 10))
                    self.rivi.setStyleSheet(self.laatikkolabel)
                    self.ruokakaappilayout.addWidget(self.rivi,0)
                self.ruokakaappilayout.addStretch(1)
                self.rivi = QtGui.QLabel('Lisää aineksia valitsemalla välilehti "Muokkaa ruokakaappia".')
            else:
                self.rivi = QtGui.QLabel('Ruokakaapissa ei näytä olevan mitään.\nLisää aineksia valitsemalla välilehti "Muokkaa ruokakaappia".')
        except OSError:
            self.rivi = QtGui.QLabel('Ruokakaappia ei pystytty hakemaan.')
            
        self.rivi.setWordWrap(True)
        self.rivi.setFont(QtGui.QFont('Arial', 10))
        self.rivi.setStyleSheet(self.laatikkolabel)
        self.ruokakaappilayout.addWidget(self.rivi,0)
        self.ruokakaappilayout.addStretch(2)
        
        #näytetään kaapin paikka
        
        self.layout.addWidget(self.kaappi,2,4,3,1)    
        
        
    def kaapin_muokkaus(self):
        '''
        -----------------------------------
        Toinen välilehti: kaapissa olevien
        ruoka-aineiden ja niiden määrän
        muokkaustyökalut
        -----------------------------------
        '''
        
        self.laatikko1 = QtGui.QGroupBox()
        self.laatikko1.setStyleSheet(".QGroupBox{border:none}")
        self.laatikko1.setLayout(self.laatikko1layout)

        
        self.nappi3 = QtGui.QPushButton("paina",self.laatikko1)
        self.nappi3.setStyleSheet(self.button_stylesheet)
        

        self.laatikko1layout.addWidget(self.nappi3,0)
        self.laatikko1layout.addStretch(0)
         
    
    def reseptihaku(self):
        '''
        -----------------------------------
        Kolmas välilehti: Reseptien haku
        erilaisten suodattimien avulla
        -----------------------------------
        '''
        
        self.laatikko2 = QtGui.QGroupBox()
        self.laatikko2.setStyleSheet(".QGroupBox{border:none}")
        self.laatikko2.setLayout(self.laatikko2layout)

        
        self.nappi4 = QtGui.QPushButton("paina",self.laatikko2)
        self.nappi4.setStyleSheet(self.button_stylesheet)
        

        self.laatikko2layout.addWidget(self.nappi4,0)
        self.laatikko2layout.addStretch(0)
    
    
    def reseptihallinta(self):
        '''
        -----------------------------------
        Neljäs välilehti: Reseptien
        luominen ja muokkaus
        -----------------------------------
        '''
        
        self.laatikko3 = QtGui.QGroupBox()
        self.laatikko3.setStyleSheet(".QGroupBox{border:none}")
        self.laatikko3.setLayout(self.laatikko3layout)

        
        self.nappi5 = QtGui.QPushButton("paina",self.laatikko3)
        self.nappi5.setStyleSheet(self.button_stylesheet)
        

        self.laatikko3layout.addWidget(self.nappi5,0)
        self.laatikko3layout.addStretch(0)
    
    
    def muunnin(self):
        '''
        -----------------------------------
        Viides välilehti: Käyttäjä voi 
        tehdä haluamiaan muunnoksia tällä
        välilehdellä
        -----------------------------------
        '''
        
        self.muunnin = Muunnin()
        #--------------------------------------laatikon muodostus välilehden sisälle-----------------
        
        self.laatikko4 = QtGui.QGroupBox()
        self.laatikko4.setStyleSheet(".QGroupBox{border:none}")
        self.laatikko4.setLayout(self.laatikko4Vlayout)
        
        #----------------------------------------------------ohjerivit-------------------------------
        
        self.muunninohje = QtGui.QLabel("Täällä voit suorittaa muunnoksia eri mittojen välillä.\nHuomaa, että paino-tilavuus -muunnokset ovat suuntaa antavia.\n ")
        self.muunninohje.setWordWrap(True)
        self.muunninohje.setFont(QtGui.QFont('Arial', 10))
        self.muunninohje.setStyleSheet(self.laatikkolabel)
        self.laatikko4Vlayout.addWidget(self.muunninohje,0)
        
        self.muunninohje3 = QtGui.QLabel("Syötä määrät lukuina ja käytä desimaalierottimena pistettä!\n")
        self.muunninohje3.setWordWrap(True)
        self.muunninohje3.setFont(QtGui.QFont('Arial', 10))
        self.muunninohje3.setStyleSheet(self.laatikkolabel)
        self.laatikko4Vlayout.addWidget(self.muunninohje3,0)
        
        '''self.muunninohje2 = QtGui.QLabel("Tilavuus\n")
        self.muunninohje2.setWordWrap(True)
        self.muunninohje2.setFont(QtGui.QFont('Arial', 10))
        self.muunninohje2.setStyleSheet(self.laatikkolabel)
        self.laatikko4Vlayout.addWidget(self.muunninohje2,0)'''
        
        #----------------------------------------ensimmäisen määrän syöttölaatikko-------------------
        
        self.syote = QtGui.QLineEdit()
        self.syote.setStyleSheet(".QLineEdit {max-width:50px; margin-left:20px;}")
        self.laatikko4Hlayout.addWidget(self.syote,1)
        self.laatikko4Vlayout.addLayout(self.laatikko4Hlayout)
        self.syote.textEdited[str].connect(self.muunnos)
        
        #----------------------------------------ensimmäisen määrän yksikön valinta------------------
        
        self.syoteyksikko = QtGui.QComboBox()
        for i in self.yksikot:
            self.syoteyksikko.addItem(i)
        self.syoteyksikko.setStyleSheet(".QComboBox {max-width:50px;}")
        self.laatikko4Hlayout.addWidget(self.syoteyksikko)
        self.syoteyksikko.activated[str].connect(self.toisinpain)
        
        #----------------------------------------------on-sana tähän väliin--------------------------
        
        self.on = QtGui.QLabel("=")
        self.laatikko4Hlayout.addWidget(self.on)
        self.on.setFont(QtGui.QFont('Arial', 12))
        self.on.setStyleSheet(self.laatikkolabel)
        
        #---------------------------------------------toisen määrän laatikko-------------------------
        
        self.tuloste = QtGui.QLineEdit()
        self.tuloste.setStyleSheet(".QLineEdit {max-width:50px;}")
        self.laatikko4Hlayout.addWidget(self.tuloste,1)
        self.tuloste.textEdited[str].connect(self.toisinpain)
                                        
        #-----------------------------------------toisen määrän yksikön valinta----------------------
        
        self.tulosteyksikko = QtGui.QComboBox()
        for i in self.yksikot:
            self.tulosteyksikko.addItem(i)
        self.tulosteyksikko.setStyleSheet(".QComboBox {max-width:50px;}")
        self.laatikko4Hlayout.addWidget(self.tulosteyksikko)
        self.laatikko4Hlayout.addStretch(0)
        self.laatikko4Vlayout.addStretch(0)
        self.tulosteyksikko.activated[str].connect(self.muunnos)
        
        
    def muunnos(self,text):
        if self.syote.text() != "":
            lahtoarvo = self.syoteyksikko.currentText()
            tuloste = self.tulosteyksikko.currentText()
            try:
                tulos = self.muunnin.tee_muunnos(None,lahtoarvo,tuloste,float(self.syote.text()))
                self.muunninohje3.setStyleSheet(".QLabel {color:rgb(109,109,109)}")
            except ValueError:
                self.tuloste.setText("")
                self.muunninohje3.setStyleSheet(".QLabel {color:red}")
                timer = QtCore.QTimer(self)
                timer.setSingleShot(True)
                timer.start(200)
                timer.timeout.connect(self.muunninerror)
            try:
                self.tuloste.setText("{:.2f}".format(tulos))
            except UnboundLocalError:
                pass
        else:
            self.tuloste.setText("")
            
            
    def muunninerror(self):
        self.muunninohje3.setStyleSheet(".QLabel {color:rgb(109,109,109)}")
        timer = QtCore.QTimer(self)
        timer.setSingleShot(True)
        timer.start(200)
        timer.timeout.connect(self.muunninerror2)
        
        
    def muunninerror2(self):
        self.muunninohje3.setStyleSheet(".QLabel {color:red}")
            
            
    def toisinpain(self,text):
        if self.tuloste.text() != "":
            lahtoarvo = self.tulosteyksikko.currentText()
            tuloste = self.syoteyksikko.currentText()
            try:
                tulos = self.muunnin.tee_muunnos(None,lahtoarvo,tuloste,float(self.tuloste.text()))
                self.muunninohje3.setStyleSheet(".QLabel {color:rgb(109,109,109)}")
            except ValueError:
                self.syote.setText("")
                self.muunninohje3.setStyleSheet(".QLabel {color:red}")
                timer = QtCore.QTimer(self)
                timer.setSingleShot(True)
                timer.start(200)
                timer.timeout.connect(self.muunninerror)
            try:
                self.syote.setText("{:.2f}".format(tulos))
            except UnboundLocalError:
                pass
        else:
            self.syote.setText("")

    
    def toggle_theme(self):
        '''
        -----------------------------------
        Themenvaihtonappula
        -----------------------------------
        '''
        
        self.poksi = QtGui.QCheckBox("Toggle Theme")
        self.layout.addWidget(self.poksi,6,4,1,1)
        self.poksi.stateChanged.connect(self.themechange)
          
       
    def themechange(self):
        '''
        -----------------------------------
        Vaihtaa ohjelman themen kirkkaan
        ja tumman välillä koska miksi ei
        -----------------------------------
        '''
        
        sender = self.sender()
        if sender.isChecked():
                self.setPalette(self.varitt)  
                self.nappi1.setStyleSheet(self.button_stylesheett)
                self.nappi2.setStyleSheet(self.button_stylesheett)
                self.nappi3.setStyleSheet(self.button_stylesheett)
                self.nappi4.setStyleSheet(self.button_stylesheett)
                self.nappi5.setStyleSheet(self.button_stylesheett)
                self.valilehti.setStyleSheet(self.tab_stylesheett)
                self.otsikko_ruokakaappi.setStyleSheet(self.label_stylesheett)
        else:
                self.setPalette(self.varit)
                self.nappi1.setStyleSheet(self.button_stylesheet)
                self.nappi2.setStyleSheet(self.button_stylesheet)
                self.nappi3.setStyleSheet(self.button_stylesheet)
                self.nappi4.setStyleSheet(self.button_stylesheet)
                self.nappi5.setStyleSheet(self.button_stylesheet)
                self.valilehti.setStyleSheet(self.tab_stylesheet)
                self.otsikko_ruokakaappi.setStyleSheet(self.label_stylesheet)


    

         
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Kayttoliittyma()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()