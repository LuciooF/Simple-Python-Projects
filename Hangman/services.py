import string
import config


def play(random_word):

    word_completion = "_" * len(random_word)
    guessed = False
    guessed_letters = []

    games_completed = config.add_game()


    tries = 6  # ?
    print("Play hangman lad")
    print(f"{word_completion}")
    while not guessed and tries > 0:
        guessed = GetAndvalidateInput()  # \t \t {GetAndReturnGuessedLetters(guessed, guessed_letters)}
        print(display_hangman(tries))
        # print("\t \t Letters Guessed")
        print("\n")
        if guessed in guessed_letters:
            print("You already guessed this, stoopid")
            guessed = False
            string_guessed_letters = " ".join(guessed_letters)
            print(f"{word_completion} \t {string_guessed_letters}")
        elif guessed not in random_word:
            print("That letter is not in the word lad")
            tries -= 1
            guessed_letters.append(guessed)
            string_guessed_letters = " ".join(guessed_letters)
            guessed = False
            print(display_hangman(tries))
            print(f"{word_completion} \t {string_guessed_letters}")
        else:
            guessed_letters.append(guessed)
            word_as_list = list(word_completion)
            indices = [i for i, letter in enumerate(random_word) if letter == guessed]
            print("nice lad, that leter do be in the word lad")
            for index in indices:
                word_as_list[index] = guessed
            word_completion = "".join(word_as_list)
            string_guessed_letters = " ".join(guessed_letters)
            print(f"{word_completion} \t {string_guessed_letters}")
            if "_" not in word_completion:
                guessed = True
            if "_" in word_completion:
                guessed = False
                continue
        if guessed:
            games_won = config.add_win()
            win_percentage = config.calculate_win_percentage()

            print("yay you've guessed the word, congrats")
            print(display_hangman(tries))
            print(f"Games played: {games_completed}")
            print(f"Number of wins: {games_won}  Percentage of games won: {win_percentage}% \nGames played: {games_completed}")
        if guessed is False and tries < 1:
            games_won = config.add_loss()
            win_percentage = config.calculate_win_percentage()

            print(display_hangman(tries))
            print(f"You've lost, the word was {random_word}")
            print(f"Games played: {games_completed}")
            print(f"Number of wins: {games_won}  Percentage of games won: {win_percentage}% \nGames played: {games_completed}")


def GetAndvalidateInput():
    validity = False
    while not validity:
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