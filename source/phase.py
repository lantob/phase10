import logging

class Phase:
    def __init__(self,hand, input_type):
        self.cards = []
        self.type = input_type
        if input_type == "samesies":
            value = hand[0].number
        elif input_type == "color":
            value = hand[0].color
        else:
            value = ""

