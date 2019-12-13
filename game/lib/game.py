# Copyright 2019 Amanda Justiniano amjustin@bu.edu

import sys
import logging

from time import sleep
from .deck import CardDeck
from .rfid_info import get_card
from .send_info import writeData


class GameFailure(Exception):
    """Base exception for this module."""

class Hand(object):
    """Base class to represent each player's hand."""
    def __init__(self, cards):
        """Create the player's hand with specified cards.

        Args:
            cards (list): List of card objects belonging to the hand.
        """
        self.cards = cards
        self.active = cards
        self.dead = []
        self.rfids = []
        self.turn = None

    def place(self, card):
        """Place card in game play."""
        temp = card
        self.active.remove(card)
        return temp

    def collect(self, cards):
        """ Collect cards that belong to hand."""
        for card in cards:
            self.dead.append(card)

    def register(self, req_hw):
        """ Register the cards that will be playing for this hand."""
        try:
            while(len(self.rfids) < req_hw):
                self.rfids.append(get_card())
        except Exception as err:
            print("Something went wrong getting RFIDs! ERR {}".format(err))


class Game(object):
    """Central game framework class."""
    def __init__(self, name, req_hw, deck_type="standard", players=2):
        """Create a template game object which will be the base object for
        all games.

        Args:
            req_hw (int): Number of required HW cards per player.
            deck_type (str): deck type i.e. standard, spanish, other
            players (int, optional): The number of players for the game.
                Defaults to 2.
        """
        self.name = name
        self.deck = CardDeck(name=deck_type)  # will create standard 52 card deck
        self.graveyard = []  # The graveyard starts empty on init of game.
        self.hands = {}
        self.players = players
        self.req_hw = req_hw
        self.log = logging.getLogger()
        self.log.level = logging.DEBUG

    def is_hw_registered(self):
        """Check if the game physical cards have been registered."""
        if (self.hands):
            count = 0
            for hand in hands.values():
                if hand.rfids:
                    count = count + 1
            if count == len(hands):
                return True
        return False

    def is_turn(self, player_hw):
        """Check if it is the players turn given the provided RFID value."""
        status = False
        player = self.get_player(player_hw)
        if self.hands[player].turn == True:
            status = True

        return status

    def get_player(self, player_hw):
        """Get player ID from the provided RFID value."""
        found = False
        ret_player = None
        for player in range(self.players):
            if player_hw in self.hands[player].rfids:
                ret_player = player
                found = True
                break
        if not found:
            raise GameFailure(
                "Not able to find player for HW: {}".format(player_hw))

        return ret_player

    def get_hw(self):
        """Get a card from the hw of the user. Return card RFID to the user
        once it has been scanned."""
        return get_card()

    def send_info(self, info):
        """Send information to the HW. The write data should return."""
        return writeData(info)

    def init(self):
        """Initialize the game, setup the HW cards and virtual deck."""
        print("Welcome to game of {}.".format(self.name))
        try:
            self.create_hands()
        except Exception as err:
            print("Something went wrong dealing the cards. ERR: {}".format(err))

    def discard(self, cards):
        """Place cards in game graveyard pile.

        Args:
            cards (list): List of Card objects to be discarded.
        """
        try:
            for card in cards:
                self.graveyard.append(card)
        except Exception as err:
            print("Something went wrong dicarding cards: {} ERR: {}".format(
                cards, err))

    def create_hands(self):
        """Create Hands for Players. This method should ovewritten by each
        individual game."""
        pass

    def start(self):
        """ Function to build the logic of the game. This method should
        ovewritten by each individual game."""
        pass

    def save(self, game_name):
        """Save the progress of the game. This method will save game data to
        later be loaded by the players."""
        pass

    def load(self):
        """Load previously saved file of an in-progress game. This will restore
        all players hands, game score and game state."""
        pass

    def update(self):
        """Method to update the game score according to the rules set in each
        specific game. This method should be ovewritten to fit specific rules
        of each game.
        """
        pass
