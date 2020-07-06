# def generatePassword(pass_length = 8, number_amount = 0):
#     stringOfEverything = f'{string.ascii_letters}{string.digits}{string.punctuation}'
#     listOfEverything = list(stringOfEverything)
#     #possibly an unnecessary while loop (Sam) though I think it didn't work without this if length was over string lenght
#     # while len(listOfEverything) < pass_length: 
#     #     listOfEverything += listOfEverything
#     random.shuffle(listOfEverything) # possibly unnecessary but double randoming seems safer idk
#     random_password = []
#     while len(random_password) < pass_length:
#         random_password += random.choices(listOfEverything, k=1)
#     random_password = ''.join(random_password)
#     return random_password
