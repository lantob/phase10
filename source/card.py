#!/usr/bin/env python3

from random import randrange

class Card:
     def __init__(self,deck):
        while True:
            int_random=randrange(107)
            if deck.numbers[int_random] != "x":
                break
        self.number = deck.numbers[int_random]
        self.color = deck.colors[int_random]
        deck.set_used(int_random)
        if self.number == "J":
            self.value = -1 
        elif self.number == "A":
            self.value = 13
        else:
            self.value=int(self.number)

     def show(self):
        return self.number,self.color

