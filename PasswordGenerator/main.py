import random
import string
import services


passwordInfo = services.getUserInputAndSeeIfValidReturnPassLength()
generatedPassword = services.generatePassword(passwordInfo.userinput, passwordInfo.amountOfNumbers)


print("Your generated password is: {}".format(generatedPassword))
