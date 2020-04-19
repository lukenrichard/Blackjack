import random
from Player import Player
from Dealer import Dealer
from VisitingTourist import VisitingTourist
from CardLettersToNumbers import cardLettersToNumbers
from CardNumbersToLetters import cardNumbersToLetters

# blackjackCheck method does not belong to a class, checks to see if either the VisitingTourist's score or the Dealer's score is 21 from their first two cards. Give a
# message to the User if so.


def blackjackCheck(touristScore, dealerScore):

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


def bustCheck(player, playerScore):
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


def stand(playerScore, dealerScore):

    # If the VisitingTourist's score is higher than the Dealer's, the User is notified that they won their hand.
    if (playerScore > dealerScore):
        print("You win! Your score is higher than the dealer's!\n")

    # If the VisitingTourist's score is lower than the Dealer's, the User is notified that they lost their hand.
    if (playerScore < dealerScore):
        print("The dealer won, their score was higher than yours.\n")

    # If the VisitingTourist's score is equal to the Dealer's, the User is notified that they pushed their hand.
    if (playerScore == dealerScore):
        print("You pushed. Your score was the same as the dealer's.\n")

# playGame method runs the game. It makes sure that all of the above functions are running in correct order and also gives
# the User their choices of what they would like to do throughout the game.


def playGame():

    print("\n---------------------")
    print("Blackjack!")
    print("---------------------\n")

    # Initialize Dealer and VisitingTourist Objects, then shuffle the deck.
    dealer = Dealer()
    visitingTourist = VisitingTourist()
    dealer.deckShuffle(dealer.deck)

    # The Dealer and the VisitingTourist both get their cards, and then their total scores are calculated. The User is notified of their cards, score,
    # and the Dealer's face up card.
    dealer.getCards(dealer.playerHand, dealer.deck)
    visitingTourist.getCards(visitingTourist.playerHand, dealer.deck)
    dealer.calculateScore(dealer.playerHand)
    visitingTourist.calculateScore(visitingTourist.playerHand)

    print("Your Hand is " + str(visitingTourist.playerHand) +
          " for a total of " + str(visitingTourist.playerScore) + ".\n")
    print("The Dealer is showing a " + str(dealer.playerHand[1]) + ".\n")

    # The program checks if the VisitingTourist or Dealer has a Blackjack with their original cards. If not, the game continues.
    check = blackjackCheck(visitingTourist.playerScore, dealer.playerScore)

    while(check == 0):

        # The program asks the User what they would like to do with their first hand after splitting. This message is only activated after splitting.
        if (visitingTourist.splitCount == 1):
            userInput = input(
                "Would you like to [h]it, [sp]lit, or [s]tand with your " + str(visitingTourist.firstHand) + "?\n")

        # The program asks the User what they would like to do with their second hand after splitting. This message is only activated after splitting
        # and finishing the firstHand.
        elif (visitingTourist.splitCount == 2):
            userInput = input(
                "Would you like to [h]it, [sp]lit, or [s]tand with your " + str(visitingTourist.secondHand) + "?\n")

        # The program asks the User what they would like to do with their hand.
        else:
            userInput = input(
                "Would you like to [h]it, [sp]lit, or [s]tand?\n")

        # If the User chooses to hit their hand, call the hit method.
        if userInput == 'h':

            # Set the original hand to the current hand.
            currentHand = visitingTourist.playerHand

            # If the User chose to split, set firstHand as the current hand.
            if (visitingTourist.splitCount == 1):
                currentHand = visitingTourist.firstHand

            # If the User chose to split, set secondHand as the current hand.
            if (visitingTourist.splitCount == 2):
                currentHand = visitingTourist.secondHand

            # Call hit method on current User hand and calculate/display score. Send User a bust message if their score after hitting exceeds 21.
            visitingTourist.hit(currentHand, dealer.deck)
            userScore = visitingTourist.calculateScore(currentHand)
            if (bustCheck(visitingTourist, userScore) == 1):
                break

        # If the User chooses to stand with their hand, call the stand method. Call the splitStand method if the User chose to split their original hand.
        elif userInput == 's':

            # If standing with the User's firstHand, flag and move onto secondHand in while loop.
            if (visitingTourist.splitCount == 1):

                # Flag that firstHand is done, splitCount now equals 2.
                visitingTourist.splitCount += 1
                continue

            # If standing with the User's secondHand, Dealer does their turn. After Dealer turn, display messages to player about final results.
            if (visitingTourist.splitCount == 2):

                # Allow Dealer to do their turn, then store their final score.
                dealerScore = dealer.dealerTurn(dealer.playerHand, dealer.deck)

                # Send scores of VisitingTourist's hands and Dealer hand into splitStand. Send User to playGame menu.
                visitingTourist.splitStand(visitingTourist.calculateScore(
                    visitingTourist.firstHand), visitingTourist.calculateScore(visitingTourist.secondHand), dealerScore)
                break

            # If User did not split, allow Dealer to have turn and then send scores to stand method. Send User to playGame menu.
            if (visitingTourist.splitCount == 0):
                userScore = visitingTourist.calculateScore(
                    visitingTourist.playerHand)
                dealerScore = dealer.dealerTurn(dealer.playerHand, dealer.deck)
                stand(visitingTourist.calculateScore(visitingTourist.playerHand),
                      dealer.calculateScore(dealer.playerHand))
                break

        # If User chooses to split with their hand, call the split method.
        elif userInput == 'sp':

            # If the cards in the User's hand do not match, they are not allowed to split.
            if (visitingTourist.playerHand[0] != visitingTourist.playerHand[1]):
                print("You cannot split with two cards that don't match!\n")

            # If the User has already chosen to split, they cannot split again.
            elif (visitingTourist.splitCount == 1):
                print("You cannot split more than once!\n")

            # Send current hand to split method. Flag that split has occured then display cards and scores of two new hands.
            else:
                firstHand, secondHand = visitingTourist.split(
                    visitingTourist.playerHand, dealer.deck)
                visitingTourist.splitCount += 1
                print("Your First Hand is " + str(firstHand) +
                      " for a total of " + str(visitingTourist.calculateScore(firstHand)) + ".\n")
                print("Your Second Hand is " + str(secondHand) +
                      " for a total of " + str(visitingTourist.calculateScore(secondHand)) + ".\n")

        # If User input is not recognized, send message to try again.
        else:
            print("Previous command not recognized, try again!")

    # Current game has ended, ask User if they would like to play again.
    userInput = input("Would you like to play again, [y]es or [n]o?\n")
    if userInput == 'y':
        playGame()
    else:
        exit()


# Start game on start of program.
if __name__ == '__main__':

    playGame()
