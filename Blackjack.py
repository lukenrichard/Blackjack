import random

cardValues = {
    1: 'A',
    11: 'J',
    12: 'Q',
    13: 'K',
    'J': 10,
    'Q': 10,
    'K': 10,
    'A': 1
}


class Player:

    def __init__(self):

        self.playerHand = []
        self.playerScore = 0

    def getCards(self, playerHand, deck):

        for i in range(2):
            temp = deck.pop()
            if temp in cardValues:
                card = cardValues.get(temp)
                playerHand.append(card)
            else:
                playerHand.append(temp)

    def getScore(self, playerHand):

        # Set total to 0, go through each card in hand and convert to number value. Then add number value to running total score.
        total = 0

        for i in range(len(playerHand)):
            temp = playerHand[i]
            if temp in cardValues:
                val = cardValues.get(temp)
            else:
                val = temp

            total += val

        if 'A' in playerHand:
            if total <= 10:
                total += 10

        self.playerScore = total
        return self.playerScore

    def hit(self, playerHand, deck):

        # Take the next number value from the deck, convert it to a J, Q, K, or A, if applicable, then add to the dealer's hand.
        temp = deck.pop()
        if temp in cardValues:
            card = cardValues.get(temp)
        else:
            card = temp
        playerHand.append(card)

        # Print message to player displaying the card the dealer added to their hand and their total current score.
        print("The " + type(self).__name__ + " hit and got a " +
              str(card) + " for a total of " + str(Player.getScore(Player, playerHand)) + ".\n")


class Dealer(Player):

    deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] * 4

    def deckShuffle(self, deck):
        return random.shuffle(Dealer.deck)

    def dealerTurn(self, playerHand, deck):
        # Retrieve score of dealer's hand then send message to player of the score of dealer's original hand.
        playerScore = Player.getScore(Dealer, playerHand)
        print("\nThe dealer reveals their face down card to be " +
              str(playerHand[0]) + ", for a total of " + str(playerScore) + ".\n")

        # If the dealer's score is under 17, the dealer needs to continue to hit until they have a score of 17 or higher.
        while (playerScore <= 16):
            self.hit(playerHand, deck)
            playerScore = Player.getScore(Dealer, playerHand)

        # When the dealer stops hitting, if the score of their hand is over 21, then the dealer busted and the player is notified.
        if (playerScore >= 22):
            print("The dealer busted! You win!\n")

            # If the deaSler busts, the current game is over and the player is offered to play again.
            # playAgain()

        # The dealer did not bust, and the dealer's final score is returned.
        else:
            return playerScore


class VisitingTourist(Player):

    def __init__(self):

        self.playerHand = []
        self.playerScore = 0
        self.firstHand = []
        self.secondHand = []
        self.splitCount = 0

    def addCard(self, playerHand, deck):
        # Take the next number value from the deck, convert it to a J, Q, K, or A, if applicable, then add to the desired hand.
        temp = deck.pop()
        if temp in cardValues:
            card = cardValues.get(temp)
        else:
            card = temp
        playerHand.append(card)

    def split(self, playerHand, deck):
        # Store the first and second card in the player's hand
        temp = playerHand[0]
        temp1 = playerHand[1]

        # Create two hands, one with each card and then add a supplementary card to each hand for a total of 2 cards per hand. Return hands.
        self.firstHand = [temp]
        self.secondHand = [temp1]
        VisitingTourist.addCard(VisitingTourist, self.firstHand, deck)
        VisitingTourist.addCard(VisitingTourist, self.secondHand, deck)
        return self.firstHand, self.secondHand

    def splitStand(self, firstScore, secondScore, dealerScore):

        # If the first hand's score is higher than the dealer's hand, the player is notified they won their first hand.
        if (firstScore > dealerScore and firstScore <= 21):
            print("You win your First Hand! Your score is higher than the dealer's!\n")

        # If the first hand's score is lower, the player is notified that they lost their first hand.
        if (firstScore < dealerScore):
            print("The dealer beat your First Hand, their score was higher than yours.\n")

        # If the first hand's score is equal to the dealer's hand, the player is notified that they pushed their hand.
        if (firstScore == dealerScore):
            print("You pushed your First Hand. The score was the same as the dealer's.\n")

        # The same statements above are repeated for the second hand, giving the player two seperate messages about their hands after splitting.
        if (secondScore > dealerScore and secondScore <= 21):
            print("You win your Second Hand! Your score is higher than the dealer's!\n")

        if (secondScore < dealerScore):
            print(
                "The dealer beat your Second Hand, their score was higher than yours.\n")

        if (secondScore == dealerScore):
            print(
                "You pushed your Second Hand. The score was the same as the dealer's.\n")


def blackjackCheck(touristScore, dealerScore):

    # If both the dealer and the player have 21 with their two opening cards, they push.
    if (touristScore == 21 and dealerScore == 21):
        print("You and the dealer were both dealt Blackjack! You push.\n")
        return 1

    # If the player's score is 21 with their two opening cards, they win.
    elif (touristScore == 21):
        print("You were dealt a Blackjack! You win!\n")
        return 1

    # If the dealer's score is 21 with their two opening cards, they win.
    elif (dealerScore == 21):
        print("The dealer was dealt a Blackjack. You lose.\n")
        return 1

    # No player's were dealt Blackjack, so this will return 0 and will not send a flag to end the current game.
    else:
        return 0


def stand(myScore, dealerScore):

    # If the player's score is higher than the dealer's, the player is notified that they won their hand.
    if (myScore > dealerScore):
        print("You win! Your score is higher than the dealer's!\n")

    # If the player's score is lower than the dealer's, the player is notified that they lost their hand.
    if (myScore < dealerScore):
        print("The dealer won, their score was higher than yours.\n")

    # If the player's score is equal to the dealer's, the player is notified that they pushed their hand.
    if (myScore == dealerScore):
        print("You pushed. Your score was the same as the dealer's.\n")

