#!/usr/bin/env python3

from random import randrange
from source.card import Card
from source.phase import Phase

# unused from functools import cmp_to_key

class Deck:
    def __init__(self):
        self.numbers = []
        self.colors = []
        self.mix()
        self.tray = [] # The tray is the "trashpile"
        self.tray.append(Card(self))
        self.board = []

    def mix(self):
        # Create 4 times 2 sets of each number, add 8 Jokers and 4 Skips
        self.numbers = [num+1 for num in range(12) for i in range(2) for y in range(4)] + ["J"]*8+["A"]*4
        # Create 12 times 2 sets of each colour to match the above created numbers
        self.colors = [x for x in ["blue","yellow","red","green"] for a in range(2)]*12 + ["black"]*12

    def set_used(self, pos):
        self.numbers[pos] = "x"
        self.colors[pos] = "x"

    def shed(self,card):
        self.tray.append(card)

    def place_phase(self,hand,input_type):
        self.board.append(Phase(hand, input_type))
        
