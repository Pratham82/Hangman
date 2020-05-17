import random
from Words import word_list

"""
This is basic hangman game which can be played through command line.
Author: Prathamesh Mali
Date: 17/5/2020
"""
"""
Steps :
1. Take random word from word_list (create method)
2. Create lists for guessed words, letters, correct guesses
3. Take user input for letter or word
4. Main loop: check the word or letter in the random word
5. If guess is correct append it to correct guesses or else guessed list
6. print out remaining tries(the correspomding state)

"""

# Taking random number from the wordlist
def get_random_word():
    secret_word = random.choice(word_list)
    return secret_word.upper()

def play_hangman(secret_word):
    completed_word = "_" *len(secret_word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's start, Hangman!!!")
    print(display_hangman(tries))
    print("Rules: You have to guess the word before the guy gets hanged.(i.e 6 tries)")

    # Start of the main loop
    while not guessed and tries > 0:
        # Getting the number from user
        user_guess = input("Guess a letter or word: ").upper()
        # Condition if the user entered a letter and it's an alphaabet
        if len(user_guess) == 1 and user_guess.isalpha():
            print("Guessed letters:",end=" ")
            for i in guessed_letters:
                print(i,end=" ")
            print()
            # If the the letter is present in the secret_word
            if user_guess in guessed_letters:
                print(f"'{user_guess}' is already guessed.")

            # If the letter is not in the secret word
            elif user_guess  not in secret_word:
                print(f"'{user_guess}' is not in the word.")
                # decrement the no. of tries
                tries -= 1
                # append the word to guessed_words list
                guessed_letters.append(user_guess)
            else:
                # For every correct guess we will add the letter to the completed list
                print(f"Nice, you guessed correct letter. '{user_guess}' is in the word")
                guessed_letters.append(user_guess)

                # Converting the correct_word from string to a list
                completed_word_list = list(completed_word)

                # Getting the list of indices where the letter is present similar to 
                # the secret_word . 
                indices = [i for i, letter in enumerate(secret_word) if letter==user_guess]

                # Replacing the '_" with the user guess
                for index in indices:
                    completed_word_list[index] = user_guess
                
                # Converting list back to string 
                completed_word = "".join(completed_word_list)
                
                # If all the the letters guessed correctly break the loop
                if "_" not in completed_word:
                    guessed =True

        elif len(user_guess) == len(secret_word) and user_guess.isaplha():
            # Checks if the user entered correct word
            if user_guess in secret_word:
                print(f"You already guessed the word {secret_word}")

            # # Checks if the user not entered correct word
            elif user_guess != secret_word:
                print(f"'{user_guess}' is not the correct word")
                tries -= 1
                guessed_words.append(user_guess)
            else:
                guessed = True
                completed_word = user_guess
        
        # Checking if the input is invalid
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(completed_word)
        print("\n")
    
    if guessed:
        print("Great work, you guessed correct word!, you win!!!")
    else:
        print(f"Sorry your tries were exceeded, the word was {secret_word}. Better luck next time!")
    


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


# for making the game continuosly running
def main():
    secret_word = get_random_word()
    play_hangman(secret_word)
    while input("Do you want to play again? Enter 'y' /'n'").upper() =='Y':
        secret_word = get_random_word()
        play_hangman(secret_word)

if __name__ == "__main__":
    main()
