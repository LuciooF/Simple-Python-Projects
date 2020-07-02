def ValidateUserInfo(userInput):
    if userInput > 10 or userInput < 0:
        return False #does this return anything ? so in this case a bool but if i wanted its an int? in csharp yiou have to name it
    else: 
        return True