# Copyright 2019 Amanda Justiniano amjustin@bu.edu

import logging
import time

from game.lib.game import Game, Hand, GameFailure


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
        super(War, self).__init__("War", 2)
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
            winner = list(current_round[0].keys())
        elif card_value2 > card_value1:
            winner = list(current_round[1].keys())
        elif card_value1 == card_value2:
            print("We have a tie!")
            return -1

        print("Player {} won this round!".format(winner))
        return winner[-1]

    def distribute(self, winner, current_round):
        """Distribute the cards to each hand given the winner."""

        if (winner != -1):
            # Append both cards to the winners hand
            self.hands[winner].dead.append(current_round[0][0])
            self.hands[winner].dead.append(current_round[1][1])

        # If there was a tie, put back the cards
        self.hands[0].active.append(current_round[0][0])
        self.hands[1].active.append(current_round[1][1])


    def create_hands(self):
        """Create Hands for players. (player:deck) dictionary."""
        print("Creating hands!")
        # Shuffle the deck
        self.deck.shuffle()

        # Split the deck
        deck_half = len(self.deck.cards)//self.players
        deck_halves = [self.deck.cards[:deck_half], self.deck.cards[deck_half:]]
        for player in range(self.players):
            self.hands[player] = Hand(deck_halves[player])
            self.hands[player].register(self.req_hw/self.players)
            print("Got RFID: {}".format(self.hands[player].rfids[-1]))

        # Set the first player turn to True so they can start
        self.hands[0].turn = True
        print("Done registering players!")

    def get_player_info(self):
        """Get the information for the player and display the card value."""
        current = {}
        # Get hw card info from player
        while True:
            player_hw = self.get_hw()
            if self.is_turn(player_hw):
                break
            print("It's not your turn!")

        # Get a value from the deck to display onto the card
        card = self.hands[self.get_player(player_hw)].active.pop(0)
        current[self.get_player(player_hw)] = card

        # Display card onto ePaper
        print("Playing card: {} {} {}".format(card.color, card.value, card.suit))
        self.send_info("{} {} {}".format(card.color, card.value, card.suit))
        time.sleep(15)

        self.switch_turns()

        return current

    def start(self):
        """Bulk of the game play should be implemented here."""

        print("Cards are dealt, lets start playing!")
        while(len(self.hands[0].dead) < 52 and len(self.hands[1].dead) < 52):
            # Start up the gameplay!
            curr_round=[]

            # Get the cards from the players
            for player in range(self.players):
                print("Player {}: Please place a card:".format(player))
                curr_round.append(self.get_player_info())

            # Check who won the round.
            winner = self.check_winner(curr_round)

            # Distributions for each hand after determination of winner
            self.distribute(winner, curr_round)

            for player in range(self.players):
                print("Player {} has {} cards in there hands.".format(
                    player, len(self.hands[player].active)))

        for player in range(self.players):
            if len(self.hands[player].dead) >= 52:
                print("Player {} you won!!".format(player))
                break

        return True
