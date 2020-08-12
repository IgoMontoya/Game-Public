print ("Welcome to Chose your own adventure python edition")
print ("")

### making this a global, because we will be using it elsewhere and I don't want to overwhelm
### you with classes and the like. Though technically the entire Game should be wrapped up in 
### it's own class for easier mutablility
players = []
### protip, lists in python are not guaranteed to be in the correct order... ###

playerCharacters = []

def playerNames():
    playerNum = int(input("How many players are playing? "))
    if playerNum > 4:
        print("I am sorry, unfortunately only four players are permitted.")
        """ No sense engaging in the next step if the data is invalid """
        return


    for playerId in range(playerNum):
        """ Using the {} modifier makes strings a little easier to concatenate"""
        newPlayerName = input("What is player {}'s name? ".format(playerId + 1));
        players.append(newPlayerName)
    print("Welcome: {} !".format(" & ".join(players)));

def characters():
    """ good ole enumerate, makes a list that doesn't respect order and 
        forces it to give me an index that I can use. What a scrub """
    for index, player in enumerate(players):
        print(player)
        """ Nerdage Moment: when you are asking someone a Yes or No Question in the terminal it's
            a good idea to specify the expected inputs. In this case the Y is capitalized so that 
            the user will know that is the default... I spend WAAAAAAY to much time in the Terminal"""
        playerCreate = input("{} (player {}), do you have a character to create. (Y/n)".format(
            player, str(index+1)))
            
        """ I don't know enough about Python to know a better way to implement default from user input,
            this solution will assume that ANY input is valid other than N or n """
        if playerCreate.lower() == "n":
            print("well I don't know how you intend to play then")
            continue

        getCharName = input("Enter Next Char name ")
        getCharDice = input("Please enter the number of dice this char will use. ")
        getCharRole = input("Please enter the villagers role. ")

        charData = {
            "name": getCharName,
            "diceCount": getCharDice,
            "role": getCharRole,
            "playerName": player
        }
        
        ### Now, I know what you may be thinking. Character.__init__ expects two parameters
        ### but you are only providing one. You are correct! The self property is passed in
        ### automagically! Also, python allows us to specify what Param we want the data to
        ### be interpretted as. Which is something I wish other languages would allow me to
        ### do... Looking at you node.js...
        newCharacter = Character(characterData=charData)
        newCharacter.printSummary()
        playerCharacters.append(newCharacter)


    return
### We are going to treat a character as an object because specific outcomes would happen to a
### particular character. It doesn't quite make sense to iterate through a list of dicts
### and it's easier to ensure that data is manipulated in a way that is more controlled
### if you aren't sure what a class/object is like I would definitely research it, maybe 
### checkout sentdex's channel on YouTube.

### I would recommend moving this to another file as well...
class Character:
    
    """ These are going to be the default values, however you don't 
        need to declare every available variable. It's just a way to 
        ensure you aren't trying to manipulate a variable that isn't set"""
        
    name = "default name"
    playerName = "john/jane doe"
    diceCount = "1"
    role = "vanillaPaste"

    """ This is called when we declare a new character, 
        we need to pass the data from another function"""
    def __init__(self, characterData):
        print(characterData)

        """ I am going to assume that characterData is a dictionary of values that should
            be applied to a character. I would use kwargs, but that may be a bit confusing."""
        
        self.playerName = characterData['playerName']
        """ would recommend validating the player role to be only what is allowed by the game
            however I am too lazy to implement this myself."""
        self.role = characterData['role']
        self.diceCount = characterData['diceCount']
        self.name = characterData['name']

    def printSummary(self):
        print("Character Name: {characterName} \r\nPlayed By: {player}\r\nDice: {dice} \r\nRole: {role}"
                .format(
                    characterName=self.name, 
                    player=self.playerName,
                    dice=self.diceCount,
                    role=self.role));


playerNames()
characters()
