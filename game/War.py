# Copyright 2019 Amanda Justiniano amjustin@bu.edu

from lib import Game
from lib import CardDeck


class War(Game):
    """Create an instance of the game War."""
    def __init__(self, players=2):
        """Initialize a War game object."""
        super(War, self).__init__("standard", players)

        # Create deck for the game
        self.deck = CardDeck(namespace="../game/decks")

    def create_hand(self):
        """Create Hands for Players."""
        for player in range(self.players):
            self.hands[player] = Hand()

    def gameplay(self):
        """Bulk of the game play should be implemented here.
