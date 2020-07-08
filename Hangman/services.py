import string
#from PyDictionary import PyDictionary

def get_word():
    return "Oliver".upper()#PyDictionary()
   #gets random word from somewhere


def play(random_word):
    word_completion = "_" * len(random_word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6 #?
    while not guessed and tries > 0:
        print("Play hangman lad")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
        guessed = GetAndvalidateInput()
        if guessed in guessed_letters:
            print("You already guessed this, stoopid")
        elif guessed not in random_word:
            print("That letter is not in the word lad")
            tries = tries - 1
            guessed_letters.append(guessed) #add equivalent in python? need to google 
            continue
        else:
                print("nice lad, that leter do be in the word lad")
                guessed_letters.append(guessed)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(random_word) if letter == guessed]
                for index in indices:
                    word_as_list[index] = guessed
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
                if "_" in word_completion:
                    guessed = False
                    continue
        if guessed == True:
           print("yay you've guessed the word, congrats")
            
        

def GetAndvalidateInput():
    validity = False
    while validity == False:
        user_input = input("Guess a letter big boy: ")
        list_of_letters = list(string.ascii_letters)
        validity = True
        user_input = str(user_input)
        if user_input not in list_of_letters:
            print("Invalid guess")
            validity = False
        else:
            return user_input.upper()
    
      


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
            """
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |     / \\
                -
            """,
            # head, torso, both arms, and one leg
            """
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |     / 
                -
            """,
            # head, torso, and both arms
            """
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |      
                -
            """,
            # head, torso, and one arm
            """
                --------
                |      |
                |      O
                |     \\|
                |      |
                |     
                -
            """,
            # head and torso
            """
                --------
                |      |
                |      O
                |      |
                |      |
                |     
                -
            """,
            # head
            """
                --------
                |      |
                |      O
                |    
                |      
                |     
                -
            """,
            # initial empty state
            """
                --------
                |      |
                |      
                |    
                |      
                |     
                -
            """
    ]
    return stages[tries]
