# Copyright 2019 Amanda Justiniano amjustin@bu.edu

import os
import yaml
import random


class Card(object):
    """Card object."""
    def __init__(self, value, suit, color=None):
        """Create a Card object"""
        self.value = value
        self.suit = suit
        self.color = color


class CardDeck(object):
    """Create Card Deck."""
    def __init__(self, name="standard", namespace="/decks"):
        """Create CardDeck object."""
        deck_info = open("{}/{}.yaml".format(namespace, name))
        deck_dict = yaml.safe_load(deck_info)
        self.name = deck_dict["name"]
        self.size = deck_dict["size"]
        self.suits = deck_dict["suits"]
        self.values = deck_dict["value_list"]
        self.cards = []

        #Create card objects
        self.__create_deck()

    def __create_deck(self):
        """ Create CardDeck."""
        try:
            for colors in self.suits:
                for color, suits in colors.items():
                    for suit in suits:
                        for val in self.values:
                            self.cards.append(Card(val, suit, color))
        except Exception as err:
            print("Something went wrong creating deck: {} ERR: {}".format(
                self.name, err))

    def shuffle(self):
        """ Shuffle the CardDeck object."""
        try:
            random.shuffle(self.cards)
        except Exception as err:
            print("Something went wrong shuffling the cards: {}", format(err))
