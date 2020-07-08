import services
#random_word = words.

#Generate random word

#get user input

# validate user input

#check if user letter is in random word

#calculate lives 

#win/lose/try again

#mini UI from google yaes <3



word = services.get_word()
services.play(word)
while input("Play Again? (Y/N) ").upper() == "Y":
    word = services.get_word()
    services.play(word)
