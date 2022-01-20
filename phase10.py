#!/usr/bin/env python3

from random import randrange
# unused from functools import cmp_to_key

class Deck:
    def __init__(self):
        self.numbers = []
        self.colors = []
        self.mix()
    #    self.ucard = []
        self.tray = [] # The tray is the "trashpile"
    #     print("Len numbers" + str(len(self.zahlen)))
        self.tray.append(card(self))

    def mix(self):
        # Create 4 times 2 sets of each number, add 8 Jokers and 4 Skips
        self.numbers = [num+1 for num in range(12) for i in range(2) for y in range(4)] + ["J"]*8+["A"]*4
        # Create 12 times 2 sets of each colour to match the above created numbers
        self.colors = [x for x in ["blue","yellow","red","green"] for a in range(2)]*12 + ["black"]*12

    def set_used(self, pos)
        self.numbers[pos] = "x"
        self.colors[pos] = "x"

#    def draw(self):
     #   self.ucard.append(card(self))

    def shed(self,card):
        self.tray.append(card)


class Card:
     def __init__(self,deck):
        while True:
            int_random=randrange(107)
            if deck.numbers[int_random] != "x":
                break
        self.number = deck.numbers[int_random]
        self.farbe = deck.colors[int_random]
        deck.set_used(int_random)
        if self.number == "J":
            self.value = -1 
        elif self.number == "A":
            self.value = 13
        else:
            self.value=int(self.number)

     def show(self):
        return self.number,self.farbe

class Game:
    def __init__(self):
        self.deck = Deck()
        self.players = [player(self,self.deck) for _ in range(int(input("Wieviele Teilnehmer? ")))]
        self.turn = 1

    def cycle(self):
        while min([len(i.hand) for i in self.players]) > 0: 
            for n in range(len(self.players)):
                print("turn", self.runde, "!", self.players[n].name, "ist dran.")
                print("Es liegt: " + str(self.deck.tray[len(self.deck.tray)-1].show()))
                self.players[n].print_hand()
                self.players[n].act_predraw(self.deck)

                n += 1
            self.turn += 1
                

class Player():
    def __init__(self,game,deck):
        self.name = input("Wie heißt du? ")
        self.phase = 1
        self.punkte = 0
        self.hand = []
        self.hand = [card(deck) for i in range(10)] # [card() for _ in range(10)]
        self.phase_preselection_1 = []
        self.phase_preselection_2 = []
        self.map_requirements1={1:3,2:3,3:4,4:7,5:8,6:9,7:4,8:7,9:5,10:5}
        self.map_requirements2={1:3,2:4,3:4,7:4,9:2,10:3}
        
    def show_hand(self,blatt):
            return list(zip([s.number for s in blatt],[t.farbe for t in blatt]))
    
    def print_hand(self):
        print(self.show_hand(self.hand))

    #unused
    @staticmethod
    def hand(a,b):
        if a.number < b.number:
            return -1
        elif a.number == b.number:
            return 0
        else:
            return 1

    def act_predraw(self,Deck):
        input_predraw = input("(Z)iehen, (B)lind ziehen, (S)ortieren? ") 
        if  input_predraw.upper() == "Z":
            self.hand.append(Deck.tray.pop())
        elif input_predraw.upper() == "B":
            self.hand.append(card(Deck))
        elif input_predraw.upper() == "S":
            #self.hand.sort(key=cmp_to_key(player.hand_sortieren))
            self.hand.sort(key=lambda x:x.value)
            self.print_hand()
            self.act_predraw(Deck)
        else: 
            print("Bitte Buchstaben wählen")
            self.act_predraw()
        self.act_postdraw(Deck)

    def hand_value(self):
        value={1:5,2:5,3:5,4:5,6:5,7:5,8:5,9:5,10:10,11:10,12:10,"A":15,"J":25}
        return sum([value[i.number] for i in self.hand]) 


    def act_postdraw(self,Deck):
        self.print_hand()
        input_postdraw = input("(K)arte wegwerfen, (P)hase legen, (A)nlegen an existierende Phase? " )
        if input_postdraw.upper() == "K":
            int_shed = int(input("Welche card abwerfen? (1-11) ")) - 1
            conf_shed = input(str(self.show_hand(self.hand)[int_shed]) +  "wirklich wegwerfen? (J)a / (N)ein ")
            if conf_shed.upper() == "J":
                    deck.shed((self.hand[int_shed]))  #self.ablegen(self.wegwerfen)
                    del self.hand[int_shed]
            elif conf_shed.upper() == "N":
                    self.act_postdraw()
            else: print("Bitte korrekten Buchstaben wählen!")
        elif input_postdraw.upper() == "P":
            self.play_phase() 
        elif input_postdraw.upper() == "A":
            self
        else: 
            print("Bitte Aktion wählen!")
            self.act_postdraw()

    def shed(self, card):
        tray.cards.append(self.hand[card])
        self.hand.remove(card)

    def play_phase(self):
        condition_required_1 = False
        condition_required_2 = False
        while not self.condition_required_1:
            self.phase_preselection_1.append([self.hand[i] for i in [int(z)-1 for z in str(input("Cards wählen: ")).split(",")]])

            if self.phase in [1,2,3,7,9,10]:
                condition_required_1 = self.samesies(self.phase_preselection_1,1)
                print("condition1: " + str(cond_required_1))
        print("Akzeptiert.")
        while not condition_required_2:
            if self.phase in [1,7,9,10]:
                self.phase_preselection_2.append([self.hand[i] for i in [int(z)-1 for z in str(input("Cards wählen: ")).split(",")]])
                self.phase_preselection_2.sort
                condition_required_2 = self.check_samesies(self.phase_preselection_2,2)


    def check_samesies(self,hand,loop):
        hand.sort()
        if loop == 2:
            map_requirements=self.map_requirements_2
        else:
            map_requirements=self.map_requirements_1

        if hand.count(hand[0])+hand.count("J") >= map_requirements[self.phase]:
            return true
    
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
            return true

    
    def check_colors(self,hand):
        pass 

    
while True:
    game = Game()
    game.cycle()
