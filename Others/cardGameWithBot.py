# Student Number : 270201050
import random

class Gamebot:

    def __init__(self, play_hand, stack):
        self.play_hand = play_hand                  # a reference to the player's hand
        self.stack = stack                          # a reference to the stack
        self.count_deck = [['b',1],['b',1],['b',1],['b',2], # a list to count the remaining
                           ['b',2],['b',3],['b',3],['b',4], # cards in the deck
                           ['w',1],['w',1],['w',1],['w',2],
                           ['w',2],['w',3],['w',3],['w',4]]
        for card in play_hand:                      # bot has already seen the player's hand,so it knows
            self.update_count_deck(card)            # that those cards are not in the deck anymore.
        self.hand = [['!',-1],['!',-1],['!',-1]]    # bot's hand. '!' indicates unknown color,
                                                    # -1 indicates unknown value

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

    # This function allows the computer to update the unknowns in the list named self.hand according to the hint after the player gives a hint to the computer.

    def get_tip(self, tip):
        # input: tip: a string entered by the player in the form of "loc1,loc2*,loc3*,tip"
        # where * indicates optionality and tip is either a value or a color.
        # e.g. "1,2,w" or "2,3" or "1,2,3,2"
        # output: none
        # The tip is processed and the information about the bot's hand is updated.
        # tip = 1,2,3,w
        tip = tip.split(",")
        if tip[len(tip) - 1] == "w":
            for i in range(len(tip) - 1):
                self.hand[int(tip[i]) - 1][0] = "w"
            if len(self.hand) == 3:
                for i in range(len(self.hand)):
                    if self.hand[i][0] == "!":
                        self.hand[i][0] = "b"
                        break
        elif tip[len(tip) - 1] == "b":
            for i in range(len(tip) - 1):
                self.hand[int(tip[i]) - 1][0] = "b"
            if len(self.hand) == 3:
                for i in range(len(self.hand)):
                    if self.hand[i][0] == "!":
                        self.hand[i][0] = "w"
                        break
        else:
            for i in range(len(tip) - 1):
                self.hand[int(tip[i]) - 1][1] = int(tip[len(tip) - 1])

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

    # This function updates count_deck when computer or player draws a card from deck.
    def update_count_deck(self,card):
        # input: card to be removed
        # output: none
        # card is removed from the count_deck of the bot.
        self.count_deck.remove(card)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

    # This function when the computer takes out a card.It deletes the discarded card from self.hand and adds a new unknown card from the shuffled deck.
    # It applies the same operations to the computer hand. Updates only self.hand and comp_hand if no cards are in the deck.

    def update_hand(self,num):
        if not deck:
            self.hand.pop(num)
            comp_hand.pop(num)
        else:
            comp_hand.remove(comp_hand[num])
            comp_hand.append(deck[0])
            deck.remove(deck[0])
            self.hand.remove(self.hand[num])
            self.hand.append(['!',-1]) #An unknown card is added to self.hand

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    # This function controls the player's hand for both colors and numbers.
    # If it finds the same, it adds a number with more than 1 index of both to a list, and if there is more than 1 of the same number in the list,
    # It removes it from the list using the set method.
    # If the number of the same number is more or equal to the number of the same colors, it gives a hint containing the number.
    # Otherwise it gives a hint of containing colors.

    def give_tip(self):
        if len(play_hand) == 3:
            counter_color = ""
            counter_number = 0
            index_color = []
            index_number = []
            for i in range(len(play_hand)):
                for j in range(len(play_hand)):
                    if i < j:
                        if play_hand[i][1] == play_hand[j][1]:
                            index_number.append(i + 1)
                            index_number.append(j + 1)
                            counter_number = play_hand[i][1]

            for i in range(len(play_hand)):
                for j in range(len(play_hand)):
                    if i < j:
                        if play_hand[i][0] == play_hand[j][0]:
                            index_color.append(i + 1)
                            index_color.append(j + 1)
                            counter_color = play_hand[i][0]

            index_color = set(index_color)
            index_number = set(index_number)
            tip_text = "Tip: "

            if len(index_number) >= len(index_color):
                for i in index_number:
                    tip_text = tip_text + str(i) + ","
                print(tip_text + str(counter_number))
                return True
            else:
                for i in index_color:
                    tip_text = tip_text + str(i) + ","
                print(tip_text + counter_color)
                return True
        else:
            print("Tip: 1,{}".format(play_hand[0][1]))
            return True