# This function runs the game. It makes sure that all of the above functions are running in correct order and also gives
# the player their choices of what they would like to do throughout the game.


def playGame():

    print("\n---------------------")
    print("Blackjack!")
    print("---------------------\n")

    dealer = Dealer()
    visitingTourist = VisitingTourist()
    dealer.deckShuffle(dealer.deck)

    # The dealer and the player both get their cards, and then their total scores are calculated. The player is notified of their cards, score,
    # and the dealer's face up card.
    dealer.getCards(dealer.playerHand, dealer.deck)
    visitingTourist.getCards(visitingTourist.playerHand, dealer.deck)

    dealer.getScore(dealer.playerHand)
    visitingTourist.getScore(visitingTourist.playerHand)

    print("Your Hand is " + str(visitingTourist.playerHand) +
          " for a total of " + str(visitingTourist.playerScore) + ".\n")
    print("The Dealer is showing a " + str(dealer.playerHand[1]) + ".\n")

    # The program checks if the player or dealer has a Blackjack with their original cards. If not, the game continues.
    check = blackjackCheck(visitingTourist.playerScore, dealer.playerScore)

    while(check == 0):

        # The program asks the player what they would like to do with their first hand after splitting. This message is only activated after splitting.
        if (visitingTourist.splitCount == 1):
            temp = input(
                "Would you like to [h]it, [sp]lit, or [s]tand with your " + str(visitingTourist.firstHand) + "?\n")

        # The program asks the player what they would like to do with their second hand after splitting. This message is only activated after splitting
        # and finishing the first hand.
        elif (visitingTourist.splitCount == 2):
            temp = input(
                "Would you like to [h]it, [sp]lit, or [s]tand with your " + str(visitingTourist.secondHand) + "?\n")

        # The program asks the player what they would like to do with their hand.
        else:
            temp = input("Would you like to [h]it, [sp]lit, or [s]tand?\n")

        # If the player chooses to hit their hand, use the hit function.
        if temp == 'h':

            currentHand = visitingTourist.playerHand

            # If the player chose to split, set first hand as the current hand.
            if (visitingTourist.splitCount == 1):
                currentHand = visitingTourist.firstHand

            # If the player chose to split, set second hand as the current hand.
            if (visitingTourist.splitCount == 2):
                currentHand = visitingTourist.secondHand

            # Use hit function on current player hand and calculate/display score. Send player a bust message if their score after hitting exceeds 21.
            visitingTourist.hit(currentHand, dealer.deck)
            myScore = visitingTourist.getScore(currentHand)
            if (myScore >= 22):
                if (visitingTourist.splitCount == 1):
                    print("Oops! It looks like you busted your first hand.\n")
                    continue
                if (visitingTourist.splitCount == 2):
                    print("Oops! It looks like you busted your second hand.\n")
                    break
                else:
                    print("Oops! It looks like you busted.\n")
                    break
            else:
                print("Your total is now " + str(myScore) + ".\n")

        # If the player chooses to stand with their hand, use the stand function. Use the splitStand function if the player chose to split their original hand.
        elif temp == 's':

            # If standing with the player's first hand, flag and move onto second hand in while loop.
            if (visitingTourist.splitCount == 1):

                # Flag that first hand is done, splitCount now equals 2.
                visitingTourist.splitCount += 1
                continue

            # If standing with the player's second hand, dealer does their turn. After dealer turn, display messages to player about final results.
            if (visitingTourist.splitCount == 2):

                # Allow dealer to do their turn, then store their final score.
                dealerScore = dealer.dealerTurn(dealer.playerHand, dealer.deck)

                # Send scores of player hands and dealer hand into splitStand. Send player to playAgain menu.
                visitingTourist.splitStand(visitingTourist.getScore(
                    visitingTourist.firstHand), visitingTourist.getScore(visitingTourist.secondHand), dealerScore)
                break

            # If player did not split, allow dealer to have turn and then send scores to stand method. Send player to playAgain menu.
            if (visitingTourist.splitCount == 0):
                myScore = visitingTourist.getScore(visitingTourist.playerHand)
                dealerScore = dealer.dealerTurn(dealer.playerHand, dealer.deck)
                stand(visitingTourist.getScore(visitingTourist.playerHand),
                      dealer.getScore(dealer.playerHand))
                break

        # If player chooses to split with their hand, use the split function.
        elif temp == 'sp':

            # If the cards in the player's hand do not match, they are not allowed to split.
            if (visitingTourist.playerHand[0] != visitingTourist.playerHand[1]):
                print("You cannot split with two cards that don't match!\n")

            # If the player has already chosen to split, they cannot split again.
            elif (visitingTourist.splitCount == 1):
                print("You cannot split more than once!\n")

            # Send current hand to split method. Flag that split has occured then display cards and scores of two new hands.
            else:
                firstHand, secondHand = visitingTourist.split(
                    visitingTourist.playerHand, dealer.deck)
                visitingTourist.splitCount += 1
                print("Your First Hand is " + str(firstHand) +
                      " for a total of " + str(visitingTourist.getScore(firstHand)) + ".\n")
                print("Your Second Hand is " + str(secondHand) +
                      " for a total of " + str(visitingTourist.getScore(secondHand)) + ".\n")

        # If player input is not recognized, send message to try again.
        else:
            print("Previous command not recognized, try again!")

    # Current game has ended, ask player if they would like to play again.
    temp = input("Would you like to play again, [y]es or [n]o?\n")
    if temp == 'y':
        playGame()
    else:
        exit()


if __name__ == '__main__':

    playGame()
