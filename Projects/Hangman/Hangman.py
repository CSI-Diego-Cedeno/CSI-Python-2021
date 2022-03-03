import json, ssl
import urllib.request
from Dessert import Dessert

# This is used to prevent errors
ssl._create_default_https_context = ssl._create_unverified_context

def getWord():
    
    # This URL is used to request a word from the class Dessert
    DessertURL = "https://random-data-api.com/api/dessert/random_dessert"
    
    # Here creates a variable to ask for data
    req = urllib.request.Request(DessertURL)
    requestData = json.loads(urllib.request.urlopen(req).read())
    
    # Deserialize into a class
    newDessert:Dessert = Dessert(**requestData)
    return newDessert

# This is the variable created for all the incorrect characters
attemptedCharacter = []

# On this part are the each steps that creates the hangman
Steps = ["""
|---------|
|         |
|         
|
|
|
|
|
""",
"""
|---------|
|         |
|        😂
|         
|
|
|
|
""",
"""
|--------|
|        |
|       😂
|        |
|       
|
|
|
""",
"""
|--------|
|        |
|       😂
|      --|
|        
|        
|
|
""",
"""
|--------|
|        |
|       😂
|      --|--
|        |
|       
|
|
""",
"""
|--------|
|        |
|       😂
|      --|--
|        |
|       / 
|
|
""",
"""
|--------|
|        |
|       😂
|      --|--
|        |
|       / \\
|
|
"""
]

# # This print starts the game
# print(Steps[0])

# # In this part it prints the word that it got from the data and puts each character an _
# print(len(newDessert.variety)*" _ ")

# The function its used so that the game tells you the characters that are errors in the game
def getInput():
    while(True):
        
      # ask for input
     Character = input(f"name a letter for this dessert: ")
     special_char = "[@_!#$%^&*()<>?/\|}{~:]"

      # Validate input
     if(len(Character) != 1):
          print("error, just type a letter: ")
          continue

     if(Character.isnumeric()):
         print("error, no numbers, just type a letter: ")
         continue

     if(Character in special_char):
        print("Error, no special character, just type a letter: ")
        continue
    
    # This is for used character that were typed
     attemptedCharacter.append(Character)
     return Character

# This function is used so that it stores every correct Character that you type
def print_word():
    Temp:str = " "
    for Character in newDessert.variety:
        if Character in attemptedCharacter:
            Temp +="_"
        else:
            Temp += Character
    print(Temp)

# This is used to store the erros you do when putting the Character, the function adds 1 to each one you get wrong
def Print_stepsErrors(Character,attemptedCharacter):
    error = 0
    for Character in attemptedCharacter:
        if(Character not in attemptedCharacter):
            error = error + 1
    print(Steps[error])


# The following part is the while True which will keep the game going and the game restarts
while True: 
    newDessert = getWord()
    attemptedCharacter = []
    
    while True:
        
        print_word()
        
        char = getInput()
        Print_stepsErrors(char,attemptedCharacter)
        # if()  :
            # break   


