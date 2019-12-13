""" Accordion with Kivy

    Example code from kivy documentation:
    Link: https://kivy.org/doc/stable/api-kivy.uix.accordion.html
"""

import logging
import _thread as thread
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.app import App

from game.War import War

""" TODO: Port this to a json file
"""
GAME = ""
games_available = {
                'Brisca':
                {
                    "Aim of the game": "Collect more points in the tricks won by a player or pair of players than the opponents.",
                    "Deck of cards"  : "It is played with a 40 card Spanish deck.",
                    "Number of players" : "It can be played by two or more players, but normally it is played between two or four. In the latter case, it is played in pairs.",
                    "Order and value of the cards" : "The order, from highest to lowest, is: ace, three, king, knight, jack, seven, six, five, four and deuce.",
                    "Source" : "https://www.nhfournier.es/en/como-jugar/brisca/"
                },

                'War':
                {
                    "Aim of the game": "Collect more points in the tricks won by a player or pair of players than the opponents.",
                    "Deck of cards"  : "It is played with a 40 card Spanish deck.",
                    "Number of players" : "It can be played by two or more players, but normally it is played between two or four. In the latter case, it is played in pairs.",
                    "Order and value of the cards" : "The order, from highest to lowest, is: ace, three, king, knight, jack, seven, six, five, four and deuce.",
                    "Source" : "https://www.nhfournier.es/en/como-jugar/brisca/"
                },

                'Poker':
                {
                    "Aim of the game": "To meld a hand higher in value than that of opponents. It is not necessary for the hand to be better than the others, merely that rivals believe it is, so that they fold before seeing the cards.",
                    "Deck of cards"  : "It is played with a 52 card English deck. Usually two decks of different back colours are used, so that while one is in play, the other is left shuffled beside the player who deals next time. Players decide beforehand whether to use one or both jokers/wild cards, but it is best to play without using any wild cards. The wild cards are used to supplement or represent any other card.",
                    "Number of players" : "Two to seven players can play, although the best games are ideally played by five or six. Each player plays as an individual, without a partner.",
                    "Order and value of the cards" : "The order of the cards, from highest to lowest, is: ace, king (K), queen (Q), jack (J), ten, nine, eight, seven, six, five, four, three and deuce. All suits have the same value in any poker hand.",
                    "Source" : "https://www.nhfournier.es/en/como-jugar/poker/"
                },

                'Black Jack':
                {
                    "Aim of the game": "Collect more points in the tricks won by a player or pair of players than the opponents.",
                    "Deck of cards"  : "It is played with a 40 card Spanish deck.",
                    "Number of players" : "It can be played by two or more players, but normally it is played between two or four. In the latter case, it is played in pairs.",
                    "Order and value of the cards" : "The order, from highest to lowest, is: ace, three, king, knight, jack, seven, six, five, four and deuce.",
                    "Source" : "https://www.nhfournier.es/en/como-jugar/brisca/"
                },

                'Go Fish':
                {
                    "Aim of the game": "Collect more points in the tricks won by a player or pair of players than the opponents.",
                    "Deck of cards"  : "It is played with a 40 card Spanish deck.",
                    "Number of players" : "It can be played by two or more players, but normally it is played between two or four. In the latter case, it is played in pairs.",
                    "Order and value of the cards" : "The order, from highest to lowest, is: ace, three, king, knight, jack, seven, six, five, four and deuce.",
                    "Source" : "https://www.nhfournier.es/en/como-jugar/brisca/"
                }
              }


class AnyCardApp(App):

    def register_cb(self, btn):
        self.game.init()

    def start_cb(self, btn):
        self.game.start()

    def build(self):
        # Create game object
        self.game = War()

        # Create logger
        self.log = logging.getLogger()
        self.log.level = logging.DEBUG

        self.root = Accordion(orientation='vertical')
        self.root.cols=2
        game_titles = list(games_available.keys())
        for i in range(len(game_titles)):
            """ Add each game title to accordion
            """
            self.item = AccordionItem(title='{}'.format(game_titles[i]))

            """ Left hand side; description for each game
            """
            left_col = GridLayout(cols=1)
            left_col.add_widget(Label(text='[size=35]Play [b]{}[/b][/size]'.format(game_titles[i]),
                                      markup=True,
                                      halign='left'))
            left_col.add_widget(Label(text=''))

            curr_game = game_titles[i]
            game_details = games_available[curr_game]
            for info_title in games_available[curr_game].keys():
                left_col.add_widget(Label(text='[size=25][b]{}[/b][/size]\n[size=15]{}[/size]'.format(info_title,game_details[info_title]),
                                              markup=True,
                                              text_size=(400,None),
                                              halign='left',
                                              padding=(5,5)))
                left_col.add_widget(Label(text=''))

            self.item.add_widget(left_col)

            """ Right hand side; register cards and game start
            """
            # self.game = game_titles[i]
            # Create buttons
            self.register = Button(text='Register')
            self.register.bind(on_press=self.register_cb)

            self.start = Button(text='Start Game')
            self.start.bind(on_press=self.start_cb)

            # Create labels and buttons
            self.register_lb = Label(text='Cards registered: {}'.format(0))

            right_col = GridLayout(cols=2)
            right_col.add_widget(self.register_lb)
            right_col.add_widget(self.register)
            right_col.add_widget(Label(text=''))
            right_col.add_widget(self.start)
            self.item.add_widget(right_col)
            self.root.add_widget(self.item)
        return self.root


if __name__ == '__main__':
    AnyCardApp().run()