#-------------------------------------------------------------------------------------------------------------------------------------------------------------

    # This function ensures that if there is no card in the stack and the computer knows that at least one of the cards in its hand is 1, that card is accumulated on the floor,
    # If there is a card on the floor, after knowing the card completely, if it can stack it on the stack.

    def pick_stack(self):
        # input: none
        # output: If possible, the location of the card to be placed in the stack, otherwise -1. Minimal
        # the requirement for this function is to find the card to be stacked with 100% certainty.
        # BONUS: Smarter decision-making algorithms can be implemented.
        for i in self.hand:
            if i[0] == "w":
                if len(stack[1]) != 0:
                    if i[1]  == stack[1][len(stack[1]) - 1][1] + 1:
                        num_ = self.hand.index(i)
                        stack[1].append(i)
                        print("Stack: ", stack)
                        bot.update_hand(num_)
                        return True
                else:
                    if i[1] == 1:
                        num_ = self.hand.index(i)
                        stack[1].append(i)
                        print("Stack: ", stack)
                        bot.update_hand(num_)
                        return True
            elif i[0] == "b":
                if len(stack[0]) != 0:
                    if i[1]  == stack[0][len(stack[0]) - 1][1] + 1:
                        num_ = self.hand.index(i)
                        stack[0].append(i)
                        print("Stack: ", stack)
                        bot.update_hand(num_)
                        return True
                else:
                    if i[1] == 1:
                        num_ = self.hand.index(i)
                        stack[0].append(i)
                        print("Stack: ", stack)
                        bot.update_hand(num_)
                        return True
            elif not stack[0] and not stack[1]:
                if i[1] == 1:
                    if comp_hand[self.hand.index(i)][0] == "w":
                        stack[1].append(comp_hand[self.hand.index(i)])
                        bot.update_hand(self.hand.index(i))
                        print("Stack: ", stack)
                        return True
                    else:
                        stack[0].append(comp_hand[self.hand.index(i)])
                        bot.update_hand(self.hand.index(i))
                        print("Stack: ", stack)
                        return True


#-----------------------------------------------------------------------------------------------------------------------------------------------------------

    # This function allows the computer to discard the card to trash.
    # If one of the cards, whose color and number is known, is in the stack.

    def pick_discard(self):
        # input: none
        # output: The location of the card to be discarded. Minimal requirement for this function is that,
        # if possible, the bot picks the card that is already in the stack. If this is not the case,
        # the bot picks the card of which it has minimum information.
        # BONUS: Smarter decision-making algorithms can be implemented.
        for i in self.hand:
            if i in stack[0] or i in stack[1]:
                if len(deck) > 0:
                    indx = self.hand.index(i)
                    bot.update_hand(indx)
                    deck.remove(deck[0])
                    trash.append(i)
                    trash.sort()
                    comp_hand.pop(indx)
                    comp_hand.append(deck[0])
                    print("Trash :", trash)
                    return True
                else:
                    indx = self.hand.index(i)
                    bot.update_hand(indx)
                    deck.remove(deck[0])
                    trash.append(i)
                    trash.sort()
                    comp_hand.pop(indx)
                    print("Trash :", trash)
                    return True
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            else:                                                           # This part checks the numbers of all cards in the stack.
                if len(deck) > 0:                                           # It will throw the card into the garbage if computer has that number on both sides of the stack, even if he does not know the color.
                    for j in range(len(stack[0])):
                        if i[1] == stack[0][j][1]:
                            for k in range(len(stack[1])):
                                if i[1] == stack[1][k][1]:
                                    indx = self.hand.index(i)
                                    bot.update_hand(indx)
                                    deck.remove(deck[0])
                                    trash.append(comp_hand[indx])
                                    trash.sort()
                                    comp_hand.pop(indx)
                                    comp_hand.append(deck[0])
                                    print("Trash :", trash)
                                    return True
                else:
                    for j in range(len(stack[0])):
                        if i[1] == stack[0][j][1]:
                            for k in range(len(stack[1])):
                                if i[1] == stack[1][k][1]:
                                    indx = self.hand.index(i)
                                    bot.update_hand(indx)
                                    deck.remove(deck[0])
                                    trash.append(comp_hand[indx])
                                    trash.sort()
                                    comp_hand.pop(indx)
                                    print("Trash :", trash)
                                    return True
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------------------------------------------------------------------

