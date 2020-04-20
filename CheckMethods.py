# CheckMethods is a helper class used to hold methods used for playGame() function that do not belong to any of the Objects being used.


class CheckMethods:

    # blackjackCheck method does not belong to a class, checks to see if either the VisitingTourist's score or the Dealer's score is 21 from their first two cards. Give a
    # message to the User if so.

    def blackjackCheck(self, touristScore, dealerScore):

        # If both the Dealer and the VisitingTourist have 21 with their two opening cards, they push.
        if (touristScore == 21 and dealerScore == 21):
            print("You and the dealer were both dealt Blackjack! You push.\n")
            return 1

        # If the VisitingTourists's score is 21 with their two opening cards, they win.
        elif (touristScore == 21):
            print("You were dealt a Blackjack! You win!\n")
            return 1

        # If the Dealer's score is 21 with their two opening cards, they win.
        elif (dealerScore == 21):
            print("The dealer was dealt a Blackjack. You lose.\n")
            return 1

        # No Players were dealt Blackjack, so this will return 0 and will not send a flag to end the current game.
        else:
            return 0

    # bustCheck method evaluates the score of the VisitingTourist after a hit and alerts the User if they have busted.

    def bustCheck(self, player, playerScore):
        if (playerScore >= 22):
            if (player.splitCount == 1):
                print("Oops! It looks like you busted your first hand.\n")
                return 1
            if (player.splitCount == 2):
                print("Oops! It looks like you busted your second hand.\n")
                return 1
            else:
                print("Oops! It looks like you busted.\n")
                return 1
        else:
            print("Your total is now " + str(playerScore) + ".\n")

    # stand method evaluates the score of the VisitingTourist after he has chosen to stand and the Dealer to see which has won or if there is a push.

    def stand(self, playerScore, dealerScore):

        # If the VisitingTourist's score is higher than the Dealer's, the User is notified that they won their hand.
        if (playerScore > dealerScore):
            print("You win! Your score is higher than the dealer's!\n")

        # If the VisitingTourist's score is lower than the Dealer's, the User is notified that they lost their hand.
        if (playerScore < dealerScore):
            print("The dealer won, their score was higher than yours.\n")

        # If the VisitingTourist's score is equal to the Dealer's, the User is notified that they pushed their hand.
        if (playerScore == dealerScore):
            print("You pushed. Your score was the same as the dealer's.\n")
