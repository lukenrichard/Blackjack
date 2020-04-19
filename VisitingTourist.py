from Player import Player
from CardLettersToNumbers import cardLettersToNumbers
from CardNumbersToLetters import cardNumbersToLetters

# VisitingTourist class is the Object that represents the User, this class inherits from the Player class.


class VisitingTourist(Player):

    # The VisitingTourist Object is the only one that can split hands, so initialize with additional empty arrays to do so if needed.
    def __init__(self):
        Player.__init__(self)
        self.firstHand = []
        self.secondHand = []
        self.splitCount = 0

    # addCard method adds a card to the VisitingTourist's hand in the case that they split, because they are not hitting.
    def addCard(self, playerHand, deck):

        # Pop a card from the Dealer's deck, then add to the VisitingTourist's hand.
        temp = deck.pop()
        if temp in cardNumbersToLetters:
            card = cardNumbersToLetters.get(temp)
        else:
            card = temp
        playerHand.append(card)

    # split method allows the VisitingTourist to split their hand.
    def split(self, playerHand, deck):

        # Store first card into the firstHand attribute and the second card into the secondHand attribute. Then add a card to each of the hands to represent the two newly
        # made hands from splitting the first two cards dealt. Return the two hands.
        self.firstHand = playerHand[0]
        self.secondHand = playerHand[1]
        VisitingTourist.addCard(VisitingTourist, self.firstHand, deck)
        VisitingTourist.addCard(VisitingTourist, self.secondHand, deck)
        return self.firstHand, self.secondHand

    # splitStand method deals with the many different print statements sent to the User when they split their hand.
    def splitStand(self, firstScore, secondScore, dealerScore):

        # If the firstHand's score is higher than the Dealer's hand, the User is notified they won their firstHand.
        if (firstScore > dealerScore and firstScore <= 21):
            print("You win your First Hand! Your score is higher than the dealer's!\n")

        # If the firstHand's score is lower, the User is notified that they lost their firstHand.
        if (firstScore < dealerScore):
            print("The dealer beat your First Hand, their score was higher than yours.\n")

        # If the firstHand's score is equal to the Dealer's hand, the User is notified that they pushed their firstHand.
        if (firstScore == dealerScore):
            print("You pushed your First Hand. The score was the same as the dealer's.\n")

        # The same statements above are repeated for the secondHand, giving the User two seperate messages about each of their hands after splitting.
        if (secondScore > dealerScore and secondScore <= 21):
            print("You win your Second Hand! Your score is higher than the dealer's!\n")

        if (secondScore < dealerScore):
            print(
                "The dealer beat your Second Hand, their score was higher than yours.\n")

        if (secondScore == dealerScore):
            print(
                "You pushed your Second Hand. The score was the same as the dealer's.\n")
