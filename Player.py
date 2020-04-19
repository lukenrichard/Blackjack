from CardLettersToNumbers import cardLettersToNumbers
from CardNumbersToLetters import cardNumbersToLetters

# Player class is used for both VisitingTourist and Dealer classes, includes all basic methods and attributes needed for the Blackjack game.


class Player:

    # Initialize any Player object with an empty array for their hand and a starting score of 0.
    def __init__(self):

        self.playerHand = []
        self.playerScore = 0

    # getCards method is used to add cards to the Player's hand in the case of a split.
    def getCards(self, playerHand, deck):

        # Pop a card off of the deck from the Dealer object, then add it to the Player's hand.
        for i in range(2):
            temp = deck.pop()
            if temp in cardNumbersToLetters:
                card = cardNumbersToLetters.get(temp)
                playerHand.append(card)
            else:
                playerHand.append(temp)

    # calculateScore method is used to go through the Player's hand and total up the numberical values of each card.
    def calculateScore(self, playerHand):

        # Player starts with a score of 0.
        total = 0

        # For every card in the Player's hand, get the numberical value (if face card) and add it to the running total, then return that total.
        for i in range(len(playerHand)):
            temp = playerHand[i]
            if temp in cardLettersToNumbers:
                val = cardLettersToNumbers.get(temp)
            else:
                val = temp

            total += val

        # If the Player has an A in their hand and their score is above 10, remove 10 off of their score.
        if 'A' in playerHand:
            if total <= 10:
                total += 10

        self.playerScore = total
        return self.playerScore

    # hit method is used to add a card to the Player's hand and send a message to the player that they did so.
    def hit(self, playerHand, deck):

        # Pop a card off of the deck from the Dealer obejct and add it to the Player's hand.
        temp = deck.pop()
        if temp in cardNumbersToLetters:
            card = cardNumbersToLetters.get(temp)
        else:
            card = temp
        playerHand.append(card)

        # Print message to User saying which card was added to their hand and the new score of their hand.
        print("The " + type(self).__name__ + " hit and got a " +
              str(card) + " for a total of " + str(self.calculateScore(playerHand)) + ".\n")