# This function first randomly assigns all the elements in the list named deck to the list named deck_2.
# Then, it adds all the elements on deck_2 one by one to the list named deck so that the elements of the list are mixed.

def shuffle(deck):
    deck_2 = []
    for i in range(len(deck)):
        rand_number = random.randint(0,len(deck) - 1)
        deck_2.append(deck[rand_number])
        deck.remove(deck[rand_number])
    for i in deck_2:
        deck.append(i)

#--------------------------------------------------------------------------------------------------------------------------------------------------------

# This function prints the main menu.

def print_menu():
    print("Hit 'v' to view the status of the game.")
    print("Hit 't' to spend a tip.")
    print("Hit 's' to try and stack your card.")
    print("Hit 'd' to discard your card and earn a tip.")
    print("Hit 'h' to view this menu.")
    print("Hit 'q' to quit.")

#----------------------------------------------------------------------------------------------------------------------------------------------------------

# This function ensures that when the player tries to stack, after throwing the card in his hand to the required place, a new card is received randomly from the deck.
# If there is no card in the deck, he does not give a new card to the player, but only deletes the discarded card.

def update_hand(hand,deck,num):
    # input: hand to be updated,current deck and the location of the card to be removed
    # output: removed card
    # This function is called when a card is played (either stacked or discarded). It removes
    # the played card from the hand. If there are any cards left in the deck, the top card
    # in the deck is drawn and appended to the hand.
    if not deck:
        hand.remove(hand[num-1])
    else:
        hand.remove(hand[num - 1])
        hand.append(deck[0])
        deck.remove(deck[0])

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

# This function checks whether the player can stack or not, and if the player can stack, adds the card to the deck and prints the cards in the stack.
# Otherwise it adds the card to the trash and reduces lives by 1.


def try_stack(card,stack,trash):
    if card[0] == "w":
        if len(stack[1]) == 0:
            if card[1] == 1:
                stack[1].append(card)
                update_hand(play_hand, deck, indexx_card)
                return False
            else:
                update_hand(play_hand, deck, indexx_card)
                trash.append(card)
                trash.sort()
                return True
        else:
            if card[1] == stack[1][len(stack[1]) - 1][1] + 1:
                stack[1].append(card)
                update_hand(play_hand, deck, indexx_card)
                return False
            else:
                update_hand(play_hand, deck, indexx_card)
                trash.append(card)
                trash.sort()
                return True
    elif card[0] == "b":
        if len(stack[0]) == 0:
            if card[1] == 1:
                stack[0].append(card)
                update_hand(play_hand, deck, indexx_card)
                return False
            else:
                update_hand(play_hand, deck, indexx_card)
                trash.append(card)
                trash.sort()
                return True
        else:
            if card[1] == stack[0][len(stack[0]) - 1][1] + 1:
                stack[0].append(card)
                update_hand(play_hand, deck, indexx_card)
                return False
            else:
                update_hand(play_hand, deck, indexx_card)
                trash.append(card)
                trash.sort()
                return True
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # This function allows the player to discard the cards in player hand to trash increase lives by 1 and, if there is a card in the deck, get a new card.

def discard(card,trash):
    # input: the card to be discarded, the current trash, number of tips
    # output: updated number of tips
    # This function appends the card to the trash, re-sorts it and increases the number of tips by 1.
    # The updated trash and the number of tips are printed.
    trash.append(card)
    trash.sort()
    if not deck:
        play_hand.remove(card)
    else:
        play_hand.remove(card)
        play_hand.append(deck[0])
        bot.update_count_deck(deck[0])
        deck.remove(deck[0])


#-------------------------------------------------------------------------------------------------------------------------------------------------------


print("Welcome! Let's play!")
print_menu()
deck = [['b',1],['b',1],['b',1],['b',2],['b',2],['b',3],['b',3],['b',4],
        ['w',1],['w',1],['w',1],['w',2],['w',2],['w',3],['w',3],['w',4]]
