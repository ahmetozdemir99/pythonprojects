import random
import numpy as np
from matplotlib import pyplot as plt

N = [10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000]
num_of_dice = 5

        # I will add to the list of Probs1 the ratios from the last experiment after the experiments as many as the numbers in the N list.
probs_P1 = []
probs_P2 = []
probs_P3 = []
P1_Teorical_List = []
P2_Teorical_List = []
P3_Teorical_List = []

# Theorical Probability of P1
        # If we subtract the undesired situation from 1, we get the result. So  - (the probability that none of the rolled dice is 3)
        # The probability that one dice is not  3 is (5/6)
        # For 5 dice ; the probability that none of the rolled dice is 3, (5/6) ** numberOfDices
def calculate_Theorical_Probability_P1():
    diceIsnot3_prob = 5/6
    return 1 - (diceIsnot3_prob ** num_of_dice)



# Theorical Probability of P2
    # P(A|B) = P(A ∩ B) / P(B)
    # P(A n B) = P(A) + P(B) - ( P(A) + P(B) - P(A n B) )
    # Event A is that at least one of the dice 3. (           --> 1 - ( there is no 3 dice.))  ### Probability of no dice rolling a three = (5/6) ** dicenumber
    # Event B is knowing that one of the dice is definitely even. --> 1 - ( all dices are odd.) ### Probability of all dices are odd = ( ( number of odd numbers between 1-6 ) / 6  ) ** dicenumber ## = (3/6)**dicenumber
    # Prob A intersection B is          P(A) + P(B) - P(AUB)
    # We know that this probability is a conditional probability, so we should find P(A|B)
    #
def calculate_Theorical_Probability_P2():
    prob_Of_a_Event = 1 - ((5/6) ** num_of_dice)
    prob_Of_a_union_b_Events  =  1 - ((1 - (4/6))**num_of_dice)  # 1 - (prob of (There wont be even and there wont be three)) P(AUB) = 1 - P(A' n B') ## --> P(A' n B') = 1 - (1 - (4/6))**dicenumber.
    prob_Of_b_Event = 1 - ((3/6)**num_of_dice)
    theorical_Prob_P2 = (prob_Of_a_Event + prob_Of_b_Event - prob_Of_a_union_b_Events) / prob_Of_b_Event
    return theorical_Prob_P2



    # If we know that only one dice is definitely even, then there are 4 dice left, and we have to calculate the probability of at least 1 of them rolling a 3.
    # If we want to calculate the probability that at least one of them will roll a 3 when we roll the remaining 4 dice, we need to subtract the probability of no 3 from the whole situation.
    # So the probability of not getting any 3 is equal to (2/3) **Num_Dice
    # So the probability we are looking for is equal to --> 1 - (2/3)**(dicenum-1)  #### (dicenum - 1 ) because we already know that a dice rolles even.
def calculate_Theorical_Probability_P3():
    return 1 - (2/3)**(num_of_dice-1)





def get_Experimental_Prob(counter_of_ones,experimental_Results_List):
    if len(experimental_Results_List) != 0:
        return counter_of_ones/len(experimental_Results_List)




# This function generates random numbers between 1 and 6 and assigns them to the list. So we can think of it as rolling 5 dice.
def roll_dice(numberOfDice):
    dices_List = []
    for i in range(numberOfDice):
        number = random.randint(1, 6)
        dices_List.append(number)
    return dices_List


# Experiments for All of probabilities...

for number_Of_Experiments in N:
    P1_Experiments_List = []
    P2_Experiments_List = []
    P3_Experiments_List = []
    probs_After_Multiple_Experiments_P1 = []
    probs_After_Multiple_Experiments_P2 = []
    probs_After_Multiple_Experiments_P3 = []
    counter_Of_Ones_P1 = 0
    counter_Of_Ones_P2 = 0
    counter_Of_Ones_P3 = 0
    for number_Of_Dice_Rolled in range(number_Of_Experiments):
        rolled_Dices_List = roll_dice(num_of_dice)
        counter_of_Threes = 0
        counter_of_Evens = 0
        for i in rolled_Dices_List:
            if i == 3:
                counter_of_Threes += 1
            if i % 2 == 0:
                counter_of_Evens += 1

        if counter_of_Threes > 0:
            P1_Experiments_List.append(1)
            counter_Of_Ones_P1 += 1
        else:
            P1_Experiments_List.append(0)


        if counter_of_Evens >= 1:
            if counter_of_Threes > 0:
                P2_Experiments_List.append(1)
                counter_Of_Ones_P2 += 1
            else:
                P2_Experiments_List.append(0)


        if counter_of_Threes > 0:
            if counter_of_Evens == 1:
                P3_Experiments_List.append(1)
                counter_Of_Ones_P3 += 1
            else:
                number_Of_Dice_Rolled -= 1
        elif counter_of_Threes == 0:
            if counter_of_Evens == 1:
                P3_Experiments_List.append(0)
            else:
                number_Of_Dice_Rolled -= 1

        probs_After_Multiple_Experiments_P1.append(get_Experimental_Prob(counter_Of_Ones_P1,P1_Experiments_List))
        probs_After_Multiple_Experiments_P2.append(get_Experimental_Prob(counter_Of_Ones_P2,P2_Experiments_List))
        probs_After_Multiple_Experiments_P3.append(get_Experimental_Prob(counter_Of_Ones_P3,P3_Experiments_List))
    P1_Teorical_List.append(calculate_Theorical_Probability_P1())
    P2_Teorical_List.append(calculate_Theorical_Probability_P2())
    P3_Teorical_List.append(calculate_Theorical_Probability_P3())
    probs_P1.append(probs_After_Multiple_Experiments_P1[-1])
    probs_P2.append(probs_After_Multiple_Experiments_P2[-1])
    probs_P3.append(probs_After_Multiple_Experiments_P3[-1])


print("Theorical Probability of P1 is : %",calculate_Theorical_Probability_P1())
print("Experimental Probability of P1 after 100000 experiment is : %",probs_P1[-1])
print("Theorical Probability of P2 is : %",calculate_Theorical_Probability_P2())
print("Experimental Probability of P2 after 100000 experiment is : %",probs_P2[-1])
print("Theorical Probability of P3 is : %",calculate_Theorical_Probability_P3())
plt.plot(N, probs_P1,N,probs_P2,N,probs_P3,N,P1_Teorical_List,N,P2_Teorical_List,N,P3_Teorical_List)
plt.tight_layout()
plt.xscale("log")
plt.legend(["Experimental Probability of P1","Experimental Probability of P2","Experimental Probability of P3","Theorical Probability of P1","Theorical Probability of P2","Theorical Probability of P3"])
plt.show()