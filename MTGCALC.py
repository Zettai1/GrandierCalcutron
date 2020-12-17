import json
import numpy as np
import math
import os
import PyQt5
import random as rng
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
import matplotlib.pyplot as plt
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
#import matplotlib.pyplot.figure as Figure
from importlib import import_module
import fmtdata as fmtda
import seaborn as sb
from matplotlib import cm
from numpy import linspace
import pandas as pd

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grandier Calcutron")
        self.setWindowIcon(QIcon('UI/icons/icon.ico'))
        self.setGeometry(0, 0, 1920, 1080)
        label = QLabel(self)
        pixmap = QPixmap("UI/background.png")
        label.setPixmap(pixmap)
        label.show()
        base_UI = QLabel(self)
        base_pixmap = QPixmap("UI/UI_BASE")
        base_pixmap = base_pixmap.scaled(1920,1080,Qt.KeepAspectRatio, Qt.FastTransformation)
        base_UI.setPixmap(base_pixmap)
        base_UI.move(0,0)
        base_UI.resize(1920, 1080)
        base_UI.show()
        help_button = QPushButton(self)
        help_button.setIcon(QIcon("UI/icons/help_ico.png"))
        help_button.setStyleSheet("border-radius: 20px;")
        help_button.setIconSize(QSize(60, 60))
        help_button.setToolTip("How to import a Deck")
        help_button.move(919, 233)
        help_button.resize(62, 62)
        help_button.show()
        self.Welcome_Message()

    def Welcome_Message(self):
        Y = 10
        X = 100
        Scale_X = 120
        Scale_Y = 30
        welcome_message = QLabel("Welcome to the Grandier Calcutron!", self)
        welcome_message.setFont(QFont("Arial",16))
        welcome_message.move(390, 210)
        tutorial_message_1 = QLabel("Import a deck to begin!", self)
        tutorial_message_1.setFont(QFont("Arial",16))
        tutorial_message_1.setAlignment(Qt.AlignCenter)
        tutorial_message_1.move(462, 250)
        Import_Deck = QPushButton(self)
        Import_Sym = QPixmap("UI/icons/import_sym")
        Import_Sym = QIcon(Import_Sym)
        Import_Deck.setIcon(Import_Sym)
        Import_Deck.setIconSize(QSize(250, 250))
        Import_Deck.clicked.connect(self.import_click)
        Import_Deck.clicked.connect(welcome_message.hide)
        Import_Deck.clicked.connect(tutorial_message_1.hide)
        Import_Deck.clicked.connect(Import_Deck.hide)
        Import_Deck.move(0, 19)
        Import_Deck.setStyleSheet("background: #ffab3f; border-radius: 125px;")
        Import_Deck.setToolTip("Import a Deck")

    def display_color_event(self):
        X = 2
        Y = 19
        SCALE = 250
        if len(fmtda.deck_id_res) == 5:
            if 'G' in fmtda.deck_id_res and 'U' in fmtda.deck_id_res and 'R' in fmtda.deck_id_res and 'B' in fmtda.deck_id_res and 'W' in fmtda.deck_id_res:
                color_icon = QPixmap("symbols/WUBRG.PNG")
            color_icon_label = QLabel(self)
            color_icon = color_icon.scaled(SCALE, SCALE, Qt.KeepAspectRatio, Qt.FastTransformation)
            color_icon_label.setPixmap(color_icon)
            color_icon_label.move(X, Y)
            color_icon_label.show()
        elif len(fmtda.deck_id_res) == 4:
            if 'W' not in fmtda.deck_id_res:
                color_icon = QPixmap("symbols/UBRG.PNG")
            elif 'U' not in fmtda.deck_id_res:
                color_icon = QPixmap("symbols/BRGW.PNG")
            elif 'B' not in fmtda.deck_id_res:
                color_icon = QPixmap("symbols/RGWU.PNG")
            elif 'R' not in fmtda.deck_id_res:
                color_icon = QPixmap("symbols/GWUB.PNG")
            elif 'G' not in fmtda.deck_id_res:
                color_icon = QPixmap("symbols/WUBR.PNG")
        else:
            if fmtda.deck_id_res == ['W','U'] or fmtda.deck_id_res == ['U','W']:
                color_icon = QPixmap("symbols/WU.PNG")
            elif fmtda.deck_id_res == ['U','B'] or fmtda.deck_id_res == ['B','U']:
                color_icon = QPixmap("symbols/UB.PNG")
            elif fmtda.deck_id_res == ['B','R'] or fmtda.deck_id_res == ['R','B']:
                color_icon = QPixmap("symbols/BR.PNG")
            elif fmtda.deck_id_res == ['R','G'] or fmtda.deck_id_res == ['G','R']:
                color_icon = QPixmap("symbols/RG.PNG")
            elif fmtda.deck_id_res == ['W','G'] or fmtda.deck_id_res == ['G','W']:
                color_icon = QPixmap("symbols/GW.PNG")
            elif fmtda.deck_id_res == ['B','W'] or fmtda.deck_id_res == ['W','B']:
                color_icon = QPixmap("symbols/BW.PNG")
            elif fmtda.deck_id_res == ['U','R'] or fmtda.deck_id_res == ['R','U']:
                color_icon = QPixmap("symbols/UR.PNG")
            elif fmtda.deck_id_res == ['B','G'] or fmtda.deck_id_res == ['G','B']:
                color_icon = QPixmap("symbols/BG.PNG")
            elif fmtda.deck_id_res == ['R','W'] or fmtda.deck_id_res == ['W','R']:
                color_icon = QPixmap("symbols/RW.PNG")
            elif fmtda.deck_id_res == ['U','G'] or fmtda.deck_id_res == ['G','U']:
                color_icon = QPixmap("symbols/UG.PNG")
            elif 'U' in fmtda.deck_id_res and 'G' in fmtda.deck_id_res and 'W' in fmtda.deck_id_res:
                color_icon = QPixmap("symbols/GWU.PNG")
            elif 'U' in fmtda.deck_id_res and 'B' in fmtda.deck_id_res and 'W' in fmtda.deck_id_res:
                color_icon = QPixmap("symbols/WUB.PNG")
            elif 'U' in fmtda.deck_id_res and 'B' in fmtda.deck_id_res and 'R' in fmtda.deck_id_res:
                color_icon = QPixmap("symbols/UBR.PNG")
            elif 'G' in fmtda.deck_id_res and 'R' in fmtda.deck_id_res and 'B' in fmtda.deck_id_res:
                color_icon = QPixmap("symbols/GRB.PNG")
            elif 'R' in fmtda.deck_id_res and 'G' in fmtda.deck_id_res and 'W' in fmtda.deck_id_res:
                color_icon = QPixmap("symbols/RGW.PNG")
            elif 'W' in fmtda.deck_id_res and 'B' in fmtda.deck_id_res and 'G' in fmtda.deck_id_res:
                color_icon = QPixmap("symbols/WBG.PNG")
            elif 'U' in fmtda.deck_id_res and 'R' in fmtda.deck_id_res and 'W' in fmtda.deck_id_res:
                color_icon = QPixmap("symbols/URW.PNG")
            elif 'B' in fmtda.deck_id_res and 'G' in fmtda.deck_id_res and 'U' in fmtda.deck_id_res:
                color_icon = QPixmap("symbols/BGU.PNG")
            elif 'G' in fmtda.deck_id_res and 'U' in fmtda.deck_id_res and 'R' in fmtda.deck_id_res:
                color_icon = QPixmap("symbols/GUR.PNG")
            elif fmtda.deck_id_res == ['W']:
                color_icon = QPixmap("symbols/W.PNG")
            elif fmtda.deck_id_res == ['U']:
                color_icon = QPixmap("symbols/U.PNG")
            elif fmtda.deck_id_res == ['B']:
                color_icon = QPixmap("symbols/B.PNG")
            elif fmtda.deck_id_res == ['R']:
                color_icon = QPixmap("symbols/R.PNG")
            elif fmtda.deck_id_res == ['G']:
                color_icon = QPixmap("symbols/G.PNG")
            else:
                color_icon = QPixmap("symbols/C.png")
        color_icon_label = QLabel(self)
        new_color_icon = color_icon.scaled(SCALE, SCALE, Qt.KeepAspectRatio, Qt.FastTransformation)
        color_icon_label.setPixmap(new_color_icon)
        color_icon_label.move(X, Y)
        color_icon_label.show()

    def stats(self):
        thing = []
        xxx = ''
        print('graphing...')
        x = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
        if __Format__ == 'commander':
            #y = fmtda.commander.find_total_cmcs()
            #z = fmtda.commander.avg_cmc()
            #plt.bar(x,y,tick_label=x)
            #plt.savefig('figs/manacurve.png')
            
            #ManaLabel = QLabel(self)
            #manaCurve = QPixmap('figs/manacurve.png')
            #ManaLabel.draw(plt)
            #manaCurve = manaCurve.scaled(512, 384, Qt.KeepAspectRatio, Qt.FastTransformation)
            #ManaLabel.setPixmap(manaCurve)
            #ManaLabel.move(1300,500)
            #ManaLabel.show()
            #Mana_Curve_Label = QLabel(f'Converted Mana Costs.  Average CMC: {z}', self)
            #Mana_Curve_Label.move(1340,530)
            #Mana_Curve_Label.setFont(QFont('Arial', 11))
            #Mana_Curve_Label.show()
            #plt.close()
            #fmtda.commander.find_mana_production()
            comp = fmtda.compendium
            self.hype()
        elif __Format__ == 'artisan':
            #y = fmtda.artisan.find_total_cmcs()
            #z = fmtda.artisan.avg_cmc()
            #plt.bar(x,y,tick_label=x)
            #plt.savefig('figs/manacurve.png')
            #plt.close()
            #ManaLabel = QLabel(self)
            #manaCurve = QPixmap('figs/manacurve.png')
            #manaCurve.scaled(400, 300, Qt.KeepAspectRatio, Qt.FastTransformation)
            #ManaLabel.setPixmap(manaCurve)
            #ManaLabel.move(1300,500)
            #ManaLabel.show()
            #Mana_Curve_Label = QLabel(f'Converted Mana Costs.  Average CMC: {z}', self)
            #Mana_Curve_Label.move(1340,530)
            #Mana_Curve_Label.setFont(QFont('Arial', 11))
            #Mana_Curve_Label.show()
            #fmtda.commander.find_mana_production()
            comp = fmtda.compendium
            self.hype()
        
    def hype(self):
        x = []
        z = []
        zzzz = []
        canvas = mana_plot(self)
        canvas.move(1100, 50)
        canvas.show()

        x1 = len(fmtda.compendium)
        
                #y = fmtda.commander.find_hyp_geom_dist(name=card['name'])
                #z.append(y)
        for value in range(x1):
            x.append(value)

    

    def Buttons(self):
        export_button = QPushButton(self)
        export_button.setIcon(QIcon("UI/icons/Xport_ico.png"))
        export_button.setStyleSheet("border-radius: 20px;")
        export_button.setIconSize(QSize(60, 60))
        export_button.setToolTip("Export Deck")
        export_button.move(919, 233)
        export_button.resize(62, 62)
        export_button.show()
        #stats_button = QPushButton(self)
        #stats_button.setIcon(QIcon("UI/icons/statsicoV2.png"))
        #stats_button.setStyleSheet("border-radius: 20px;")
        #stats_button.setIconSize(QSize(60, 60))
        #stats_button.setToolTip("Deck Stats")
        #stats_button.clicked.connect(stats_button.hide)
        #stats_button.clicked.connect(self.stats)
        #stats_button.move(324, 311)
        #stats_button.resize(62, 62)
        #stats_button.show()

    def import_click(self):
        global __Format__
        self.openFileNameDialog()
        ext = os.path.splitext(deckFile)[-1].lower()
        if ext == ".cmdr":
            __Format__ = "commander"
            fmtda.commander.decklist_import(deckFile)
            label = QLabel(self)
            pixmap = QPixmap("UI/UI_LEADER.png")
            pixmap = pixmap.scaled(1920,1080,Qt.KeepAspectRatio, Qt.FastTransformation)
            label.setPixmap(pixmap)
            label.move(0,0)
            label.resize(1920, 1080)
            label.show()
            format_label = QLabel("Format: Commander", self)
            format_label.setToolTip("\u2022 Each deck must contain exactly 100 cards, including the commander(s).\n\u2022 A player cannot include more than one copy of any individual card in their deck unless it is a basic land or a card that specifically states otherwise (e.g. Shadowborn Apostle).\n\u2022 No cards in any player's deck may have a color identity that does not match or is not a subset of the color identity of the commander(s). The color identity of a card is composed of its colors plus the colors of every colored mana symbol that appears on the card, whether in its mana cost or its rules text; for double-faced cards, the colors and text boxes of both faces count. Hybrid mana symbols count as both halves' colors for this purpose.\n\u2022 When choosing a commander, you must use either a legendary creature, a planeswalker with the ability to be commander, or a pair of legendary creatures or planeswalkers that both have partner. The chosen card or pair is called the commander or general of the deck. Decks may contain other legendary creatures and planeswalkers within them as well.")
            format_label.setFont(QFont("Arial", 14))
            format_label.move(17, 311)
            format_label.resize(300, 30)
            format_label.show()
            print("Gettting card data...")
            fmtda.get_card_data()
            print("Card data obtained!")
            self.Buttons()
            self.stats()
            self.display_color_event()
            self.decklist_display()
        elif ext == ".oath":
            __Format__ = "oath"
            fmtda.oathbreaker.decklist_import(deckFile)
            self.Buttons()     
            self.display_color_event()
            self.decklist_display(formatword="oath-breaker")       
        elif ext == ".stand":
            __Format__ = "stand"
            fmtda.standard.decklist_import(deckFile)
            self.display_color_event()   
            self.decklist_display()     
        elif ext == ".free":
            __Format__ = "free"
            fmtda.free_form.decklist_import(deckFile)
            label = QLabel(self)
            pixmap = QPixmap("UI/UI_BASE.png")
            pixmap = pixmap.scaled(1920,1080,Qt.KeepAspectRatio, Qt.FastTransformation)
            label.setPixmap(pixmap)
            label.move(0,0)
            label.resize(1920, 1080)
            label.show()
            format_label = QLabel("Format: Freeform", self)
            format_label.setToolTip("\u2022 Freeform is a sanctioned casual Magic Online format that allows all sets and cards.\n\u2022 Regular deckbuilding rules are relaxed; In that:\n\u2022 decks can contain any number of copies of a card; multiple Vanguard cards may be included.\n\u2022 The only restriction is a 40-card minimum deck.")
            format_label.setFont(QFont("Arial", 14))
            format_label.move(17, 311)
            format_label.resize(300, 30)
            format_label.show()
            self.Buttons()
            print("Gettting card data...")
            fmtda.get_card_data()
            print('Card data obtained!')
            self.display_color_event()  
            self.decklist_display()
        elif ext == ".arti":
            __Format__ = "artisan"
            fmtda.artisan.decklist_import(deckFile)
            label = QLabel(self)
            pixmap = QPixmap("UI/UI_BASE.png")
            pixmap = pixmap.scaled(1920,1080,Qt.KeepAspectRatio, Qt.FastTransformation)
            label.setPixmap(pixmap)
            label.move(0,0)
            label.resize(1920, 1080)
            label.show()
            format_label = QLabel("Format: Artisan", self)
            format_label.setToolTip("\u2022 An artisan deck uses only cards of Common or Uncommon rarity.\n\u2022 Minimum of 60 cards in the main deck (Maximum 250 cards for main decks)\n\u2022 Up to 15 cards in your sideboard, if used \n\u2022 Quadrupleton (Except for Basic Lands)")
            format_label.setFont(QFont("Arial", 14))
            format_label.move(17, 311)
            format_label.resize(300, 30)
            format_label.show()
            self.Buttons()
            print("Gettting card data...")
            fmtda.get_card_data()
            print('Card data obtained!')
            self.display_color_event()  
            self.stats()    
            self.decklist_display()
        
        
        #import_deck.hide()

    def decklist_display(self):
        if __Format__ == 'commander':
            lis = fmtda.base_decklist
            compendium = fmtda.compendium
            commanderlis = fmtda.commanders
            lis3 = fmtda.Commander_compendium
            Y_BASE = 350
            X_BASE = 20
            X = 20
            X2 = 100
            Y = 350
            Y2 = 100
            for num, card in lis:
                label = QLabel(f"{num}x {card}", self)
                label.setFont(QFont("Arial",10))
                for card_comp in compendium:
                    if card_comp['name'] == card:
                        SS = card_comp['name']
                        try:
                            SSS = card_comp['manaCost']
                        except:
                            SSS = ''
                        SSSS = card_comp['text']
                        label.setToolTip(f'{SS}, cost: {SSS}\n{SSSS}')
                label.move(X, Y)
                label.show()
                Y = Y+20
                Y2 = Y2+30
                if Y > 950 and X < 320:
                    Y = Y_BASE
                    Y_BASE = Y
                    X = X+300
                elif Y > 950:
                    Y = Y_BASE
                    X = X+300

            Y = Y_BASE-100
            X = X_BASE+320
            for card in commanderlis:
                label = QLabel(f"{card}", self)
                label.setFont(QFont("Arial",14))
                for card_comp in lis3: #BROKEN
                    if card_comp['name'] == card:
                        SS = card_comp['name']
                        try:
                            SSS = card_comp['manaCost']
                        except:
                            SSS = ''
                        SSSS = card_comp['text']
                        label.setToolTip(f'{SS}, cost: {SSS}\n{SSSS}')
                label.move(X, Y)
                label.show()
                Y = Y+26
                if Y > (Y_BASE-140)+26:
                    Y = Y_BASE-140
                    X = X+333
        elif __Format__ == 'artisan':
            lis = fmtda.base_decklist
            lis2 = fmtda.compendium
            Y_BASE = 350
            X_BASE = 20
            X = 20
            X2 = 100
            Y = 350
            Y2 = 100
            for num, card in lis:
                label = QLabel(f"{num}x {card}", self)
                label.setFont(QFont("Arial",10))
                for card_comp in lis2:
                    if card_comp['name'] == card:
                        SS = card_comp['name']
                        try:
                            SSS = card_comp['manaCost']
                            SSS = f', cost: {SSS}'
                        except:
                            SSS = ''
                        SSSS = card_comp['text']
                        label.setToolTip(f'{SS}{SSS}\n{SSSS}')
                label.move(X, Y)
                label.show()
                Y = Y+20
                Y2 = Y2+30
                if Y > 950 and X < 320:
                    Y = Y_BASE
                    Y_BASE = Y
                    X = X+300
                elif Y > 950:
                    Y = Y_BASE
                    X = X+300
        elif __Format__ == 'free':
            lis = fmtda.base_decklist
            lis2 = fmtda.compendium
            Y_BASE = 350
            X_BASE = 20
            X = 20
            X2 = 100
            Y = 350
            Y2 = 100
            for num, card in lis:
                label = QLabel(f"{num}x {card}", self)
                label.setFont(QFont("Arial",10))
                for card_comp in lis2:
                    if card_comp['name'] == card:
                        SS = card_comp['name']
                        try:
                            SSS = card_comp['manaCost']
                            SSS = f', cost: {SSS}'
                        except:
                            SSS = ''
                        SSSS = card_comp['text']
                        label.setToolTip(f'{SS}{SSS}\n{SSSS}')
                label.move(X, Y)
                label.show()
                Y = Y+20
                Y2 = Y2+30
                if Y > 950 and X < 320:
                    Y = Y_BASE
                    Y_BASE = Y
                    X = X+300
                elif Y > 950:
                    Y = Y_BASE
                    X = X+300
    
    def openFileNameDialog(self):
        global deckFile
        deckfile = 0
        #fmtda.destroy
        #self.messages.hide()
        #self.hicons
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","Commander files (*.cmdr);;Oath Breaker files (*.oath);;Standard files (*.stand);;Free Form files (*.free);;Artisan files (*.arti)", options=options)
        deckFile = fileName