stack = [[],[]] #0 means black, 1 means white
trash = []
lives = 2
tips = 3
shuffle(deck)
# First hands are dealt.
comp_hand = deck[:3]    # TODO: obtain cards (3 cards) from deck
play_hand = deck[3:6]   # TODO: obtain cards (3 cards) from deck
del deck[0:6]
bot = Gamebot(play_hand,stack)  # Gamebot object is created.
turn = 0                        # 0 means player, 1 means computer. So for each game, the player starts.
while True:
    if turn == 0:
        inp = input("Your turn:")
        if inp == 'v':
            print("Computer's hand:", comp_hand)
            print("Number of tips left:", tips)
            print("Number of lives left:", lives)
            print("Current stack:")
            print("Black:", stack[0])
            print("White:", stack[1])
            print("Current trash:", trash)
        elif inp == "t":
            if tips > 0:
                turn = 1        # Switch turns.
                # Take a tip from the player, give it to the bot, update and print the number of tips.
                tip = input("Please enter a tip.")
                bot.get_tip(tip)            #---> It updates self.hand according to the given type
                tips -= 1  # Decrease tips.
            else:
                print("Not possible! No tips left!")
        elif inp == "s":
            indexx_card = int(input("Enter card number."))
            card = play_hand[indexx_card - 1]
            if try_stack(card, stack, trash):   # If player inputs "s",Firstly; player will input a card number and then function named try_stack will work.
                lives -= 1                      # If player can not stack function will return True and lives will decrease by 1.
                print("Trash:",trash)
                print("Lives: ", lives)
            else:                               # If player can stack function will return False and prints current stack and lives as well.
                print("Stack: ",stack)
                print("Lives: ", lives)
            turn = 1        # Switch turns.
            # Take the location of the card to be stacked from the player,
            # update hands and bot's count_deck and try to stack the selected card.
        elif inp == "d":
            discarded_card = int(input("Enter a card number."))
            selected_card = play_hand[discarded_card - 1]
            discard(selected_card,trash)   # If player inputs "d", Firstly ; player will input a card number and then function named discard will work
            tips += 1       # Increase tips.
            print("Trash: ", trash)
            print("Tips: ", tips)
            turn = 1        # Switch turns.
            # Take the location of the card to be discarded from the player,
            # update hands and bot's count_deck and discard the selected card.
        elif inp == "h":
            print_menu()
        elif inp == "q":
            break
        else:
            print("Please enter a valid choice (v,t,s,d,h,q)!")
    else:
        # A minimal strategy of the bot is given.
        # BONUS: Smarter rule sets can be implemented.
        if tips > 0  and len(play_hand)>0:
            # Take a tip from the bot. Update the number of tips. Print both
            # the given tip by the bot and the updated number of tips.
            if not bot.pick_stack():                # If pick_stack returns False pick_discard will work.If not computer will stack and other functions will not work.
                if not bot.pick_discard():          # If pick_discard returns False give_tip will work.If not computer will discard and other function will not work and tips will increase by 1.
                    if not bot.give_tip():          # If give_tip returns False nothing will happen.If not computer will give a tip to user and tips will decrease by 1.
                        pass
                    else:
                        tips -= 1
                else:
                    tips += 1
        else:
            # Check if bot can pick a card to stack.
            # If yes, update comp_hand, bot's hand and bot's count_deck and try to stack the selected card.
            # If no, make bot pick a card to discard. Update comp_hand, bot's hand and bot's count_deck
            # and discard the selected card.
            if not bot.pick_stack():                                                # If pick_stack returns False pick_discard will work.If not computer will stack and other functions will not work.
                if not bot.pick_discard():                                          # If pick_discard returns True it will discard the avaible card and ıncrease tips by 1.
                    random_discard_number = random.randint(0, len(comp_hand) - 1)   # ---> If not, computer will discard a card randomly and ıncrease by 1.
                    trash.append(comp_hand[random_discard_number])
                    bot.update_hand(random_discard_number)
                    tips += 1
                else:
                    tips += 1
        turn = 0        # Switch turns.
    score = sum([len(d) for d in stack])
    if lives == 0:
        print("No lives left! Game over!")
        print("Your score is", score)
        break
    if len(comp_hand+play_hand)==0:
        print("No cards left! Game over!")
        print("Your score is", score)
        break
    if score == 8:
        print("Congratulations! You have reached the maximum score!")
        break