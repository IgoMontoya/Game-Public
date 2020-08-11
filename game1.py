print ("Welcome to Chose your own adventure python edition")
print ("")

def playerNames():
    playerNum = int(input("How many players are playing? "))
    print(playerNum)
    # Great place to consider using a for loop
    if playerNum == 1:
        player1 = input("What is player one's first name? ")

        print("Welcome ", player1, "!")
    elif playerNum == 2:
        player1 = input("What is player one's first name? ")
        player2 = input("What is player two's first name? ")
        print("Welcome ", player1, "&",  player2, "!")
    elif playerNum == 3:
        player1 = input("What is player one's first name? ")
        player2 = input("What is player two's first name? ")
        player3 = input("What is player three's first name? ")
        print("Welcome ", player1, ",", player2, "&", player3, "!")
    elif playerNum == 4:
        player1 = input("What is player one's first name? ")
        player2 = input("What is player two's first name? ")
        player3 = input("What is player three's first name? ")
        player4 = input("What is player four's first name? ")
        print("Welcome ", player1, ",", player2, ",", player3, ",", player4, "!")
    elif playerNum >= 5:
        print ("I am sorry unfortunately only four players are permitted.")



def characters():

    ### Artibuttes each char will have: Name, Dice(1-2), Acceptable Dice Values(each dice has a seperate value), Role type(Builder,Recruiter,Both(Builder and Recruiter)), current state(available,active, tired, injured),which player controls them(determined by how many players in the game, and if unowned their cost if they are avail for purchase)
    continueCreation = input("do you have a char to create? ").lower()
    charNames = []
    charDice = []
    charRole = []
    if continueCreation == "yes":

        
        getCharNames = input("Enter Next Char name ")
        getCharDice = input("Please enter the number of dice this char will use. ")
        getCharRole = input("Please enter the villagers role. ")
        charNames.append(getCharNames)
        charDice.append(getCharDice)
        charRole.append(getCharRole)
        print (charNames)
        print (charRole)
        print (charDice)
        continueCreationNext = input("Do you have another char to enter? ").lower()
        if continueCreationNext == "yes":
            characters()
        else:
            print("Thanks for entering these chars" )
    else: 
        print("Thanks for entering these chars" )

        
        # diceNumber = int(input("How many dice does this character have? "))

playerNames()
characters()
