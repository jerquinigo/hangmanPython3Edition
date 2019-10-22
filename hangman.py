words = [ "cat", "dog",]

import random
compChoice = random.choice(words)

gameTries = 5

def split(word):
    newList = [];
    for char in word:
        newList.append(char)
    return newList

gameWord = split(compChoice)
print(gameWord)

correctList = []
wrongList = []
print(len(gameWord))
while gameTries != 0 or len(correctList) - 1 == len(gameWord):
    userInput = input("enter your character ")
    print(userInput, "the input")
    for item in gameWord:
        if(userInput == item):
            correctList.append(userInput)
            print(correctList)
            print(len(correctList))
        else:
            gameTries = gameTries - 1


print(correctList, "in the list")
    
