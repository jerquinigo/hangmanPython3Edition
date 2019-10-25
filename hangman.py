# old game logic. Player two inputs their words to play
# words = [ "cat", "dog", "tea", "rabbit", "python",]

# import random
# import time
# compChoice = random.choice(words)

gameTries = 5
guesses = ""

print("""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    
""")

userWordInput = input("please enter a word: ")
userWord = userWordInput.lower()

def split(word):
    newList = []
    for char in word:
        newList.append(char)
    return newList

gameWord = split(userWord)
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
losingCount = 0

newSet = set(userWord)



presentGameWord = 0
while count < len(gameWord) and losingCount < 5:
    userInput = input("please enter a letter: ")
    userInput = userInput.lower()
    print(userInput, "lowered the input")
    print(count, "the current count")

    if userInput in newSet:
        for i in range(len(userWord)):
            if userWord[i] == userInput:
                gameWord[i] = userInput
                count = count + 1
                presentGameWord =" ".join(gameWord)


    else: 
         print(userInput, "the user input")
         print("not in ")
         losingCount = losingCount + 1
         print(losingCount, "loser")

    if losingCount == 0:
     print(presentGameWord,""" 
    _________
    |/        
    |              
    |          
    |                 
    |               
    |                   
    |___ 
    """)

    if losingCount == 1:
        print(presentGameWord,"""
     _________       
    |/   |              
    |   (_)
    |                         
    |                       
    |                         
    |                          
    |___  
        """)

    if losingCount == 2:
        print(presentGameWord, """
     ________               
    |/   |                   
    |   (_)                  
    |    |                     
    |    |                    
    |                           
    |                            
    |___  
        """)

    if losingCount == 3:
        print(presentGameWord, """
    _________              
    |/   |                     
    |   (_)                     
    |   /|\                    
    |    |                       
    |                             
    |                            
    |___ 
        """)

    if losingCount == 4:
        print(presentGameWord, """
     ________                   
    |/   |                         
    |   (_)                      
    |   /|\                             
    |    |                          
    |   /                            
    |                                  
    |___ 
        """)

    if losingCount == 5:
        print(presentGameWord, """
     ________
    |/   |     
    |   (_)    
    |   /|\           
    |    |        
    |   / \        
    |               
    |___  
        """)
    print(presentGameWord)


if count == len(gameWord):
    print("congratulations! you won the game")
if(losingCount == 5):
    print("sorry, you lost the game, try again")




