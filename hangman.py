words = [ "cat", "dog",]

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
print(type(gameWord))

# this turns the list into a string, but since string are not mutable directly, i will continue to work using list
#gameWord = ''.join(map(str, gameWord))
#print(gameWord, "the new game word")
# end of list to string conversion.


for i in range (len(gameWord)):
    gameWord[i] = "_"

print(gameWord, "after the loop ")
    

#print(" ".join(gameWord))