import random

#importing the words and picking a random word for the game
from hangman_words import word_list

chosen_word = random.choice(word_list)

#importing the logo, image, start, and rules of the game for better user experience
from hangman_art import logo

print(logo)
from hangman_art import image

print(image)
from hangman_art import start

print(start)
from hangman_art import description

print(description)

#print(chosen_word)
#Displaying how many letters are there in the word.
display = []
for i in range(len(chosen_word)):
    display += "_"

#GAME BODY
end_of_game = False
from hangman_art import stages

lives = 6
while not lives == 0:  #game continues as long as the lives is greater than 0
    while not end_of_game:
        print(stages[lives])
        print(f"Lives left = {lives}\n"
              )  #Printing the image and the lives left for every guess
        print(
            f"{' '.join(display)}\n"
        )  #Printing the letters that were correctly guessed in the blanks
        guess = input(
            f"Guess a letter. The word has {len(chosen_word)} letters. "  #Ask the user to guess a letter
        ).lower()
        if guess in display:
            print("\nYou already guess the letter."
                  )  #Telling the user if they already guessed the letter
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = chosen_word[
                    i]  #Replacing the guessed letter of the chosen word on the blanks if the user is right
        if guess not in chosen_word:  #Decreasing the lives of the user everytime he is incorrect. Which includes if guessed letter is already repeated
            lives -= 1

        if "_" not in display:
            end_of_game = True
            #Printing the chosen word and congratulating the user if guessed all the letters
            print(f'\nYou guessed the correct word! "{chosen_word}"')
            from hangman_art import win
            print(win)

        if lives == 0:  #Stop the game if no lives left
            end_of_game = True
            print(stages[0])
            print(f"Lives left = {lives}")
            #Printing the chosen word and displaying game over
            from hangman_art import gameover
            print(gameover)
            print(f'\nThe correct word is: "{chosen_word}"')