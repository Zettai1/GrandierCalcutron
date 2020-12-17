import numpy as np
import pyqtgraph as pg 
from scipy.stats import hypergeom as hyper
import json

CardDataJSON = "AtomicCards.json"
base_decklist = []
base_sideboardlist = []
decklist_super = []
decklist = []
Compendium = []
Commander_compendium = []
sideboardlist = []
res = []
cmdr_res = []
deck_identity = []
deck_id_res = []
cmdr_identity = []
compendium = []
commanders = []
signatures = []
signature_spells = []
oathbreakers = []
companion = []

#list_o_values = [res, commanders, cmdr_identity, cmdr_res, deck_id_res, deck_identity, decklist, sideboardlist]
#double_list_o_values = [base_sideboardlist, base_decklist]
# "name": "Lim-Dûl's Vault", "printings": ["ALL", "C13", "ME1"], 
#def destroy():
#    for x in list_o_values:
#        globals()[x].clear()
#    for x in double_list_o_values:
#        globals()[x].clear()

#{"data": {"\"Ach! Hans, Run!\"": [{"colorIdentity": ["G", "R"], "colors": ["G", "R"], "convertedManaCost": 6.0, "foreignData": [], "identifiers": {"scryfallOracleId": "a2c5ee76-6084-413c-bb70-45490d818374"}, "layout": "normal", "legalities": {}, "manaCost": "{2}{R}{R}{G}{G}", "name": "\"Ach! Hans, Run!\"", "printings": ["UNH"], "purchaseUrls": {"cardKingdom": "https://mtgjson.com/links/84dfefe718a51cf8", "cardKingdomFoil": "https://mtgjson.com/links/d8c9f3fc1e93c89c", "cardmarket": "https://mtgjson.com/links/b9d69f0d1a9fb80c", "tcgplayer": "https://mtgjson.com/links/c51d2b13ff76f1f0"}, "rulings": [], "subtypes": [], "supertypes": [], "text": "At the beginning of your upkeep, you may say \"Ach! Hans, run! It's the . . .\" and the name of a creature card. If you do, search your library for a card with that name, put it onto the battlefield, then shuffle your library. That creature gains haste. Exile it at the beginning of the next end step.", "type": "Enchantment", "types": ["Enchantment"]}],   

def avg_cmc():
        avgCmc = 0
        X = len(compendium)
        for card in compendium:
            if 'Land' in card['type']:
                X = X-1
            else:
                avgCmc = avgCmc + card['convertedManaCost']
        avgCmc = avgCmc / X
        return avgCmc

def find_total_cmcs():
    cmcs = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    #costs = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0, '13': 0, '14': 0, '15': 0, '16': 0}
    costs = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for card in compendium:
        if 'Land' in card['type']:
            1+1
        else:
            for cmc in cmcs:
                if card['convertedManaCost'] == cmc:
                    costs[(cmc)] += 1
                #print(costs)
    return costs

def get_card_data():
    with open('cards/AtomicCards.json', encoding='utf-8') as json_file:
        atomcards = json.load(json_file)
        data_map = atomcards['data']
        for item in decklist:
            myCards = data_map[f'{item}']
            compendium.extend(myCards)
        for item in commanders:
            myCards = data_map[f'{item}']
            Commander_compendium.extend(myCards)
    for card in compendium:
        identity = card['colorIdentity']
        deck_identity.extend(identity)
    for card in Commander_compendium:
        identity = card['colorIdentity']
        deck_identity.extend(identity)
        cmdr_identity.extend(identity)
    print(len(compendium))
    print(len(Commander_compendium))
    identitysolver()

def identitysolver():
    for i in deck_identity:
        if i not in deck_id_res:
            deck_id_res.append(i)
    for i in cmdr_identity:
        if i not in cmdr_res:
            cmdr_res.append(i)

def print_deck():
    try:
        print("Deck size: "+str(len(decklist)))
        print("Sideboard size: "+str(len(sideboardlist)))
    except:
        print("Deck size: "+str(len(decklist)))

