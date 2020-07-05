import random
import Services


randomGeneratedNumber = random.randint(1, 10) # takes two args and picks a random number between
userInput = int(input("Pick a number between 1 and 10: ")) # ask for user input and cast to int
isUserInputValid = Services.ValidateUserInfo(userInput)


# guys please send me this manic code once it's finished

if isUserInputValid == False: # like this
    print("Invalid input")
elif randomGeneratedNumber == userInput: # check for equality
    print("Yes!")
else:
    print("No!, the action number was {}".format(randomGeneratedNumber))



# if expression and anotherExpression:
#     pass
# elif expression2 or anotherExpression2:
#     pass
# elif 1 in range(0, 5):
#     pass
# else:
#     whaterv

# def ValudateUserInfo():
#       body 

# if userInput > 10 or userInput < 0: # like this good man Sam
#     print("Invalid input")
# else:
# if randomGeneratedNumber == userInput: # check for equality
#     print("Yes!")
# else:
#     print("No!, the action number was {}".format(randomGeneratedNumber)) #how do i interlapse if's #