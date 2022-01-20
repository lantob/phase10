# /usr/bin/env python3

from random import randrange
from source.card import Card
import logging

log = logging.getLogger("player")

# unused from functools import cmp_to_key
class Player():
    def __init__(self,game,deck):
        self.name = input("Wie heißt du? ")
        self.phase = 1
        self.punkte = 0
        self.hand = []
        self.hand = [Card(deck) for i in range(10)] # [card() for _ in range(10)]
        self.phase_preselection_1 = []
        self.phase_preselection_2 = []
        self.map_requirements_1={1:3,2:3,3:4,4:7,5:8,6:9,7:4,8:7,9:5,10:5}
        self.map_requirements_2={1:3,2:4,3:4,7:4,9:2,10:3}
        
    def show_hand(self,hand):
            return list(zip(["K"+str(i+1) for i in range(len(hand))], zip([s.number for s in hand],[t.color for t in hand])))
    
    def print_hand(self):
        print("-"*10+"\n" + str(self.show_hand(self.hand)))

    #unused
    @staticmethod
    def hand(a,b):
        if a.number < b.number:
            return -1
        elif a.number == b.number:
            return 0
        else:
            return 1

    def act(self,deck):
        self.act_predraw(deck)
        self.act_postdraw(deck)
        print("-"*10)

    def act_predraw(self,deck):
        input_predraw = input("(Z)iehen, (B)lind ziehen, (S)ortieren, nach (P)aaren sortieren, nach (F)arben sortieren? ") 
        if  input_predraw.upper() == "Z":
            self.hand.append(deck.tray.pop())
        elif input_predraw.upper() == "B":
            self.hand.append(Card(deck))
        elif input_predraw.upper() == "S":
            #self.hand.sort(key=cmp_to_key(player.hand_sortieren))
            self.hand.sort(key=lambda x:x.value)
            self.print_hand()
            self.act_predraw(deck)
        elif input_predraw.upper() == "P":
            self.hand.sort(key=lambda x:count(x.value))
            self.print_hand()
        elif input_predraw.upper() == "F":
            pass
        else: 
            print("Bitte Buchstaben wählen")
            self.act_predraw(deck)

    def hand_points(self):
        value={1:5,2:5,3:5,4:5,6:5,7:5,8:5,9:5,10:10,11:10,12:10,"A":15,"J":25}
        return sum([value[i.number] for i in self.hand]) 


    def act_postdraw(self,deck):
        self.print_hand()
        input_postdraw = input("\n" + "-"*10+"\n(K)arte wegwerfen, (P)hase legen, (A)nlegen an existierende Phase? " )
        if input_postdraw.upper() == "K":
            int_shed = int(input("Welche Karte abwerfen? (1-11) ")) - 1
            confirm_shed = input(str(self.show_hand(self.hand)[int_shed]) +  "wirklich wegwerfen? (J)a / (N)ein ")
            if confirm_shed.upper() == "J":
                    deck.shed((self.hand[int_shed]))  #self.ablegen(self.wegwerfen)
                    del self.hand[int_shed]
                    log.debug("Karte abgeworfen")
            elif confirm_shed.upper() == "N":
                    self.act_postdraw(deck)
            else: print("Bitte korrekten Buchstaben wählen!")
        elif input_postdraw.upper() == "P":
            self.play_phase(deck) 
        elif input_postdraw.upper() == "A":
            pass 
        else: 
            print("Bitte Aktion wählen!")
            self.act_postdraw(deck)

#unused
#    def shed(self, card):
     #   tray.cards.append(self.hand[card])
     #   self.hand.remove(card)

    def play_phase(self,deck):
        condition_required_1 = False
        condition_required_2 = False
        strRound = ""

        phase_type = {1:"samesies",2:"samesies",3:"samesies",4:"sequence",5:"sequence",6:"sequence",7:"samesies",8:"color",9:"samesies",10:"samesies"}
        phase_type2 = {1:"samesies",2:"sequence",3:"sequence",7:"samesies",9:"samesies",10:"samesies"}
        while not condition_required_1:
            self.phase_preselection_1 = [self.hand[i] for i in [int(z)-1 for z in str(input(strRound +  "Karten wählen: ")).split(",")]]
            strRound = "Andere " 
            log.debug(self.phase_preselection_1)

            if self.phase in [1,2,3,7,9,10]:
                log.debug("Check Samesies:" + str(self.check_samesies(self.phase_preselection_1,1)))
                condition_required_1 = self.check_samesies(self.phase_preselection_1,1)
                log.debug("condition1: " + str(condition_required_1))
        print("Akzeptiert.")
        if self.phase in [4,5,6,8]:
            condition_required_2 = True
        else:
            while not condition_required_2:
                    self.phase_preselection_2 = [self.hand[i] for i in [int(z)-1 for z in str(input("Cards wählen: ")).split(",")]]
                    condition_required_2 = self.check_samesies(self.phase_preselection_2,2)
        print("Akzeptiert.")
        deck.place_phase(self.phase_preselection_1, phase_type[self.phase])
        if phase_type2 != None:
            deck.place_phase(self.phase_preselection_2, phase_type2[self.phase])
        print("Glückwunsch! Phase " + str(self.phase) + " geschafft!")
        self.phase += 1
        self.act_postphase()

    def act_postphase():
        pass
        


    def check_samesies(self,hand,loop):
        hand.sort(reverse=True,key=lambda x:x.value)
        if loop == 2:
            map_requirements=self.map_requirements_2
        else:
            map_requirements=self.map_requirements_1
            #hand.count(hand[0].zahl)+hand.count("J")
        log.debug(sum(h.number==hand[0].number for h in hand))
        if sum(h.number == hand[0].number for h in hand) + sum(h.number == "J" for h in hand)  >= map_requirements[self.phase]:
            return True
    
    def check_sequence(self,hand,loop):
        n=0

        if loop == 2:
            map_requirements=self.map_requirements_2
        else:
            map_requirements=self.map_requirements_1

        for i in hand:
            if hand[i] == hand[i+1] or hand[i+1] == "J":
                n += 1
        if n >= map_requirements[phase]:
            return True

    
    def check_colors(self,hand):
        pass 