class mana_plot(FigureCanvas):
    def __init__(self, parent=None, width = 10, height = 8, dpi=100):
        fig = plt.figure(figsize=(width, height), dpi=dpi, facecolor=(1,1,1,0), edgecolor=(1,1,1,0))
        self.axes = fig.add_subplot(111)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        self.mana_pie_plot()
        self.cmc_plot()
    def mana_pie_plot(self):
        size = 0.5
        Types_of_mana = ['{W}', '{U}', '{B}', '{R}', '{G}']
        PIPS = []
        W = 0
        U = 0
        B = 0
        R = 0
        G = 0
        WPRO = 0
        UPRO = 0
        BPRO = 0
        RPRO = 0
        GPRO = 0
        color_values = []
        color_values_PRO = []
        pie_colors = []
        pie_colors_pro = []
        WHEX = '#fffbd5'
        WHEXPRO = '#fffce6'
        UHEX = '#aae0fa'
        UHEXPRO = '#b7e4fa'
        BHEX = '#cbc2bf'
        BHEXPRO = '#ddd7d5'
        RHEX = '#f9aa8f'
        RHEXPRO = '#fbc8b6'
        GHEX = '#9bd3ae'
        GHEXPRO = '#cae8d4'
        for card in fmtda.compendium:
            if 'manaCost' in card:
                cost_in_pips = card['manaCost']
                cost_in_pips = cost_in_pips.strip("1")
                cost_in_pips = cost_in_pips.strip("2")
                cost_in_pips = cost_in_pips.strip("3")
                cost_in_pips = cost_in_pips.strip("4")
                cost_in_pips = cost_in_pips.strip("5")
                cost_in_pips = cost_in_pips.strip("6")
                cost_in_pips = cost_in_pips.strip("7")
                cost_in_pips = cost_in_pips.strip("8")
                cost_in_pips = cost_in_pips.strip("9")
                cost_in_pips = cost_in_pips.strip("10")
                cost_in_pips = cost_in_pips.strip("11")
                cost_in_pips = cost_in_pips.strip("12")
                cost_in_pips = cost_in_pips.strip("13")
                cost_in_pips = cost_in_pips.strip("14")
                cost_in_pips = cost_in_pips.strip("15")
                cost_in_pips = cost_in_pips.strip("16")
                cost_in_pips = cost_in_pips.strip("0")
                cost_in_pips = cost_in_pips.strip('{')
                cost_in_pips = cost_in_pips.strip('}')
                PIPS.extend(cost_in_pips)
        for pip in PIPS:
            if pip == 'W':
                W = W + 1
            if pip == 'U':
                U = U + 1 
            if pip == 'B':
                B = B + 1 
            if pip == 'R':
                R = R + 1 
            if pip == 'G':
                G = G + 1
        for card in fmtda.compendium:
            card_name = card['name']
            if "Add" in card['text']:
                cardtex = card['text']
                types = card['types']
                cmc = card['convertedManaCost']
                for color in Types_of_mana:
                    if color in cardtex:
                        if 'Land' in  types and cmc == 0:
                            if '{W}' in cardtex:
                                WPRO = WPRO + cardtex.count('{W}')
                            elif '{U}' in cardtex:
                                UPRO = UPRO + cardtex.count('{U}')
                            elif '{B}' in cardtex:
                                BPRO = BPRO + cardtex.count('{B}')
                            elif '{R}' in cardtex:
                                RPRO = RPRO + cardtex.count('{R}')
                            elif '{G}' in cardtex:
                                GPRO = GPRO + cardtex.count('{G}')
                            elif 'Add one mana of any color.' in cardtex:
                                WPRO = WPRO + cardtex.count('{W}')
                                UPRO = UPRO + cardtex.count('{U}')
                                BPRO = BPRO + cardtex.count('{B}')
                                RPRO = RPRO + cardtex.count('{R}')
                                GPRO = GPRO + cardtex.count('{G}')
                        elif 'Instant' not in types and 'Sorcery' not in types:
                            if '{W}' in cardtex:
                                WPRO = WPRO + ((cardtex.count('{W}'))/(cmc + 1))
                            elif '{U}' in cardtex:
                                UPRO = UPRO + ((cardtex.count('{U}'))/(cmc + 1))
                            elif '{B}' in cardtex:
                                BPRO = BPRO + ((cardtex.count('{B}'))/(cmc + 1))
                            elif '{R}' in cardtex:
                                RPRO = RPRO + ((cardtex.count('{R}'))/(cmc + 1))
                            elif '{G}' in cardtex:
                                GPRO = GPRO + ((cardtex.count('{G}'))/(cmc + 1))
                            elif 'Add one mana of any color.' in cardtex:
                                WPRO = WPRO + ((cardtex.count('{W}'))/(cmc + 1))
                                UPRO = UPRO + ((cardtex.count('{U}'))/(cmc + 1))
                                BPRO = BPRO + ((cardtex.count('{B}'))/(cmc + 1))
                                RPRO = RPRO + ((cardtex.count('{R}'))/(cmc + 1))
                                GPRO = GPRO + ((cardtex.count('{G}'))/(cmc + 1))
                        elif 'Instant' in types or 'Sorcery' in types:
                            if '{W}' in cardtex:
                                WPRO = WPRO + ((cardtex.count('{W}'))/(cmc + 2))
                            elif '{U}' in cardtex:
                                UPRO = UPRO + ((cardtex.count('{U}'))/(cmc + 2))
                            elif '{B}' in cardtex:
                                BPRO = BPRO + ((cardtex.count('{B}'))/(cmc + 2))
                            elif '{R}' in cardtex:
                                RPRO = RPRO + ((cardtex.count('{R}'))/(cmc + 2))
                            elif '{G}' in cardtex:
                                GPRO = GPRO + ((cardtex.count('{G}'))/(cmc + 2))
                            elif 'Add one mana of any color.' in cardtex:
                                WPRO = WPRO + ((cardtex.count('{W}'))/(cmc + 1))
                                UPRO = UPRO + ((cardtex.count('{U}'))/(cmc + 1))
                                BPRO = BPRO + ((cardtex.count('{B}'))/(cmc + 1))
                                RPRO = RPRO + ((cardtex.count('{R}'))/(cmc + 1))
                                GPRO = GPRO + ((cardtex.count('{G}'))/(cmc + 1))

        print(f'White pips: {W}')
        print(f'White production: {WPRO}')
        print(f'Blue pips: {U}')
        print(f'Blue production: {UPRO}')
        print(f'Black pips: {B}')
        print(f'Black production: {BPRO}')
        print(f'Red pips: {R}')
        print(f'Red production: {RPRO}')
        print(f'Green pips: {G}')
        print(f'Green production: {GPRO}')
        ax = self.figure.add_subplot(1, 1, 1)
        #ax.axis('equal')
        if W != 0 and U != 0 and B != 0 and R != 0 and G != 0:
            colors = ['White', 'Blue', 'Black', 'Red', 'Green']
        elif W != 0 and U != 0 and B != 0 and R != 0:
            colors = ['White', 'Blue', 'Black', 'Red']
        elif W != 0 and U != 0 and B != 0 and R == 0 and G != 0:
            colors = ['White', 'Blue', 'Black', 'Green']
        elif W != 0 and U != 0 and B == 0 and R != 0 and G != 0:
            colors = ['White', 'Blue', 'Red', 'Green']
        elif W != 0 and U == 0 and B != 0 and R != 0 and G != 0:
            colors = ['White', 'Black', 'Red', 'Green']
        elif W != 0 and U != 0 and B == 0 and R != 0 and G != 0:
            colors = ['Blue', 'Black', 'Red', 'Green']
        elif W != 0 and U != 0 and B != 0 and R == 0 and G == 0:
            colors = ['White', 'Blue', 'Black']
        elif W != 0 and U != 0 and B == 0 and R == 0 and G != 0:
            colors = ['White', 'Blue', 'Green']
        elif W != 0 and U == 0 and B == 0 and R != 0 and G != 0:
            colors = ['White', 'Red', 'Green']
        elif W == 0 and U == 0 and B != 0 and R != 0 and G != 0:
            colors = ['Black', 'Red', 'Green']
        elif W == 0 and U != 0 and B != 0 and R != 0 and G == 0:
            colors = ['Blue', 'Black', 'Red']
        elif W != 0 and U != 0 and B == 0 and R != 0 and G == 0:
            colors = ['White', 'Blue', 'Red']
        elif W != 0 and U == 0 and B != 0 and R == 0 and G != 0:
            colors = ['White', 'Black', 'Green']
        elif W == 0 and U != 0 and B == 0 and R != 0 and G != 0:
            colors = ['Blue', 'Red', 'Green']
        elif W != 0 and U == 0 and B != 0 and R != 0 and G == 0:
            colors = ['White', 'Black', 'Red']
        elif W == 0 and U != 0 and B != 0 and R == 0 and G != 0:
            colors = ['Blue', 'Black', 'Green']
        elif W != 0 and U == 0 and B == 0 and R != 0 and G == 0:
            colors = ['White', 'Red']
        elif W != 0 and U == 0 and B == 0 and R == 0 and G != 0:
            colors = ['White', 'Green']
        elif W != 0 and U == 0 and B != 0 and R == 0 and G == 0:
            colors = ['White', 'Black']
        elif W != 0 and U != 0 and B == 0 and R == 0 and G == 0:
            colors = ['White', 'Blue']
        elif W == 0 and U != 0 and B == 0 and R != 0 and G == 0:
            colors = ['Blue', 'Red']
        elif W == 0 and U != 0 and B != 0 and R == 0 and G == 0:
            colors = ['Blue', 'Black']
        elif W == 0 and U != 0 and B == 0 and R == 0 and G != 0:
            colors = ['Blue', 'Green']
        elif W == 0 and U == 0 and B != 0 and R != 0 and G == 0:
            colors = ['Black', 'Red']
        elif W == 0 and U == 0 and B != 0 and R == 0 and G != 0:
            colors = ['Black', 'Green']
        elif W == 0 and U == 0 and B == 0 and R != 0 and G != 0:
            colors = ['Red', 'Green']
        elif W == 0 and U == 0 and B == 0 and R == 0 and G != 0:
            colors = ['Green']
        elif W == 0 and U == 0 and B == 0 and R != 0 and G == 0:
            colors = ['Red']
        elif W == 0 and U == 0 and B != 0 and R == 0 and G == 0:
            colors = ['Black']
        elif W == 0 and U != 0 and B == 0 and R == 0 and G == 0:
            colors = ['Blue']
        elif W != 0 and U == 0 and B == 0 and R == 0 and G == 0:
            colors = ['White']
        for color in colors:
            if color == 'White':
                color_values.append(W)
                color_values_PRO.append(WPRO)
                pie_colors.append(WHEX)
                pie_colors_pro.append(WHEXPRO)
            elif color == 'Blue':
                color_values.append(U)
                color_values_PRO.append(UPRO)
                pie_colors.append(UHEX)
                pie_colors_pro.append(UHEXPRO)
            elif color == 'Black':
                color_values.append(B)
                color_values_PRO.append(BPRO)
                pie_colors.append(BHEX)
                pie_colors_pro.append(BHEXPRO)
            elif color == 'Red':
                color_values.append(R)
                color_values_PRO.append(RPRO)
                pie_colors.append(RHEX)
                pie_colors_pro.append(RHEXPRO)
            elif color == 'Green':
                color_values.append(G)
                color_values_PRO.append(GPRO)
                pie_colors.append(GHEX)
                pie_colors_pro.append(GHEXPRO)
        #ax.setp(autotexts, size=8, weight="bold")
        ax.pie(color_values, labels = colors, radius=1, autopct='%1.1f%%', colors = pie_colors, pctdistance=0.8)
        ax.pie(color_values_PRO, radius=1-size, autopct='%1.1f%%', colors = pie_colors_pro)
        ax.set(aspect="equal", title='Pips and Production')
        #plt.
        #Pie_Label = QLabel(self)
        #Pie_Pie = QPixmap(f'figs/mana_pie.png')
        #Pie_Pie = Pie_Pie.scaled(512, 384, Qt.KeepAspectRatio, Qt.FastTransformation)
        #Pie_Label.setPixmap(Pie_Pie)
        #Pie_Label.move(1300,50) #1300x50
        #Pie_Label.resize(320,240)
        #Pie_Label.show()
    def cmc_plot(self):
        ay = self.figure.add_subplot(4, 4, 6)
        x = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
        y = fmtda.find_total_cmcs()
        z = fmtda.avg_cmc()
        ay.bar(x,y,tick_label=x)
        ay.set(aspect='equal', title=f'Mana Costs, AVG CMC: {z}')
        #plt.savefig('figs/manacurve.png')

app = QApplication(sys.argv)

screen = Window()
screen.show()
sys.exit(app.exec_())