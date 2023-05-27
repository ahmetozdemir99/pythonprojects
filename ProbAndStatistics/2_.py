# Ahmet Özdemir
# 270201050
# CENG222_HomeWork-2
#-----------------------------------------------------------------------------------------------------------------------

import random
import numpy as np
import matplotlib.pyplot as plt
import numpy as geek
import math

#-----------------------------------------------------------------------------------------------------------------------
#   This function generates a random float between 0 and 1.

def generateFloat():
    return random.random()

#-----------------------------------------------------------------------------------------------------------------------
#   This function creates a random float between the entered parameters (a-b).

def generateNumber(x,y):
    return random.uniform(x,y)

#-----------------------------------------------------------------------------------------------------------------------
#   This function provides that the totals from the entered experiments are stored in a list.

def generateSums(x):
    list = []
    for i in range(200000):
        sum = 0
        for j in range(x):
            sum += generateFloat()
        list.append(sum)
    return list

#-----------------------------------------------------------------------------------------------------------------------
#   This function provides that the totals from the entered experiments are stored in a list.

def calculateExperiment(number):
    if number == 1:
        return generateSums(2)
    elif number == 2:
        return generateSums(4)
    elif number == 3:
        return generateSums(50)
    elif number == 4:
        listOfSums = []
        for i in range(200000):
            sum = 0
            randomNumber = generateNumber(0, 200)
            previousNumber = randomNumber
            for j in range(50):
                if previousNumber < 99:
                    previousNumber = generateNumber(0, 200)
                    sum += previousNumber
                else:
                    previousNumber = generateNumber(98, 102)
                    sum += previousNumber
            listOfSums.append(sum)
        return listOfSums
    elif number == 5:
        listOfSums2 = []
        for i in range(200000):
            sum = 0
            for j in range(50):
                a = np.random.uniform()
                b = np.random.uniform()
                sum += np.random.uniform(a, b - a)
            listOfSums2.append(sum)
        return listOfSums2
                

#-----------------------------------------------------------------------------------------------------------------------
#   This function calculates the mean of that experiment according to the entered experiment number.

def calculateMean(x):
    sum = 0
    for i in calculateExperiment(x):
        sum += i
    mean = sum / len(calculateExperiment(x))
    return mean

#-----------------------------------------------------------------------------------------------------------------------
#   This function finds the standard deviation of the experiment whose experiment number is entered.

def calculateStandardDeviation(x):
    mean = calculateMean(x)
    sum = 0
    for i in calculateExperiment(x):
        sum += (i - mean) ** 2
    standardDeviation = (sum / (len(calculateExperiment(x)) - 1)) ** 0.5
    return standardDeviation

#-----------------------------------------------------------------------------------------------------------------------
#   This function generates horizontal axes for that experiment according to the entered experiment.

def generateHorizontalAxises(number):
    if number == 1:
        x = geek.linspace(0,2,200000)
        return x
    elif number == 2:
        x = geek.linspace(0,4, 200000)
        return x
    elif number == 3:
        x = geek.linspace(0, 50, 200000)
        return x
    elif number == 4:
        x = geek.linspace(0, 6000, 200000)
        return x
    elif number == 5:
        x = geek.linspace(0,max(calculateExperiment(5)),200000)
        return x

#-----------------------------------------------------------------------------------------------------------------------
#   This function returns the vertical axis values corresponding to the horizontal axis values to create the curve.

def generateVerticalAxises(expNumber):
    verticalAxisesList = []
    x = generateHorizontalAxises(expNumber)
    deviation = calculateStandardDeviation(expNumber)
    mean = calculateMean(expNumber)
    for horizontalAxis in x:
        verticalAxisesList.append((1 / (deviation * ((2 * math.pi) ** 0.5)) * (
            math.exp(-((horizontalAxis - mean) ** 2) / (2 * (deviation ** 2))))))
    return verticalAxisesList

#-----------------------------------------------------------------------------------------------------------------------
#   This function allows the experiment-1 to be plotted graphically.

def experiment1():
    plt.plot(generateHorizontalAxises(1), generateVerticalAxises(1), label = "Normal Distribution")
    plt.title("Experiment 1")
    plt.hist(calculateExperiment(1), 100, density=True, label = "Histogram")
    plt.legend()
    plt.show()

#-----------------------------------------------------------------------------------------------------------------------
#   This function allows the experiment-2 to be plotted graphically.

def experiment2():
    plt.plot(generateHorizontalAxises(2), generateVerticalAxises(2), label = "Normal Distribution")
    plt.title("Experiment 2")
    plt.hist(calculateExperiment(2), 100, density=True, label = "Histogram")
    plt.legend()
    plt.show()

#-----------------------------------------------------------------------------------------------------------------------
#   This function allows the experiment-3 to be plotted graphically.

def experiment3():
    plt.plot(generateHorizontalAxises(3), generateVerticalAxises(3), label = "Normal Distribution")
    plt.title("Experiment 3")
    plt.hist(calculateExperiment(3), 100, density=True,label="Histogram")
    plt.legend()
    plt.show()

#-----------------------------------------------------------------------------------------------------------------------
#   This function allows the experiment-4 to be plotted graphically.

def experiment4():
    plt.plot(generateHorizontalAxises(4), generateVerticalAxises(4), label = "Normal Distribution")
    plt.title("Experiment 4")
    plt.hist(calculateExperiment(4), 100, density=True, label="Histogram")
    plt.legend()
    plt.show()

#-----------------------------------------------------------------------------------------------------------------------
#   This function allows the experiment-5 to be plotted graphically.
def experiment5():
    plt.plot(generateHorizontalAxises(5), generateVerticalAxises(5), label="Normal Distribution")
    plt.title("Experiment 5")
    plt.hist(calculateExperiment(5), 100, density=True, label="Histogram")
    plt.legend()
    plt.show()

#-----------------------------------------------------------------------------------------------------------------------
#   This function plots all of the experiment results.

def mainApp():
    experiment1()
    experiment2()
    experiment3()
    experiment4()
    experiment5()

#-----------------------------------------------------------------------------------------------------------------------

mainApp()
