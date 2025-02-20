from typing import List
import random
import os


class Card:
    def __init__(self, name: str, value: int):
        self.name: str = name
        self.value: int = value


class Deck:
    def __init__(self):
        self._cards: List[Card] = list()  # list of total cards, not used in game
        self._deck_cards: List[Card] = (
            list()
        )  # list of cards left in deck, cards pulled are removed from this deck

    def addCard(self, card: Card):
        """NOTE: Only used while creating the Deck
        | DO NOT USE IN GAME"""
        # print(f"adding {card.name}")
        self._cards.append(card)
        # print(f"added, not length is {len(self._cards)}")
        self.shuffle()

    def shuffle(self):
        """returns all cards to the deck cards set, assuming all cards were taken from players"""
        self._deck_cards = self._cards.copy()

    def pullCard(self) -> Card:
        """returns random card from those that have not been pulled after last shuffle"""
        card: Card = self._deck_cards.pop(
            random.randint(0, len(self._deck_cards) - 1)
        )  # "pull" random card from the deck
        return card


class Hand:
    def __init__(self):
        self._cards: List[Card] = list()

    def addCard(self, card: Card):
        self._cards.append(card)

    def getTotalValue(self):
        sum = 0
        for card in self._cards:
            sum += card.value
        return sum

    def __getitem__(self, key):
        return self._cards[key]

    def __len__(self):
        return len(self._cards)

    def play(self):
        """returns all cards and removes them from hand"""
        res = self._cards.copy()
        self._cards.clear()
        return res


