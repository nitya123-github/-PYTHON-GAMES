import os
import re
import random
os.system('cls' if os.name=='nt' else 'clear')
while (1 < 2):
    print ("\n")
    print ("Rock, Paper, Scissors - Shoot!")
    userChoice = input("Choose your weapon [R]ock], [P]aper, or [S]cissors ")
    if not re.match("[SsRrPpWw]", userChoice):
        print( "Please choose a letter:")
        print ("[R]ock, [S]cissors or [P]aper .")
        continue
    #Echo the user's choice
    print ("You chose: " + userChoice)
    choices = ['R', 'P', 'S']
    opponenetChoice = random.choice(choices)
    print ("I chose: " + opponenetChoice)
    if opponenetChoice == str.upper(userChoice):
        print ("Tie! ")
    #if opponenetChoice == str("R") and str.upper(userChoice) == "P"
    elif opponenetChoice == 'R' and userChoice.upper() == 'S':      
        print ("Rock  beats scissor, I win back off! ")
        continue
    elif opponenetChoice == 'S' and userChoice.upper() == 'P':      
        print( "Scissors beats paper! I win back off! ")
        continue
    elif opponenetChoice == 'P' and userChoice.upper() == 'R':      
        print (" ok Rocks beats paper U win! ")
        continue
    
    else:       
        print ("You win!")
