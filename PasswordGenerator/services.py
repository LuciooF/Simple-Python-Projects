import string
import random

def getUserInputAndSeeIfValidReturnPassLength():
    dud = False
    while dud == False:
        userInput = (input("How long do you want the password to be? "))
        try:
            userInput = int(userInput)
            if userInput > 0:
                if userInput > 20:
                    confirm = (input("Are you sure you want to do this (y/n)?"))
                    if confirm == "y":
                        dud = True
                    else:
                        pass
                else:    
                    dud = True
            else:
                print("thats not a valid number are you stupid - Try again you numpty")
        except ValueError:
            print("thats not a valid number are you stupid - Try again you numpty")
    if userInput > 0:
        return userInput
    else:
        raise TypeError("Invalid User Input, stoopid")      



def generatePassword(pass_length = 8):
    StringOfEverything = f'{string.ascii_letters}{string.digits}{string.punctuation}'
    listOfEverything = list(listOfEverything)
    random.shuffle(listOfEverything) # possibly unnecessary but double randoming seems safer idk
    while len(listOfEverything) < pass_length:
        listOfEverything += listOfEverything
    random_password = random.choices(listOfEverything, k=pass_length)
    random_password = ''.join(random_password)
    return random_password