class BlackJack:
    def __init__(self):
        self._deck = Deck()
        self._dealer_hand = Hand()
        self._player_hand = Hand()
        self._player_money = 1000
        self._min_bet = 100
        self._bet_increase = 100
        self._current_bet = self._min_bet

        for i in range(2, 10 + 1):
            self._deck.addCard(Card(f"♣ {i} of clubs", i))
            self._deck.addCard(Card(f"♦ {i} of diamonds", i))
            self._deck.addCard(Card(f"♥ {i} of hearts", i))
            self._deck.addCard(Card(f"♠ {i} of spades", i))

        self._deck.addCard(Card(f"♣ Ace of clubs", 1))
        self._deck.addCard(Card(f"♦ Ace of diamonds", 1))
        self._deck.addCard(Card(f"♥ Ace of hearts", 1))
        self._deck.addCard(Card(f"♠ Ace of spades", 1))

        self._deck.addCard(Card(f"♣ Jack of clubs", 10))
        self._deck.addCard(Card(f"♦ Jack of diamonds", 10))
        self._deck.addCard(Card(f"♥ Jack of hearts", 10))
        self._deck.addCard(Card(f"♠ Jack of spades", 10))

        self._deck.addCard(Card(f"♣ Queen of clubs", 10))
        self._deck.addCard(Card(f"♦ Queen of diamonds", 10))
        self._deck.addCard(Card(f"♥ Queen of hearts", 10))
        self._deck.addCard(Card(f"♠ Queen of spades", 10))

        self._deck.addCard(Card(f"♣ King of clubs", 10))
        self._deck.addCard(Card(f"♦ King of diamonds", 10))
        self._deck.addCard(Card(f"♥ King of hearts", 10))
        self._deck.addCard(Card(f"♠ King of spades", 10))

    def _getPlayerInput(self):
        while True:
            player_input = input(">> : ")
            if not player_input.isalnum():
                print("ivalid input")
                continue
            player_input = int(player_input)
            if player_input not in [1, 2, 3, 0]:
                print("plese choose valid option")
                continue
            return player_input

    def _printOnTurn(self):
        print("┏━┏━━━━━━━━━━━━━┓━┓")
        print("┣┣━┫ blackjack ┣━┫┫")
        print("┗━┗━━━━━━━━━━━━━┛━┛")

        print("Dealer cards: ")
        for i in range(len(self._dealer_hand)):
            if i == 1:
                print(f"  X\t| secret card")
            else:
                print(f"  {self._dealer_hand[i].value}\t| {self._dealer_hand[i].name}")

        print("\nYour cards: ")
        for card in self._player_hand:
            print(f"  {card.value}\t| {card.name}")
        print(f"  {self._player_hand.getTotalValue()}\t| total score")

        print(f"\nYour bet  : {self._current_bet}")
        print(f"\nYour money: {self._player_money}")
        print("\n1. Hit")
        print("2. Stand")
        print("3. Increase bet")
        print("0. Exit game")

    def _printOnEnd(self):
        print("┏━┏━━━━━━━━━━━━━┓━┓")
        print("┣┣━┫ blackjack ┣━┫┫")
        print("┗━┗━━━━━━━━━━━━━┛━┛")

        print("Dealer cards: ")
        for i in range(len(self._dealer_hand)):
            print(f"  {self._dealer_hand[i].value}\t| {self._dealer_hand[i].name}")
        print(f"  {self._dealer_hand.getTotalValue()}\t| total score")

        print("\nYour cards: ")
        for card in self._player_hand:
            print(f"  {card.value}\t| {card.name}")
        print(f"  {self._player_hand.getTotalValue()}\t| total score")

    def _dealerCardsCheck(self):
        attempt_count = 0
        while True:
            attempt_count += 1
            willTakeCard = False
            player_score = self._player_hand.getTotalValue()
            dealer_score = self._dealer_hand.getTotalValue()
            diff = 21 - dealer_score
            if player_score < dealer_score:
                return
            if player_score == dealer_score:
                if dealer_score > 18:
                    return  # not worth the risk
                else:
                    willTakeCard = (
                        True if diff >= 10 else 1 == random(1, int(15 / diff))
                    )  # chance to take the card
            if self._player_hand.getTotalValue() > dealer_score:
                willTakeCard = (
                    True if diff >= 10 else 1 == random(1, int(15 / diff))
                )  # chance to take the card, smaller if risk is higher

            if willTakeCard:
                self._dealer_hand.addCard(self._deck.pullCard())
                return
            elif attempt_count >= 3:
                return

    def _moneyResult(self, bet_multiplier):
        self._player_money += self._current_bet * bet_multiplier
        self._current_bet = self._min_bet

    def _cardsReset(self):
        self._player_hand.play()
        self._dealer_hand.play()
        self._deck.shuffle()

    def _startTurn(self):
        self._player_hand.addCard(self._deck.pullCard())
        self._player_hand.addCard(self._deck.pullCard())
        self._dealer_hand.addCard(self._deck.pullCard())
        self._dealer_hand.addCard(self._deck.pullCard())

    def play(self):
        self._startTurn()
        while self._player_money > 0:
            os.system("cls")
            self._printOnTurn()
            if self._player_hand.getTotalValue() > 21:
                print("YOU LOOSE (score over 21)")
                self._player_money -= self._current_bet
                input("press enter")
                self._cardsReset()
                self._startTurn()
                continue

            user_input = self._getPlayerInput()

            if user_input == 1:
                self._player_hand.addCard(self._deck.pullCard())
            if user_input == 2:
                player_score = self._player_hand.getTotalValue()
                dealer_score = self._dealer_hand.getTotalValue()
                if player_score > dealer_score:
                    self._moneyResult(1)
                    self._printOnEnd()
                    print("You won!")
                    input("press enter...")
                    self._cardsReset()
                    self._startTurn()
                    continue
                elif player_score < dealer_score:
                    self._moneyResult(-1)
                    self._printOnEnd()
                    print("You loose!")
                    input("press enter...")
                    self._cardsReset()
                    self._startTurn()
                    continue
                else:
                    self._moneyResult(0)
                    self._printOnEnd()
                    print("You tie!")
                    input("press enter...")
                    self._cardsReset()
                    self._startTurn()
                    continue

            if user_input == 3:
                newbet = self._current_bet + self._bet_increase
                if newbet <= self._player_money:
                    self._current_bet = newbet
            if user_input == 0:
                print("bye!")
                return


# deck = Deck()
# deck.addCard(Card(f"♣ King of clubs", 10))
# deck.addCard(Card(f"♦ King of diamonds", 10))
# deck.addCard(Card(f"♥ King of hearts", 10))
# deck.addCard(Card(f"♠ King of spades", 10))

# hand = Hand()
# hand.addCard(deck.pullCard())
# hand.addCard(deck.pullCard())

# print(len(hand))
# print("Your cards: ")
# for card in hand:
#     print(f"    {card.value}\t| {card.name}")

game = BlackJack()
game.play()
