import random
from Player import Player
from CardLettersToNumbers import cardLettersToNumbers
from CardNumbersToLetters import cardNumbersToLetters

# Dealer class inherits everything from the Player class, however has to add a deck attribute when initialized.


class Dealer(Player):

    def __init__(self):
        Player.__init__(self)

    # deckShuffle method shuffles the deck before the game starts.
    def deckShuffle(self, deck):
        return random.shuffle(deck)

    # dealerTurn method automates the Dealer's turn once the player is done with their hand/hands.
    def dealerTurn(self, playerHand, deck):

        # Retrieve score of Dealer's hand then send message to player of the score of Dealer's dealt hand.
        playerScore = self._calculateScore(playerHand)
        print("\nThe dealer reveals their face down card to be " +
              str(playerHand[0]) + ", for a total of " + str(playerScore) + ".\n")

        # If the Dealer's score is under 17, the dealer needs to continue to hit until they have a score of 17 or higher.
        while (playerScore <= 16):
            self._hit(playerHand, deck)
            playerScore = self._calculateScore(playerHand)

        # When the Dealer stops hitting, if the score of their hand is over 21, then the dealer busted and the player is notified.
        if (playerScore >= 22):
            print("The dealer busted! You win!\n")

        # The dealer did not bust, and the dealer's final score is returned.
        else:
            return playerScore