class artisan():
    mindeck = 40
    def decklist_import(filename):
        with open(filename, encoding='utf-8') as file:
                for line in file:
                    if line.startswith("!"):
                        line = line.strip("!")
                        number, name = line.split(" ", maxsplit=1)
                        name = str(name)
                        name = name.strip("\n")
                        try:
                            name, Tag = name.split("@", maxsplit=1)
                            Tag = str(Tag)
                        except:
                            1+1
                        new_cards = [name for _ in range(int(number))]
                        base_sideboardlist.append([number, name])
                        try:
                            print(number+" "+name+" "+Tag)
                        except:
                            print(number+" "+name)
                        sideboardlist.extend(new_cards)
                    else:
                            number, name = line.split(" ", maxsplit=1)
                            name = str(name)
                            name = name.strip("\n")
                            try:
                                name, Tag = name.split("@", maxsplit=1)
                                commandTag = str(Tag)
                            except:
                                1+1
                            new_cards = [name for _ in range(int(number))]
                            base_decklist.append([number, name])
                            try:
                                print(number+" "+name+" "+Tag)
                            except:
                                print(number+" "+name)
                            decklist.extend(new_cards)
    def avg_cmc():
        avgCmc = 0
        X = len(compendium)
        for card in compendium:
            if 'Land' in card['type']:
                X = X-1
            else:
                avgCmc = avgCmc + card['convertedManaCost']
        avgCmc = avgCmc / X
        return avgCmc

    def find_total_cmcs():
        cmcs = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
        #costs = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0, '13': 0, '14': 0, '15': 0, '16': 0}
        costs = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for card in compendium:
            if 'Land' in card['type']:
                1+1
            else:
                for cmc in cmcs:
                    if card['convertedManaCost'] == cmc:
                        costs[(cmc)] += 1
                    #print(costs)
        return costs
    
class commander():
    maxdeck = 100
    mindeck = 100
    def decklist_import(filename):
        with open(filename, encoding='utf-8') as file:
                for line in file:
                    commandTag = 0
                    companion_Tag = 0
                    number, name = line.split(" ", maxsplit=1)
                    name = str(name)
                    name = name.strip("\n")
                    try:
                        name, Tag = name.split("@", maxsplit=1)
                        if Tag.upper() == 'CMDR':
                            commandTag = str(Tag)
                        elif Tag.upper() == 'COMPANION':
                            companion_Tag = str(Tag)
                    except:
                        1+1
                    if type(commandTag) is str:
                        try:
                            #print(number+" "+name+" "+commandTag)
                            commanders.append(name)
                            #decklist_super.append(name)
                        except:
                            1+1
                    elif type(companion_Tag) is str:
                        try:
                            companion.append(name)
                        except:
                            1+1
                    elif type(commandTag) is int and type(companion_Tag) is int:
                        try:
                            #print(number+" "+name)
                            new_cards = [name for _ in range(int(number))]
                            base_decklist.append([number, name])
                            decklist.extend(new_cards)
                            decklist_super.extend(new_cards)
                        except:
                           1+1
                    
    def avg_cmc():
        avgCmc = 0
        X = len(compendium)
        for card in compendium:
            if 'Land' in card['type']:
                X = X-1
            else:
                avgCmc = avgCmc + card['convertedManaCost']
        avgCmc = avgCmc / X
        return avgCmc

    def find_total_cmcs():
        cmcs = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
        #costs = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0, '13': 0, '14': 0, '15': 0, '16': 0}
        costs = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for card in compendium:
            if 'Land' in card['type']:
                1+1
            else:
                for cmc in cmcs:
                    if card['convertedManaCost'] == cmc:
                        costs[(cmc)] += 1
                    #print(costs)
        return costs

    def find_hyp_geom_dist(name):
        pmf = hyper.pmf
        hands = [7, 6, 5, 4, 3, 2, 1]
        size = 0
        count = 0
        for card in compendium:
            if card['name'] == name:
                count = count + 1
        size = size + (len(compendium))
        #for hand in hands:
        #    h = hand
        #    x2 = np.arange(0, count+1)
        #    s = hyper.mean(size, count, h)
        #    s = np.array([s])
        #    try:
        #        binomial_output = np.concatenate((binomial_output, s))
        #    except:
        #        binomial_output = np.array(s)
        for x in range(size):
            if x < size:
                x2 = np.arange(0, count+1)
                s = pmf(size, count, 1, 1)
                s = np.array([s*100])
                try:
                    output = np.concatenate((output, s))
                except:
                    output = np.array(s)
        print(output)
        print(name)
        return output
    
    #def find_mana_production():
    #    mana_producers = []
    #    mana_pool = []
    #    colors_of_mana = ['{W}','{U}','{B}','{R}','{G}','{C}']
    #    for card in compendium:
            #for card['text:']:
    #        for color in colors_of_mana:
    #            if 'Add' in card['text'] and color in card['text']:
    #                print((card['name'])+f' can produce {color} mana')
    #                mana_producers.append(card['name'])
    #    for producer in mana_producers:
    #        for card in compendium:
    #            if producer == card['name'] and card['convertedManaCost'] == 0:
    #                for color in colors_of_mana:
    #                    if 'Add' in card['text'] and color in card['text']:
    #                        print((f' can produce {color} mana')


