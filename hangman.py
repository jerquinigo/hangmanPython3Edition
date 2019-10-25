
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

#for debugging purposes
#print(gameWord, "the current game word")


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
    #debugging purposes
    #print(count, "the current count")

    if userInput in newSet:
        for i in range(len(userWord)):
            if userWord[i] == userInput:
                gameWord[i] = userInput
                count = count + 1
                presentGameWord =" ".join(gameWord)


    else: 
         losingCount = losingCount + 1
         print(losingCount, " the current losing count")

    if losingCount == 0:
     print(""" 
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
        print("""
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
        print( """
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
        print( """
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
        print( """
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
        print( """
        _.---,._,'
       /' _.--.<
         /'     `'
       /' _.---._____
       \.'   ___, .-'`
           /'    \\             .
         /'       `-.          -|-
        |                       |
        |                   .-'~~~`-.
        |                 .'         `.
        |                 |  R  I  P  |
        |                 |           |
        |                 |           |
         \              \\|           |//
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        """)
    print(presentGameWord)


if count == len(gameWord):
    print("congratulations! you won the game")
if(losingCount == 5):
    print("sorry, you lost the game, try again")




