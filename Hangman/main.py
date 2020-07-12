import services
import Word

#random_word = words.

#Generate random word

#get user input

# validate user input

#check if user letter is in random word

#calculate lives

#win/lose/try again
#mini UI from google yaes <3


loop = False
while not loop:
    word = Word.GetRandomWord()
    services.play(word)
    # while input("Play Again? (Y/N) ").upper() == "Y":
    #     break
    # while input("Play Again? (Y/N) ").upper() == "N":
    #     loop = True
    #     break
    # continue
    while True:
        play_again_input = input("Play Again? (Y/N) ").upper()
        if play_again_input == "Y":
            break
        elif play_again_input == "N":
            loop = True
            break
        else:
            print("Invalid input")
print("Thanks for playing, have a great day!")