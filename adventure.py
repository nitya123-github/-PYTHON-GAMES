import random
import time

def displayIntro():
    print("hey its nitya")
    print("seriously, i can tell you what your secrets are...")
    print("i know i sound like a dumb ass!")
    print("you have 2 options trust me ")
    print()

def choosePath():
    path = ""
    while path != "1" and path != "2": # input validation
        path = input("Which path will you choose? (1 or 2): ")

    return path

def checkPath(chosenPath):
    print("You head right path")
    time.sleep(2)
    print("there's good sign and...")
    time.sleep(2)
    print("serously,how can u fell in my trap...")
    print()
    time.sleep(2)

    correctPath = random.randint(1, 2)

    if chosenPath == str(correctPath):
        print("The wizards of the galaxy!")
        print("Welcome home!")
    else:
        print("An extremely energetic burst of gamma rays pass through you")
        print("causing all of the atoms in your body to dissociate")
        print("there is no record left of your existence.")


playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
    displayIntro()
    choice = choosePath()
    checkPath(choice) # choice is equal to "1" or "2"
    playAgain = input("Do you want to play again? (yes or y to continue playing): ")