class oathbreaker():
    def decklist_import(filename):
        with open(filename) as file:
                for line in file:
                    oathTag = 0
                    number, name = line.split(" ", maxsplit=1)
                    name = str(name)
                    name = name.strip("/n")
                    try:
                        name, oathTag = name.split("@", maxsplit=1)
                        oathTag = str(oathTag)
                        if oathTag == "OATH":
                            oathbreakers.extend(name)
                        elif oathTag == "SIG":
                            signatures.extend(name)
                    except:
                        1+1
                    number = number.strip("x")
                    new_cards = [name for _ in range(int(number))]
                    base_decklist.append([number, name])
                    if type(oathTag) is str:
                        try:
                            print(number+" "+name+" "+oathTag)
                        except:
                            print(number+" "+name)
                    elif type(oathTag) is int:
                        try:
                            print(number+" "+name)
                        except:
                            print("Could not print card name!")
                    #try:
                    #    card_data = get_card_data(card=name, ZF=commander, commandertag=str(commandTag))
                    #except:
                    #    card_data = get_card_data(card=name, ZF=commander, commandertag="")
                    decklist.extend(new_cards)
#        identitysolver()
#        print(str_cmdr_res)
#        print(str_deck_id_res)
#        print(deck_id_res)

class free_form():
    mindeck = 40
    def decklist_import(filename):
        with open(filename, encoding='utf-8') as file:
                for line in file:
                    if line.startswith("!"):
                        line = line.strip("!")
                        number, name = line.split(" ", maxsplit=1)
                        name = str(name)
                        name = name.strip("\n")
                        try:
                            name, Tag = name.split("@", maxsplit=1)
                            Tag = str(Tag)
                        except:
                            1+1
                        new_cards = [name for _ in range(int(number))]
                        base_sideboardlist.append([number, name])
                        try:
                            print(number+" "+name+" "+Tag)
                        except:
                            print(number+" "+name)
                        sideboardlist.extend(new_cards)
                    else:
                            number, name = line.split(" ", maxsplit=1)
                            name = str(name)
                            name = name.strip("\n")
                            try:
                                name, Tag = name.split("@", maxsplit=1)
                                commandTag = str(Tag)
                            except:
                                1+1
                            new_cards = [name for _ in range(int(number))]
                            base_decklist.append([number, name])
                            try:
                                print(number+" "+name+" "+Tag)
                            except:
                                print(number+" "+name)
                            decklist.extend(new_cards)
    def avg_cmc():
        avgCmc = 0
        X = len(compendium)
        for card in compendium:
            if 'Land' in card['type']:
                X = X-1
            else:
                avgCmc = avgCmc + card['convertedManaCost']
        avgCmc = avgCmc / X
        return avgCmc

    def find_total_cmcs():
        cmcs = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
        #costs = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0, '13': 0, '14': 0, '15': 0, '16': 0}
        costs = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for card in compendium:
            if 'Land' in card['type']:
                1+1
            else:
                for cmc in cmcs:
                    if card['convertedManaCost'] == cmc:
                        costs[(cmc)] += 1
                    #print(costs)
        return costs

class standard():
    mindeck = 60
    def decklist_import(filename):
        with open(filename) as file:
                for line in file:
                    number, unfiltered_name = line.split(" ", maxsplit=1)
                    unfiltered_name += str(unfiltered_name)
                    print(unfiltered_name)
                    name, commandTag = unfiltered_name.split("@", maxsplit=1)
                    cmdr_status = commnadTag.split("/n", maxsplit=1)
                    new_cards = [name for _ in range(int(number))]
                    base_decklist.append([number, name])
                    get_card_data(name, status=cmder_status)
                    decklist.extend(new_cards)

class highlander():
    maxdeck = 100
    mindeck = 100
    def decklist_import(filename):
        with open(filename) as file:
                for line in file:
                    number, unfiltered_name = line.split(" ", maxsplit=1)
                    unfiltered_name += str(unfiltered_name)
                    print(unfiltered_name)
                    name, commandTag = unfiltered_name.split("@", maxsplit=1)
                    cmdr_status = commnadTag.split("/n", maxsplit=1)
                    new_cards = [name for _ in range(int(number))]
                    base_decklist.append([number, name])
                    get_card_data(name, status=cmder_status)
                    decklist.extend(new_cards)

class prismatic():
    maxdeck = 1
    mindeck = 250
    cmdr_status = "WUBRG"
    def decklist_import(filename):
        with open(filename) as file:
                for line in file:
                    number, unfiltered_name = line.split(" ", maxsplit=1)
                    unfiltered_name += str(unfiltered_name)
                    print(unfiltered_name)
                    name, Tag = unfiltered_name.split("@", maxsplit=1)
                    Tagged = Tag.split("/n", maxsplit=1)
                    new_cards = [name for _ in range(int(number))]
                    base_decklist.append([number, name, Tag])
                    get_card_data(name, status=cmder_status)
                    decklist.extend(new_cards)