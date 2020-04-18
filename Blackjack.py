import random

# Dictionary for Card Letters and Number Values
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
            if temp in cardValues:
                card = cardValues.get(temp)
                playerHand.append(card)
            else:
                playerHand.append(temp)

    # getScore method is used to go through the Player's hand and total up the numberical values of each card.
    def getScore(self, playerHand):

        # Player starts with a score of 0.
        total = 0

        # For every card in the Player's hand, get the numberical value (if face card) and add it to the running total, then return that total.
        for i in range(len(playerHand)):
            temp = playerHand[i]
            if temp in cardValues:
                val = cardValues.get(temp)
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
        if temp in cardValues:
            card = cardValues.get(temp)
        else:
            card = temp
        playerHand.append(card)

        # Print message to User saying which card was added to their hand and the new score of their hand.
        print("The " + type(self).__name__ + " hit and got a " +
              str(card) + " for a total of " + str(Player.getScore(Player, playerHand)) + ".\n")


# Dealer class inherits everything from the Player class, however has to add a deck attribute when initialized.
class Dealer(Player):

    def __init__(self):
        self.playerHand = []
        self.playerScore = 0
        self.deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] * 4

    # deckShuffle method shuffles the deck before the game starts.
    def deckShuffle(self, deck):
        return random.shuffle(self.deck)

    # dealerTurn method automates the Dealer's turn once the player is done with their hand/hands.
    def dealerTurn(self, playerHand, deck):

        # Retrieve score of Dealer's hand then send message to player of the score of Dealer's dealt hand.
        playerScore = Player.getScore(Dealer, playerHand)
        print("\nThe dealer reveals their face down card to be " +
              str(playerHand[0]) + ", for a total of " + str(playerScore) + ".\n")

        # If the Dealer's score is under 17, the dealer needs to continue to hit until they have a score of 17 or higher.
        while (playerScore <= 16):
            self.hit(playerHand, deck)
            playerScore = Player.getScore(Dealer, playerHand)

        # When the Dealer stops hitting, if the score of their hand is over 21, then the dealer busted and the player is notified.
        if (playerScore >= 22):
            print("The dealer busted! You win!\n")

        # The dealer did not bust, and the dealer's final score is returned.
        else:
            return playerScore

# VisitingTourist class is the Object that represents the User, this class inherits from the Player class.


class VisitingTourist(Player):

    # The VisitingTourist Object is the only one that can split hands, so initialize with additional empty arrays to do so if needed.
    def __init__(self):
        self.playerHand = []
        self.playerScore = 0
        self.firstHand = []
        self.secondHand = []
        self.splitCount = 0

    # addCard method adds a card to the VisitingTourist's hand in the case that they split, because they are not hitting.
    def addCard(self, playerHand, deck):

        # Pop a card from the Dealer's deck, then add to the VisitingTourist's hand.
        temp = deck.pop()
        if temp in cardValues:
            card = cardValues.get(temp)
        else:
            card = temp
        playerHand.append(card)

    # split method allows the VisitingTourist to split their hand.
    def split(self, playerHand, deck):

        # Store the first and second card in the VisitingTourist's hand
        temp = playerHand[0]
        temp1 = playerHand[1]

        # Store first card into the firstHand attribute and the second card into the secondHand attribute. Then add a card to each of the hands to represent the two newly
        # made hands from splitting the first two cards dealt. Return the two hands.
        self.firstHand = [temp]
        self.secondHand = [temp1]
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

# stand method evaluates the score of the VisitingTourist and the Dealer to see which has won or if there is a push.


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
    dealer.getScore(dealer.playerHand)
    visitingTourist.getScore(visitingTourist.playerHand)

    print("Your Hand is " + str(visitingTourist.playerHand) +
          " for a total of " + str(visitingTourist.playerScore) + ".\n")
    print("The Dealer is showing a " + str(dealer.playerHand[1]) + ".\n")

    # The program checks if the VisitingTourist or Dealer has a Blackjack with their original cards. If not, the game continues.
    check = blackjackCheck(visitingTourist.playerScore, dealer.playerScore)

    while(check == 0):

        # The program asks the User what they would like to do with their first hand after splitting. This message is only activated after splitting.
        if (visitingTourist.splitCount == 1):
            temp = input(
                "Would you like to [h]it, [sp]lit, or [s]tand with your " + str(visitingTourist.firstHand) + "?\n")

        # The program asks the User what they would like to do with their second hand after splitting. This message is only activated after splitting
        # and finishing the firstHand.
        elif (visitingTourist.splitCount == 2):
            temp = input(
                "Would you like to [h]it, [sp]lit, or [s]tand with your " + str(visitingTourist.secondHand) + "?\n")

        # The program asks the User what they would like to do with their hand.
        else:
            temp = input("Would you like to [h]it, [sp]lit, or [s]tand?\n")

        # If the User chooses to hit their hand, call the hit method.
        if temp == 'h':

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

        # If the User chooses to stand with their hand, call the stand method. Call the splitStand method if the User chose to split their original hand.
        elif temp == 's':

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
                visitingTourist.splitStand(visitingTourist.getScore(
                    visitingTourist.firstHand), visitingTourist.getScore(visitingTourist.secondHand), dealerScore)
                break

            # If User did not split, allow Dealer to have turn and then send scores to stand method. Send User to playGame menu.
            if (visitingTourist.splitCount == 0):
                myScore = visitingTourist.getScore(visitingTourist.playerHand)
                dealerScore = dealer.dealerTurn(dealer.playerHand, dealer.deck)
                stand(visitingTourist.getScore(visitingTourist.playerHand),
                      dealer.getScore(dealer.playerHand))
                break

        # If User chooses to split with their hand, call the split method.
        elif temp == 'sp':

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
                      " for a total of " + str(visitingTourist.getScore(firstHand)) + ".\n")
                print("Your Second Hand is " + str(secondHand) +
                      " for a total of " + str(visitingTourist.getScore(secondHand)) + ".\n")

        # If User input is not recognized, send message to try again.
        else:
            print("Previous command not recognized, try again!")

    # Current game has ended, ask User if they would like to play again.
    temp = input("Would you like to play again, [y]es or [n]o?\n")
    if temp == 'y':
        playGame()
    else:
        exit()


# Start game on start of program.
if __name__ == '__main__':

    playGame()
