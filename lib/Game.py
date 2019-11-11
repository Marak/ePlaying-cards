# Copyright 2019 Amanda Justiniano amjustin@bu.edu

import CardDeck


class Hand(object):
    """Base class to represent each player's hand."""
    def __init__(self, cards):
        """Create the player's hand with specified cards.

        Args:
            cards (list): List of card objects belonging to the hand.
        """
        self.cards = cards
        self.turn = None
        self.in_play = []
        self.dead = []

    def place(self, card):
        """Place card or cards in game play."""


    def collect(self):
        """ Collect cards that belong to hand."""

class Game(object):
    """Central game framework class."""
    def __init__(self, deck_type, players=2):
        """Create a template game object which will be the base object for
        all games.

        Args:
            deck_type (str): deck type i.e. standard, spanish, other
            players (int, optional): The number of players for the game.
                Defaults to 2.
        """
        self.deck = CardDeck() # will create standard 52 card deck
        self.hands = {}
        self.players = players

    def __create_hand(self):
        """Create Hands for Players."""
        for player in range(self.players):
            self.hands[player] = Hand()

    def deal_cards(self):
        """Distribute cards to each player."""


    def discard(self, cards):
        """Place cards in game graveyard pile.

        Args:
            cards (list): List of Card objects to be discarded.
        """
        try:
            for card in cards:
                graveyard.append(card)
        except Exception as err:
            print("Something went wrong on the graveyard. ERR: {}".format(err))

    def save(self):
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
