import services
import Word

#random_word = words.

#Generate random word

#get user input

# validate user input

#check if user letter is in random word

#calculate lives 

#win/lose/try again
67
#mini UI from google yaes <3



word = Word.makeArrayOutOfWordString()
services.play(word)
while input("Play Again? (Y/N) ").upper() == "Y":
    word = services.get_word()
    services.play(word)
