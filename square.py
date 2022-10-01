import numpy as np
from random import shuffle


# CONSTANT VALUES FOR SETUP

SUITS = np.array(["diamonds", "clubs", "spades", "hearts"])
VALUES = np.linspace(1, 13, 13)


# Class for the cards that are used to play.
class Card:
    # Each card has a suit and a value.
    def __init__(self, suit: str, value: int):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

    # Defining equalities and inequalities based on the cards values.
    def __gt__(self, other):
        return self.value > other.value

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value


# Defines a pile of cards and allows the manipulation of said pile.
class CardPile:

    # Each pile starts with only one card
    def __init__(self, starting_card: Card):
        self.height = 1
        self.cards = [starting_card]

    def __repr__(self):
        return f"On top: {self.cards[-1]}, height: {self.height}"

    # Method for checking if card is smaller, greater or the same value as the card before
    # and placing it on top.
    def add_to_top(self, card):
        size_diff = 0

        # Checks if the given card has higher value than the top card on the pile.
        if self.cards[-1] < card:
            size_diff += 1

        # In the case that the cards value is lower than the value of the highest card.
        # If neither of these statements are True, the card must be of the same value.
        elif self.cards[-1] > card:
            size_diff -= 1

        # Finally, sets the new card on top and updates the stack's height.
        self.cards.append(card)
        self.height += 1

        # Returns the information whether the new card was smaller, the same or higher -value
        # than the previous card.
        return size_diff

    # Allows for the viewing of the uppermost card.
    def show_top_card(self):
        return self.cards[-1]

    # Gives the height of the card stack.
    def get_height(self):
        return self.height


# Defines the table that the game is played on.
class Table:
    def __init__(self, size):
        self.card_piles = []
        self.size = size
        self.stage = 0
        self.cards_in_deck = []

    def __repr__(self):
        return f"Table is set"

    def set_the_square_table(self):
        # Creates the deck of 52 playing cards. (without joker -cards)
        cards = []
        for i in range(4):
            for j in range(13):
                cards.append(Card(SUITS[i], int(VALUES[j])))

        # Randomly selects a specified amount of cards for the start.
        shuffle(cards)
        start_cards = cards[:self.size]
        self.cards_in_deck = cards[self.size:]

        # Creates the card piles for the starts
        for card in start_cards:
            self.card_piles.append(CardPile(card))

    # Places the next card in the deck onto the specified pile on the table.
    # The value of parameter guess is either -1, 0 or 1. They mean lower-, same and -higher value than
    # the current top card on the pile.
    def place_on_pile(self, pile: int, guess: int):
        card_to_place = self.cards_in_deck.pop(0)
        result = self.card_piles[pile].add_to_top(card_to_place)

        # Returns whether the guess was right or not
        if guess == result:
            print("correct\n")
        else:
            print("Wrong\n")

    def print_table(self):
        print(f"1  2  3")
        print(f"{self.card_piles[0].show_top_card()}  {self.card_piles[1].show_top_card()}  {self.card_piles[2].show_top_card()}")
        print(f"{self.card_piles[3].show_top_card()}  {self.card_piles[4].show_top_card()}  {self.card_piles[5].show_top_card()}")
        print(f"{self.card_piles[6].show_top_card()}  {self.card_piles[7].show_top_card()}  {self.card_piles[8].show_top_card()}\n")

    def set_next_stage(self, num_of_piles: int):
        self.stage += 1


# Keeps track of the players and advances the game.
class Dealer(Table):
    def __init__(self, *args: str, size=9):
        self.number_of_players = len(args)
        self.players = []
        for i in args:
            self.players.append(i)
        self.table = Table(size)
        self.table.set_the_square_table()
        self.size = size

    def get_size(self):
        return self.size

    def guess(self, pile: int, guess: int):
        self.table.place_on_pile(pile, guess)

    def whose_turn(self):
        i = 0
        while True:
            if i == len(self.players):
                i = 0
            yield self.players[i]
            i += 1

def main():
    game = Dealer("Lauri", "Henrik")
    #print(game.number_of_players)
    #(game.players)
    player = game.whose_turn()

    while True:


        print(next(player))
        game.table.print_table()
        pile = int(input(f"Which pile (0-{game.get_size()}): "))

        guess = int(input("Greater: 1, same: 0, smaller: -1. Guess: "))
        game.guess(pile, guess)




if __name__ == "__main__":
    main()
