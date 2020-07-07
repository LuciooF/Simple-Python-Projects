import string
import random
class Password:
    def __init__(self, userinput, amountOfNumbers):
        self.userinput = userinput
        self.amountOfNumbers = amountOfNumbers
def getUserInputAndSeeIfValidReturnPassLength():
    nul = False
    while nul == False:
        dud = False
        while dud == False:
            userInput = (input("How long do you want the password to be? "))
            try:
                userInput = int(userInput)
                if userInput > 0:
                    if userInput > 1000:
                        print("That's far too long")
                        continue
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
                dud = False
        user_number = (input("How many numbers do you want in it? "))
        try:
            user_number = int(user_number)
            if user_number >= 0 and user_number < (userInput + 1):
                pass
            else:
                print("thats not a valid number are you stupid - Try again you numpty")
                continue
        except ValueError:
            print("thats not a valid number are you stupid - Try again you numpty")
            continue
        if userInput > 0:
            password = Password(0,0)
            password.userinput = userInput
            password.amountOfNumbers = user_number
            return password
            nul = True
        else:
            raise TypeError("Invalid User Input, stoopid")
# Currently possibly insecure as there will only be one letter of each, in case of a web attack it'd be easier to hack this. Need to make so it picks one random from listof everything everytime, with foreach
def generatePassword(pass_length = 8, pass_number = 9):
    stringOfEverything = f'{string.ascii_letters}{string.punctuation}'
    string_of_numbers = f'{string.digits}'
    list_of_numbers = list(string_of_numbers)
    listOfEverything = list(stringOfEverything)
    #possibly an unnecessary while loop (Sam) though I think it didn't work without this if length was over string lenght
    # while len(listOfEverything) < pass_length:
    #     listOfEverything += listOfEverything
    random.shuffle(listOfEverything)
    random.shuffle(list_of_numbers) # possibly unnecessary but double randoming seems safer idk
    random_password = []
    while len(random_password) < (pass_length - pass_number):
        random_password += random.choices(listOfEverything, k=1)
    while len(random_password) < (pass_length):
        random_password += random.choices(list_of_numbers, k=1)
    random.shuffle(random_password)
    random_password = ''.join(random_password)
    return random_password