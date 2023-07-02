class CardDeck:
    """
    CLass create shuffle deck.
    :argument: __suits
               __ranks
               __deck_counter = -1 , usual counter
    :methods: __init - create shuffle list of cards
              __next - return card from deck
    """
    __suits = ["clubs", "dizmonds", "hearts", "Spades"]
    __ranks = ["Ace", '2', '3', '4', '5', '6', '7', '8', '9', '10', "Jack", "Queen", "King"]
    __deck_counter = -1

    def __init__(self):
        """
        Create shuffle list of cards
        """
        self.__deck = set()
        for suit in CardDeck.__suits:
            for rank in CardDeck.__ranks:
                self.__deck.add(f"{rank} of {suit}")
        self.__deck = list(self.__deck)

    def __next__(self):
        """
        increase counter by 1 and return card
        :return: card
        """
        self.__deck_counter += 1
        return self.__deck[self.__deck_counter]



my_deck = CardDeck()
print(next(my_deck))
print(next(my_deck))
print(next(my_deck))
print(next(my_deck))
print(next(my_deck))
print(next(my_deck))
print(next(my_deck))
