import random
from Player import Player
from Dealer import Dealer
from VisitingTourist import VisitingTourist
from CheckMethods import CheckMethods
from CardLettersToNumbers import cardLettersToNumbers
from CardNumbersToLetters import cardNumbersToLetters


# playGame method runs the game. It makes sure that all of the above functions are running in correct order and also gives
# the User their choices of what they would like to do throughout the game.


def playGame():

    # The deck array represents the cards used for the game.

    deck = [1, 13] * 4

    print("\n---------------------")
    print("Blackjack!")
    print("---------------------\n")

    # Initialize Dealer and VisitingTourist Objects, then shuffle the deck.
    dealer = Dealer()
    visitingTourist = VisitingTourist()
    dealer.deckShuffle(deck)
    checkMethods = CheckMethods()

    # The Dealer and the VisitingTourist both get their cards, and then their total scores are calculated. The User is notified of their cards, score,
    # and the Dealer's face up card.
    dealer._getCards(dealer._playerHand, deck)
    visitingTourist._getCards(visitingTourist._playerHand, deck)
    dealer._calculateScore(dealer._playerHand)
    visitingTourist._calculateScore(visitingTourist._playerHand)

    print("Your Hand is " + str(visitingTourist._playerHand) +
          " for a total of " + str(visitingTourist._playerScore) + ".\n")
    print("The Dealer is showing a " + str(dealer._playerHand[1]) + ".\n")

    # The program checks if the VisitingTourist or Dealer has a Blackjack with their original cards. If not, the game continues.
    check = checkMethods.blackjackCheck(
        visitingTourist._playerScore, dealer._playerScore)

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
            currentHand = visitingTourist._playerHand

            # If the User chose to split, set firstHand as the current hand.
            if (visitingTourist.splitCount == 1):
                currentHand = visitingTourist.firstHand

            # If the User chose to split, set secondHand as the current hand.
            if (visitingTourist.splitCount == 2):
                currentHand = visitingTourist.secondHand

            # Call hit method on current User hand and calculate/display score. Send User a bust message if their score after hitting exceeds 21.
            visitingTourist._hit(currentHand, deck)
            userScore = visitingTourist._calculateScore(currentHand)
            if (checkMethods.bustCheck(visitingTourist, userScore) == 1):
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
                dealerScore = dealer.dealerTurn(dealer._playerHand, deck)

                # Send scores of VisitingTourist's hands and Dealer hand into splitStand. Send User to playGame menu.
                visitingTourist.splitStand(visitingTourist._calculateScore(
                    visitingTourist.firstHand), visitingTourist._calculateScore(visitingTourist.secondHand), dealerScore)
                break

            # If User did not split, allow Dealer to have turn and then send scores to stand method. Send User to playGame menu.
            if (visitingTourist.splitCount == 0):
                userScore = visitingTourist._calculateScore(
                    visitingTourist._playerHand)
                dealerScore = dealer.dealerTurn(dealer._playerHand, deck)
                checkMethods.stand(visitingTourist._calculateScore(visitingTourist._playerHand),
                                   dealer._calculateScore(dealer._playerHand))
                break

        # If User chooses to split with their hand, call the split method.
        elif userInput == 'sp':

            # If the cards in the User's hand do not match, they are not allowed to split.
            if (visitingTourist._playerHand[0] != visitingTourist._playerHand[1]):
                print("You cannot split with two cards that don't match!\n")

            # If the User has already chosen to split, they cannot split again.
            elif (visitingTourist.splitCount == 1):
                print("You cannot split more than once!\n")

            # Send current hand to split method. Flag that split has occured then display cards and scores of two new hands.
            else:
                firstHand, secondHand = visitingTourist.split(
                    visitingTourist._playerHand, deck)
                visitingTourist.splitCount += 1
                print("Your First Hand is " + str(firstHand) +
                      " for a total of " + str(visitingTourist._calculateScore(firstHand)) + ".\n")
                print("Your Second Hand is " + str(secondHand) +
                      " for a total of " + str(visitingTourist._calculateScore(secondHand)) + ".\n")

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
