words = [ "cat", "dog", "tea"]

import random
import time
compChoice = random.choice(words)

gameTries = 5
guesses = ""


def split(word):
    newList = []
    for char in word:
        newList.append(char)
    return newList

gameWord = split(compChoice)
print(gameWord, "the current game word")


# this turns the list into a string, but since string are not mutable directly, i will continue to work using list
#gameWord = ''.join(map(str, gameWord))
#print(gameWord, "the new game word")
# end of list to string conversion.


for i in range (len(gameWord)):
    gameWord[i] = "_"

    

# turns the list back into a string
print(" ".join(gameWord))

count = 0

while count < len(gameWord):
    userInput = input("please enter a letter: ")
    userInput = userInput.lower()
    print(userInput, "lowered the input")
    print(count, "the current count")

    for i in range(len(compChoice)):
        if compChoice[i] == userInput:
            gameWord[i] = userInput
            count = count + 1

print(" ".join(gameWord))