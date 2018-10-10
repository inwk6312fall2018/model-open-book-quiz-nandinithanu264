
"""
example modified from - https://pycarddeck.readthedocs.io/en/latest/examples/poker.html
P.s - Code runs out of attribute
 
"""
# get equired references
import pyCardDeck
from typing import List
from pyCardDeck.cards import PokerCard


# intializing player 
class Player:

    def __init__(self, name: str):
        self.hand = []
        self.name = name

    def __str__(self):
        return self.name

#group of players created
class PokerTable:

    def __init__(self, players: List[Player]):
        self.deck = pyCardDeck.Deck(
            cards=generate_deck(),
            name='Poker deck',
            reshuffle=False)
        self.players = players
        self.table_cards = []
        print("Created a table with {} players".format(len(self.players)))

#main loop for the game to run

def texas_holdem(self):
    """
    Basic Texas Hold'em game structure
    """
    print("Starting a round of Texas Hold'em")
    self.deck.shuffle()
    self.deal_cards(2)
    self.flop()
    self.river_or_flop()
    self.river_or_flop()
    self.cleanup()
 
#random cards are dealt to players

def deal_cards(self, number: int):
    for _ in range(0, number):
        for player in self.players:
            card = self.deck.draw()
            player.hand.append(card)
            print("Dealt {} to player {}".format(card, player))

#deck of cards generated

def generate_deck() -> List[PokerCard]:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = {'A': 'Ace',
             '2': 'Two',
             '3': 'Three',
             '4': 'Four',
             '5': 'Five',
             '6': 'Six',
             '7': 'Seven',
             '8': 'Eight',
             '9': 'Nine',
             '10': 'Ten',
             'J': 'Jack',
             'Q': 'Queen',
             'K': 'King'}
    cards = []
    for suit in suits:
        for rank, name in ranks.items():
            cards.append(PokerCard(suit, rank, name))
    print('Generated deck of cards for the table')
    return cards\

#main entry to the game

if __name__ == '__main__':
    table = PokerTable([Player("Jay"), Player("Joe"), Player("Jim")])
    table.texas_holdem()


