import random
import string
import services


pass_length = services.getUserInputAndSeeIfValidReturnPassLength()
generatedPassword = services.generatePassword(pass_length)


print("Your generated password is: {}".format(generatedPassword))



