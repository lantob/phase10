#!/usr/bin/env python3

from random import randrange
from source.player import Player
from source.deck import Deck

class Game:
    def __init__(self):
        self.deck = Deck()
        self.players = [Player(self,self.deck) for _ in range(int(input("Wieviele Teilnehmer? ")))]
        self.turn = 1

    def cycle(self):
        while min([len(i.hand) for i in self.players]) > 0: 
            for n in range(len(self.players)):
                print("turn", self.turn, "!", self.players[n].name, "ist dran.")
                print("Es liegt: " + str(self.deck.tray[len(self.deck.tray)-1].show()))
                self.players[n].print_hand()
                self.players[n].act(self.deck)

                n += 1
            self.turn += 1
