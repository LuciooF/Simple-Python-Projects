import string
import random
import Password

def GetUserInputReturnPasswordClass():
    nul = False
    while nul == False:
        dud = False
        while dud == False:
            userInput = (input("How long do you want the password to be? "))
            try:
                userInput = int(userInput)
                if userInput >= 8:                   
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
                    print("thats not a valid number are you stupid - Try again you numpty it has to be at least 8 characters")
            except ValueError:
                print("thats not a valid number are you stupid - Try again you numpty")
                dud = False
        user_number = (input("How many numbers do you want in it? "))
        try:
            user_number = int(user_number)
            if user_number > 0 and user_number < (userInput + 1):
                pass
            else:
                print("thats not a valid number are you stupid - Try again you numpty, need at least 1 number")
                continue
        except ValueError:
            print("thats not a valid number are you stupid - Try again you numpty")
            continue
        if userInput > 0:
            password = Password.Password(0,0)
            password.userinput = userInput
            password.amountOfNumbers = user_number
            return password
            nul = True
        else:
            raise TypeError("Invalid User Input, stoopid")
# Currently possibly insecure as there will only be one letter of each, in case of a web attack it'd be easier to hack this. Need to make so it picks one random from listof everything everytime, with foreach
def generatePassword(pass_length = 8, pass_number = 9, amount_of_punctuation = 1, amount_of_uppercase = 1):

    string_of_lower_letters = f'{string.ascii_lowercase}'
    string_of_upper_letters = f'{string.ascii_uppercase}'
    string_of_punctuation = f'{string.punctuation}'
    string_of_numbers = f'{string.digits}'
    string_of_nonnumbers = f'{string_of_lower_letters}{string_of_upper_letters}{string_of_punctuation}'


    list_of_numbers = list(string_of_numbers)
    list_of_lower_letters = list(string_of_lower_letters)
    list_of_upper_letters = list(string_of_upper_letters)
    list_of_punctutation = list(string_of_punctuation)
    list_of_nonnumbers = list(string_of_nonnumbers)

    random_password = [] 

    random_password += random.choices(list_of_lower_letters, k=1)
    random_password += random.choices(list_of_upper_letters, k=1)
    random_password += random.choices(list_of_punctutation, k=1)

    while len(random_password) < (pass_length - pass_number):
        random_password += random.choices(list_of_nonnumbers, k=1)
    while len(random_password) < (pass_length):
        random_password += random.choices(list_of_numbers, k=1)

    random.shuffle(random_password)
    random_password = ''.join(random_password)
    
    return random_password
    