# Copyright 2019 Amanda Justiniano amjustin@bu.edu

from lib import Game
from lib import CardDeck

import logging
import time

"""
Reference: https://bicyclecards.com/how-to-play/war/
THE DEAL
The deck is divided evenly, with each player receiving 26 cards,
dealt one at a time, face down. Anyone may deal first. Each player
places their stack of cards face down, in front of them.

THE PLAY
Each player turns up a card at the same time and the player with
the higher card takes both cards and puts them, face down, on the
bottom of their stack.

If the cards are the same rank, it is War. Each player turns up
one card face down and one card face up. The player with the higher
cards takes both piles (six cards). If the turned-up cards are again
the same rank, each player places another card face down and turns
another card face up. The player with the higher card takes all 10
cards, and so on.

HOW TO KEEP SCORE
The game ends when one player has won all the cards.
"""

class War(Game):
    """Create an instance of the game War."""
    def __init__(self):
        """Initialize a War game object."""
        super(War, self).__init__(1, "standard", 2)

        # Create deck for the game
        self.deck = CardDeck(namespace="../game/decks")
        self.in_play = []

    def switch_turns(self):
        """Simple method to switch turns for the players."""
        for player in range(self.players):
            self.hands[player].turn = not self.hands[player].turn

    def check_winner(self, current_round):
        """Check who won or if a war is declared!"""
        winner = None
        translate_A_K = {'A': 'Z', 'K': 'X'}

        if current_round[0][0].value in translate_A_K.keys():
            card_value = translate_A_K[current_round[0][0].value]
        card_value1 = current_round[0][0].value

        if current_round[1][1].value in translate_A_K.keys():
            card_value = translate_A_K[current_round[1][1].value]
        card_value2 = current_round[1][1].value

        if card_value1 > card_value2:
            winner = card_value1
        elif card_value2 > card_value1:
            winner = card_value2

        return winner

    def create_hands(self):
        """Create Hands for players. (player:deck) dictionary."""
        # Shuffle the deck
        self.deck.shuffle()

        # Split the deck
        deck_half = len(self.deck.cards)//self.players
        deck_halves = [self.deck.cards[:deck_half], self.deck.cards[deck_half:]]
        for player in range(self.players):
            self.hands[player] = Hand(deck_halves[player])
            self.hands[player].register(self.req_hw)

        # Set the first player turn to True so they can start
        self.hands[0].turn = True

    def get_player_info(self):
        """Get the information for the player and display the card value."""
        current = {}
        # Get hw card info from player
        player_hw = self.get_hw()
        if not self.is_turn(player_hw):
            continue

        # Get a value from the deck to display onto the card
        card = self.hands[self.get_player(player_hw)].active.pop(0)
        current[self.get_player(player_hw)] = card

        # Display card onto ePaper
        self.send_info("{} {} {}".format(card.color, card.value, card.suit))
        time.sleep(10)

        self.switch_turns()

        return current

    def start(self):
        """Bulk of the game play should be implemented here."""

        print("Cards are dealt, lets start playing!")
        while(len(self.hands[0].dead) < 52 and len(self.hands[1].dead) < 52):
            # Start up the gameplay!
            cur_round=[]
            print("Player, place a card:")
            for player in range(self.players):
                cur_round.append(get_player_info())

            # Check who won the round.
            self.check_winner()



            # Distributions for each hand after determination of winner

            # Update the score?? This game doesn't need score technically.
